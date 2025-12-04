import subprocess
import tempfile
import json
import traceback
import os
import re
import uuid
from termcolor import colored
from typing import Optional, Dict, Any

from ProAgent.n8n_tester.credential_loader import credentials
from ProAgent.n8n_parser.node import n8nPythonNode
from ProAgent.n8n_tester.pseudo_node.run_pseudo_node import run_pseudo_workflow
from ProAgent.n8n_tester.prompts import success_prompt, error_prompt


class n8nRunningException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.code_stack = []
        self.error_message = message

    def add_context_stack(self, code_context):
        self.code_stack.append(code_context)


class anonymous_class():
    def __init__(self, node: n8nPythonNode, *args, **kwargs):
        self.node = node

    def run(self, input_data, params):
        output_data, error = run_node(node=self.node, input_data=input_data)
        if error:
            raise n8nRunningException(error)
        return output_data


def _get_constant_workflow(input_data):
    """Generates a workflow with Start -> Code (Inject Data) -> Target Node"""
    node_start_name = "Start"
    node_code_name = "Code_Inject_Data"
    node_target_name = "Target_Node"

    # 1. Start Node (Required for full workflow execution)
    node_start = {
        "id": str(uuid.uuid4()),
        "name": node_start_name,
        "type": "n8n-nodes-base.start",
        "typeVersion": 1,
        "position": [0, 0],
        "parameters": {}
    }

    # 2. Code Node to inject input data
    js_code = f"return {json.dumps(input_data)};"
    node_code = {
        "id": str(uuid.uuid4()),
        "name": node_code_name,
        "type": "n8n-nodes-base.code",
        "typeVersion": 2,
        "position": [200, 0],
        "parameters": {"jsCode": js_code}
    }

    # 3. Target Node Placeholder (Details filled in run_node)
    node_target = {
        "id": str(uuid.uuid4()),
        "name": node_target_name,
        "position": [400, 0]
    }

    workflow = {
        "name": f"AutoRun_{uuid.uuid4().hex[:8]}",
        "nodes": [node_start, node_code, node_target],
        "connections": {
            node_start_name: {
                "main": [[{"node": node_code_name, "type": "main", "index": 0}]]
            },
            node_code_name: {
                "main": [[{"node": node_target_name, "type": "main", "index": 0}]]
            }
        },
        "active": False,
        "settings": {"executionOrder": "v1"},
        "tags": []
    }
    return workflow


def parse_n8n_output(output_str, target_node_name):
    """Parses the JSON output from n8n execution to find the target node's data."""
    try:
        # Find the JSON object in the stdout (n8n returns objects, not arrays)
        start_idx = output_str.find('{')
        end_idx = output_str.rfind('}') + 1
        if start_idx == -1 or end_idx == 0:
            return []

        json_str = output_str[start_idx:end_idx]
        execution_data = json.loads(json_str)
        
        # Navigate the n8n response structure: data.resultData.runData[target_node_name]
        run_data = execution_data.get("data", {}).get("resultData", {}).get("runData", {})
        target_node_data = run_data.get(target_node_name, [])
        
        if target_node_data and len(target_node_data) > 0:
            # Get the successful execution data
            latest_execution = target_node_data[-1]  # Use the latest execution
            if latest_execution.get("executionStatus") == "success":
                # Return the list of items from the first output of 'main'
                return latest_execution.get("data", {}).get("main", [[]])[0]
                
    except Exception as e:
        print(colored(f"Error parsing n8n output: {e}", "yellow"))
        print(colored(f"Raw output: {output_str[:500]}...", "yellow"))  # Show first 500 chars for debugging
    return []


def get_workflow_id_by_name(target_name, env_vars):
    """Fallback lookup if ID isn't in import output"""
    try:
        cmd = ["n8n", "export:workflow", "--all"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env_vars)
        workflows = json.loads(res.stdout)
        for wf in workflows:
            if wf.get("name") == target_name:
                return wf.get("id")
    except:
        pass
    return None


def run_node(node: n8nPythonNode, input_data: list[dict] = [{}]) -> tuple[Any, str]:
    # 1. Prepare input data
    if not input_data:
        input_data = [{}]  # Ensure at least one item exists for flow

    # 2. Create Workflow
    workflow_json = _get_constant_workflow(input_data)
    node_var = workflow_json["nodes"][-1]  # The target node is the last one

    # 3. Configure Target Node (Credentials & Parameters)
    node_var["type"] = "n8n-nodes-base." + node.node_meta.integration_name

    # Inject Credentials
    cred_item = credentials.query(node.node_meta.integration_name)
    if cred_item:
        node_var["credentials"] = {
            cred_item["type"]: {
                "id": cred_item["id"],
                "name": cred_item["name"],
            }
        }

    # Initialize parameters with base structure
    param_json = {}
    
    # Set standard operation and resource first
    param_json["operation"] = node.node_meta.operation_name
    param_json["resource"] = node.node_meta.resource_name

    # Add integration-specific authentication and type version
    if node.node_meta.integration_name == 'googleSheets':
        node_var["typeVersion"] = 4
        param_json["authentication"] = "oAuth2"
    elif node.node_meta.integration_name == 'slack':
        param_json["authentication"] = "accessToken"
    elif node.node_meta.integration_name == 'httpRequest':
        # For httpRequest with credentials, set authentication to use the credential type
        if cred_item:
            param_json["authentication"] = "genericCredentialType"
            param_json["genericAuthType"] = cred_item["type"]

    # Process custom parameters with proper type handling
    for key, value in node.params.items():
        p_val = value.to_json()
        if p_val is not None:
            # Special handling for Google Sheets parameters
            if node.node_meta.integration_name == 'googleSheets':
                if key == "sheetName" and isinstance(p_val, dict) and p_val.get("mode") == "id":
                    # Fix: Google Sheets V4 expects "name" mode for sheet names, not "id"
                    param_json[key] = {"mode": "name", "value": p_val["value"]}
                elif key == "documentId":
                    # Ensure documentId is properly formatted
                    if isinstance(p_val, dict):
                        param_json[key] = p_val
                    else:
                        param_json[key] = {"mode": "id", "value": str(p_val)}
                else:
                    param_json[key] = p_val
            # Special handling for Slack parameters  
            elif node.node_meta.integration_name == 'slack':
                # Ensure Slack parameters are properly formatted
                if key == "channelId" and isinstance(p_val, dict) and p_val.get("mode") == "id":
                    param_json[key] = {"mode": "name", "value": p_val["value"]}
                else:
                    param_json[key] = p_val
            else:
                param_json[key] = p_val

    # Set final parameters
    node_var["parameters"] = param_json

    # 4. Handle Pseudo Nodes (No Change)
    if 'pseudoNode' in node.node_json.keys() and node.node_json['pseudoNode']:
        try:
            output = run_pseudo_workflow(input_data, workflow_json)
            return output, ""
        except BaseException as e:
            traceback.print_exc()
            return [], str(e)

    # Add debugging output
    print(colored(f"### WORKFLOW DEBUG ({node.node_meta.integration_name}) ###", "yellow"))
    print(f"Target Node: {node_var['name']}")
    print(f"Node Type: {node_var['type']}")
    print(f"Parameters: {json.dumps(node_var.get('parameters', {}), indent=2)}")
    if cred_item:
        print(f"Using credential: {cred_item['name']} (type: {cred_item['type']})")
    else:
        print(colored("WARNING: No credentials found!", "red"))

    # 5. Real Execution (The Fix)
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".json")
    json.dump(workflow_json, temp_file)
    temp_file.close()
    temp_path = temp_file.name

    my_env = os.environ.copy()
    my_env["N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS"] = "true"

    imported_id = None
    output_data = []
    error = ""

    try:
        # A. Import
        import_cmd = ["n8n", "import:workflow", "--input", temp_path]
        imp_res = subprocess.run(import_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=my_env)

        if imp_res.returncode != 0:
            error = f"Import Failed: {imp_res.stderr}"
        else:
            # B. Get ID
            match = re.search(r'\(ID: ([a-zA-Z0-9\-]+)\)', imp_res.stdout + imp_res.stderr)
            if match:
                imported_id = match.group(1)
            else:
                imported_id = get_workflow_id_by_name(workflow_json["name"], my_env)

            if not imported_id:
                error = "Could not find workflow ID after import."
            else:
                # C. Execute
                exec_cmd = ["n8n", "execute", "--id", imported_id]
                # print(f"Executing Node: {node.node_meta.integration_name} (ID: {imported_id})")
                exec_res = subprocess.run(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                          env=my_env)

                print(colored(f"### N8N STDOUT ({node.node_meta.integration_name}) ###", "green"))
                print(colored(exec_res.stdout, "green"))

                if exec_res.returncode != 0:
                    error = f"Execution Failed: {exec_res.stderr}\nOutput: {exec_res.stdout}"
                    print(colored(f"### N8N ERROR ###\n{error}", "red"))
                else:
                    # D. Extract Data for Target Node
                    target_name = node_var["name"]  # "Target_Node"
                    extracted = parse_n8n_output(exec_res.stdout, target_name)

                    # Normalize output to match what ProAgent expects (list of dicts with 'json' key)
                    # n8n extraction usually returns [{'json': {...}}, ...] which is correct.
                    output_data = extracted

    except Exception as e:
        error = str(e)
        traceback.print_exc()
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        if imported_id:
            subprocess.run(["n8n", "delete:workflow", "--id", imported_id], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, env=my_env)

    return output_data, error