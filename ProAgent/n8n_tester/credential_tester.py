import json
import subprocess
import tempfile
import os
import re
import uuid
from typing import Dict, Any, Optional, Tuple, List

# --- Mock Data Simulation ---
MOCK_C_JSON_CONTENT = [
    {
        "id": "L6lm8Thz7eceg8y7",
        "name": "Google Sheets account",
        "type": "googleSheetsOAuth2Api",
    }
]

MOCK_W_JSON_CONTENT = [
    {"id": "mock-workflow-id-7890"}
]


# --- Credentials Logic ---
class Credentials:
    def __init__(self):
        credential_data = MOCK_C_JSON_CONTENT
        self.credential_data: Dict[str, Any] = {}

        for item in credential_data:
            item_info = {
                "name": item["name"],
                "id": item["id"],
                "type": item["type"],
            }

            type_mapping = {
                "googleSheetsOAuth2Api": ["googleSheets"],
            }
            possible_node_types = type_mapping.get(item["type"], [item["type"]])

            for node_type_name in possible_node_types:
                if self.credential_data.get(node_type_name) is None:
                    self.credential_data[node_type_name] = []
                self.credential_data[node_type_name].append(item_info)

    def query(self, node_type: str) -> Optional[Dict[str, str]]:
        if node_type not in self.credential_data:
            return None
        return self.credential_data[node_type][-1]


# --- Workflow Generation ---

def create_google_sheets_workflow(credential_item: Dict[str, str], document_id: str, sheet_name: str) -> Dict[str, Any]:
    start_node = {
        "id": "start",
        "name": "Start",
        "type": "n8n-nodes-base.start",
        "typeVersion": 1,
        "position": [250, 50],
        "parameters": {}
    }

    gs_node = {
        "id": "gs_test_node",
        "name": "Google Sheets",
        "type": "n8n-nodes-base.googleSheets",
        "typeVersion": 4,
        "position": [450, 50],
        "credentials": {
            credential_item["type"]: {
                "id": credential_item["id"],
                "name": credential_item["name"],
            }
        },
        # --- CORRECTED PARAMETERS FOR V4 ---
        "parameters": {
            "authentication": "oAuth2",  # Explicitly set auth mode
            "operation": "read",  # V4: 'read' instead of 'getAll'
            "resource": "sheet",  # V4: 'sheet' instead of 'row'
            "documentId": {"mode": "id", "value": document_id},
            "sheetName": {"mode": "name", "value": sheet_name},
            # V4 Read Options (optional but good for testing)
            "options": {}
        }
    }

    workflow = {
        "name": f"AutoTest_GSheets_{uuid.uuid4().hex[:6]}",
        "nodes": [start_node, gs_node],
        # Corrected Deeply Nested Connections Structure
        "connections": {
            "Start": {
                "main": [
                    [
                        {"node": "Google Sheets", "type": "main", "index": 0}
                    ]
                ]
            }
        },
        "active": False,
        "settings": {"executionOrder": "v1"},
        "tags": []
    }
    return workflow


def parse_n8n_output_json(output: str) -> List[Any]:
    try:
        start_index = output.find('[')
        end_index = output.rfind(']') + 1
        if start_index != -1 and end_index != -1:
            json_str = output[start_index:end_index]
            return json.loads(json_str)
    except Exception:
        pass
    return []


def get_workflow_id_by_name(target_name: str, env_vars: Dict) -> Optional[str]:
    print("   ⚠️  ID not found in import output. Attempting lookup by name...")
    try:
        list_cmd = ["n8n", "export:workflow", "--all"]
        process = subprocess.run(list_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env_vars)
        if process.returncode != 0:
            print(f"   ❌ Failed to list workflows: {process.stderr}")
            return None
        workflows = json.loads(process.stdout)
        for wf in workflows:
            if wf.get("name") == target_name:
                return wf.get("id")
    except Exception as e:
        print(f"   ❌ Error during lookup: {e}")
    return None


# --- Main Execution Logic ---

def fetch_google_sheets_data():
    print("--- Starting Correct N8N CLI Data Fetch ---")

    my_env = os.environ.copy()
    my_env["N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS"] = "true"

    credentials_loader = Credentials()
    credential_item = credentials_loader.query('googleSheets')

    if not credential_item:
        print("❌ Credentials not found.")
        return

    # 2. Create Workflow JSON
    DOCUMENT_ID = "1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c"
    SHEET_NAME = "commercial"

    workflow_json = create_google_sheets_workflow(credential_item, DOCUMENT_ID, SHEET_NAME)

    # 3. Save to Temp File
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".json")
    json.dump(workflow_json, temp_file, indent=2)
    temp_file.close()
    temp_path = temp_file.name

    print(f"1. Workflow file created: {temp_path}")

    imported_id = None

    try:
        # 4. IMPORT
        print("2. Importing workflow into n8n database...")
        import_cmd = ["n8n", "import:workflow", "--input", temp_path]
        import_process = subprocess.run(import_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                        env=my_env)

        if import_process.returncode != 0:
            print("❌ Import failed!")
            print(import_process.stderr)
            return

        # 5. Extract ID
        output_str = import_process.stdout + import_process.stderr
        match = re.search(r'\(ID: ([a-zA-Z0-9\-]+)\)', output_str)
        if match:
            imported_id = match.group(1)
            print(f"✅ Workflow imported successfully. ID: {imported_id}")
        else:
            imported_id = get_workflow_id_by_name(workflow_json["name"], my_env)
            if imported_id:
                print(f"✅ Workflow found via lookup. ID: {imported_id}")
            else:
                print("❌ Could not find Workflow ID.")
                return

        # 6. EXECUTE
        print(f"3. Executing workflow ID: {imported_id}...")
        exec_cmd = ["n8n", "execute", "--id", imported_id]
        exec_process = subprocess.run(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=my_env)

        print("\n--- EXECUTION RESULTS ---")
        if exec_process.returncode == 0:
            print("✅ EXECUTION SUCCESS!")
            print("--- Google Sheets Data ---")
            data = parse_n8n_output_json(exec_process.stdout)
            if data:
                print(json.dumps(data, indent=2))
            else:
                print("Raw STDOUT:")
                print(exec_process.stdout)
        else:
            print(f"❌ Execution Failed (Code: {exec_process.returncode}).")
            print("--- STDOUT ---")
            print(exec_process.stdout)
            print("--- STDERR ---")
            print(exec_process.stderr)

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        if imported_id:
            print(f"\n4. Cleaning up (Deleting Workflow {imported_id})...")
            subprocess.run(["n8n", "delete:workflow", "--id", imported_id], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, env=my_env)


if __name__ == "__main__":
    fetch_google_sheets_data()