"""
Execute workflow by replaying tool calls from saved record.
This is the CORRECT approach - use the LLM's actual tool calls instead of parsing code.
"""
import sys
import os
import json
import hydra
import omegaconf
from typing import List, Dict

from ProAgent.n8n_parser.compiler import Compiler
from ProAgent.config import CONFIG
from ProAgent.running_recorder import RunningRecoder

def load_tool_calls(record_dir):
    """Load all tool calls from the record in order."""
    tool_call_dir = os.path.join(record_dir, "tool_call_logs")
    if not os.path.exists(tool_call_dir):
        raise FileNotFoundError(f"Tool call logs directory not found: {tool_call_dir}")

    # Get all tool JSON files
    tool_files = [f for f in os.listdir(tool_call_dir) if f.endswith("_tool.json")]
    tool_files.sort()

    tool_calls = []
    for tool_file in tool_files:
        with open(os.path.join(tool_call_dir, tool_file), "r", encoding="utf-8") as f:
            tool_call = json.load(f)
            tool_calls.append(tool_call)

    return tool_calls

def execute(record_dir, cfg: omegaconf.DictConfig):
    """
    Execute workflow by replaying the saved tool calls.
    If the workflow was created with refine_oneshot mode, it will first load the base workflow.
    """
    print("=" * 80)
    print("Executing Workflow by Replaying Tool Calls")
    print("Using LLM's actual tool calls from record (no code parsing!)")
    print("=" * 80)
    print()

    # Check for ancestor reference file
    ancestor_file = os.path.join(record_dir, 'ancestor.json')
    base_workflow_id = None

    if os.path.exists(ancestor_file):
        with open(ancestor_file, 'r', encoding='utf-8') as f:
            ancestor_data = json.load(f)
            base_workflow_id = ancestor_data.get('base_workflow_id')
        print(f"📋 Found ancestor reference: base workflow is ID_{base_workflow_id}")
        print()

    # Load tool calls from current workflow
    print(f"Record directory: {record_dir}")
    tool_calls = load_tool_calls(record_dir)
    print(f"✓ Loaded {len(tool_calls)} tool calls from current workflow")
    print()

    # Create compiler
    recorder = RunningRecoder()
    compiler = Compiler(cfg, recorder)

    # If there's a base workflow, load it first to establish the node definitions
    if base_workflow_id:
        print("=" * 80)
        print(f"Loading base workflow from ID_{base_workflow_id}...")
        print("=" * 80)
        print()

        # Construct path to base workflow
        base_dir = os.path.dirname(record_dir)
        base_record_dir = os.path.join(base_dir, f'ID_{base_workflow_id}')

        if os.path.exists(base_record_dir):
            base_tool_calls = load_tool_calls(base_record_dir)
            print(f"✓ Loaded {len(base_tool_calls)} tool calls from base workflow")
            print()

            # Replay base workflow tool calls (stops at task_submit to avoid executing)
            print("Replaying base workflow tool calls...")
            for i, tool_call in enumerate(base_tool_calls):
                tool_name = tool_call.get("tool_name")
                tool_input = tool_call.get("tool_input", {})

                print(f"  [{i}] Base: {tool_name}", end='')

                if tool_name == "function_define":
                    compiler.handle_function_define(tool_input)
                    functions = tool_input.get("functions", [])
                    print(f" ({len(functions)} functions)")
                elif tool_name == "function_rewrite_params":
                    compiler.handle_rewrite_params(tool_input)
                    print(f" ({tool_input.get('function_name')})")
                elif tool_name == "workflow_implment":
                    compiler.handle_workflow_implement(tool_input)
                    print(f" ({tool_input.get('workflow_name')})")
                elif tool_name == "task_submit":
                    print(" (skipping)")
                    break
                else:
                    print(f" (skipping)")

            print()
            print("✓ Base workflow nodes loaded successfully")
            print()
        else:
            print(f"⚠️  Warning: Base workflow directory not found: {base_record_dir}")
            print(f"   Continuing with current workflow only...")
            print()

    # Replay each tool call from current workflow (incremental changes)
    if base_workflow_id:
        print("Replaying current workflow tool calls (incremental changes)...")
    else:
        print("Replaying tool calls...")
    print("=" * 80)

    for i, tool_call in enumerate(tool_calls):
        tool_name = tool_call.get("tool_name")
        tool_input = tool_call.get("tool_input", {})

        print(f"\n[{i}] Tool: {tool_name}")

        if tool_name == "function_define":
            # Define functions
            functions = tool_input.get("functions", [])
            print(f"    Defining {len(functions)} function(s):")
            for func in functions:
                print(f"      → {func['integration_name']}.{func['resource_name']}.{func['operation_name']}")

            status, output = compiler.handle_function_define(tool_input)
            print(f"    Status: {status.name}")

        elif tool_name == "function_rewrite_params":
            # Set function parameters
            func_name = tool_input.get("function_name")
            print(f"    Setting parameters for: {func_name}")

            status, output = compiler.handle_rewrite_params(tool_input)
            print(f"    Status: {status.name}")

        elif tool_name == "workflow_implment":
            # Implement workflow
            workflow_name = tool_input.get("workflow_name")
            print(f"    Implementing workflow: {workflow_name}")

            status, output = compiler.handle_workflow_implement(tool_input)
            print(f"    Status: {status.name}")

        elif tool_name == "task_submit":
            # Task submission - workflow is complete
            print(f"    Workflow complete!")
            break

        else:
            print(f"    Skipping unknown tool: {tool_name}")

    print()
    print("=" * 80)
    print("All tool calls replayed - now executing workflow...")
    print("=" * 80)
    print()

    # Execute the workflow with real API calls
    compiler.update_runtime()

    print()
    print("=" * 80)
    print("✓ Workflow Execution Complete!")
    print("=" * 80)
    print()

    return True

# if __name__ == "__main__":
def run(record_dir, cfg: omegaconf.DictConfig):
    try:
        print(f'\n record_dir = {record_dir}')
        execute(record_dir, cfg)
        print("\n✓ Success!")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
