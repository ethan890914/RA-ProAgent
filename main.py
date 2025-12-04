import hydra
import omegaconf
import logging
from colorama import Fore, Style
import json

from mock_agent import mock_function_call_list

from ProAgent.loggers.logs import logger
from ProAgent.n8n_parser.compiler import Compiler
from ProAgent.handler.ReACT import ReACTHandler
from ProAgent.utils import userQuery
from ProAgent.running_recorder import RunningRecoder
from query_loader import query_loader
from execute_from_tool_calls import run
from ProAgent.router.utils import ENVIRONMENT
from ProAgent.config import CONFIG

def run_refine_oneshot_mode(cfg, new_query_id, old_id):
    """
    Run ProAgent in refine_oneshot mode.

    Args:
        cfg: Configuration object
        new_query_id: ID of the new query to process
        old_id: ID of the old workflow to use as reference

    Returns:
        None
    """
    import os

    recorder = RunningRecoder()

    query_loader_ = query_loader()

    # Load new query
    new_query = query_loader_.get_single_query(ID=new_query_id)

    # Load old workflow data
    workflow_data = query_loader_.load_workflow_from_storage(old_ID=old_id)

    # Prepare refine_oneshot_data
    refine_oneshot_data = {
        'old_query': workflow_data['query'],
        'workflow_code': workflow_data['workflow_code']
    }

    # Create compiler and initialize with old workflow
    compiler = Compiler(cfg, recorder)

    # Load and replay tool calls from old workflow to initialize the compiler
    current_dir = os.path.dirname(os.path.abspath(__file__))
    old_workflow_dir = os.path.join(current_dir, 'apa_case_storage', f'ID_{old_id}')
    tool_call_logs_dir = os.path.join(old_workflow_dir, 'tool_call_logs')

    if os.path.exists(tool_call_logs_dir):
        # Get all tool JSON files
        tool_files = sorted([f for f in os.listdir(tool_call_logs_dir) if f.endswith('_tool.json')])

        # Replay tool calls to initialize the compiler state
        for tool_file in tool_files:
            with open(os.path.join(tool_call_logs_dir, tool_file), 'r', encoding='utf-8') as f:
                tool_call = json.load(f)
                tool_name = tool_call.get('tool_name')
                tool_input = tool_call.get('tool_input', {})

                # Replay the tool call to build the workflow
                if tool_name == 'function_define':
                    compiler.handle_function_define(tool_input)
                elif tool_name == 'function_rewrite_params':
                    compiler.handle_rewrite_params(tool_input)
                elif tool_name == 'workflow_implment':
                    compiler.handle_workflow_implement(tool_input)
                elif tool_name == 'task_submit':
                    break  # Stop at task submission

    # Create handler with refine_oneshot_data
    handler = ReACTHandler(
        cfg=cfg,
        query=new_query,
        compiler=compiler,
        recorder=recorder,
        refine_oneshot_data=refine_oneshot_data
    )

    handler.run()

    # Save ancestor reference file so Production_quick mode knows to load the base workflow
    ancestor_file_path = os.path.join(recorder.record_root_dir, 'ancestor.json')
    with open(ancestor_file_path, 'w', encoding='utf-8') as f:
        json.dump({
            'base_workflow_id': old_id,
            'description': f'This workflow was created using refine_oneshot mode based on workflow ID_{old_id}'
        }, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved ancestor reference: {ancestor_file_path}")

@hydra.main(config_path="ProAgent/configs", config_name="generate_n8n_query")
def main(cfg: omegaconf.DictConfig):
    """
    The main function that runs the ReACTHandler.

    Args:
        cfg (omegaconf.DictConfig): The configuration object.

    Returns:
        None
    """

    if CONFIG.environment == ENVIRONMENT.Production_quick:
        # run("./records/2025_11_30_10_21_25", cfg)
        run("./apa_case_storage/ID_21-2", cfg)
        return
    elif CONFIG.environment == ENVIRONMENT.Refine_oneshot:
        run_refine_oneshot_mode(cfg, new_query_id='21-2', old_id='21')
        return

    recorder = RunningRecoder() # default root directory: ./records

    record_dir = None
    record_dir = "./apa_case"

    if record_dir != None:
        recorder.load_from_disk(record_dir, cfg)
        # this record_dir is the record history provided by the original paper, which is different from saving
        # directory of current round

    # original ProAgent demo example
    # query = userQuery(
    #     task = "Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Calculate the profit of the business flow (= sales - cost), and based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C), and send profit or loss information to the business manager. If the business flow type is to B (to Business), send a message to slack. If the business flow type is to C (to Client), send a reminder email to the business flow manager, with the content generated by the second aiCompletion.",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(url) of Google Sheet is: https://docs.google.com/spreadsheets/d/1_B038J1f3VW94z179OagFwEtnr3k5mTyXKBTPI2Fw-U/edit#gid=1759497495\n",
    #         "2.2 The sheetName(url) of Google is: https://docs.google.com/spreadsheets/d/1_B038J1f3VW94z179OagFwEtnr3k5mTyXKBTPI2Fw-U/edit#gid=1759497495\n"
    #         "3.1 Use ai node1 to determine if there is a business flow, you can use the aiCompletion node (remember to adjust the Prompt!), if the ai's answer contains 'to B', then the business flow type is to B, if it contains 'to C', then the business flow type is to C.\n"
    #         "4.1 Choose #general for the Slack Channel.\n",
    #         "4.2 Use ai node2 to generate the email content.\n"
    #     ],
    #     refine_prompt=""
    # )

    query_loader_ = query_loader()
    query = query_loader_.get_single_query(ID='21')

    compiler = Compiler(cfg, recorder)

    handler = ReACTHandler(cfg=cfg,
                            query=query,
                            compiler=compiler,
                            recorder=recorder)
    handler.run()

if __name__ == "__main__":
    main()