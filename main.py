import hydra
import omegaconf
import logging
from colorama import Fore, Style
import json
import os

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

from proagent_rag import *


def retrieval_samples(query):
    query_file = "queries_data.json"

    with open(query_file) as f:
        query_library = json.load(f)

    rag = ProAgentRAG(query_library)
    rag.build_index()
    res = rag.retrieve_similar(query)

    # Find the first retrieved query that has NO ancestor workflow
    # Check apa_case_storage to see if the workflow has an ancestor.json file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    storage_dir = os.path.join(current_dir, 'apa_case_storage')

    for retrieved_query in res:
        retrieved_query_id = retrieved_query['ID']
        # Check if this query's workflow has an ancestor.json
        workflow_dir = os.path.join(storage_dir, f'ID_{retrieved_query_id}')
        ancestor_file = os.path.join(workflow_dir, 'ancestor.json')

        # Only return this ID if it has NO ancestor (i.e., it's a base workflow)
        if not os.path.exists(ancestor_file):
            print(f"✓ Found base workflow (no ancestor): ID_{retrieved_query_id}")
            return str(retrieved_query_id)

    # If no workflow without ancestor found, return None or raise error
    print("⚠️  Warning: All retrieved workflows have ancestors. Returning first result anyway.")
    return str(res[0]) if res else None


def run_refine_oneshot_mode(cfg, new_query, old_id, new_query_id=None):
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
    if new_query_id is not None:
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
    elif CONFIG.environment == ENVIRONMENT.RARefine:
        # task = '''
        # Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each news headline as 'technology' or 'sport', and sends results to Slack. Each Slack message contains a single news-category pair.
        # '''

        task = '''
                Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and emails the result or send it to slack.'''
        additions = None
        additions = [
            "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
            "1.2 The sheetName of Google is: commercial",
            "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",
            "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
            "2.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
            "2.3 User prompt: Include the actual commercial entry's Description text",
            "2.4 aiCompletion should process each of the commercial entry separately",
            "3.1 Parse aiCompletion output to extract the category ('to Business' or 'to Customer')",
            "3.2 If it's a 'to Business' commercial entry, then send it through slack.",
            "3.3 If it's a 'to Customer' commercial entry, then send it through email.",
            "4.1 slack format:",
            "4.2 Send results to slack channel #news",
            "4.3 Each slack message format: 'Commercial Entry: [Description]\nCategory: [category]'",
            "5.1 email format:",
            "5.2 Send results with Gmail to qwuqwuqwu@gmail.com",
            "5.3 Each email abstract: Commercial Entry: [Description]",
            "5.4 Each email content format: 'Commercial Entry: [Description]\nCategory: [category]'"
        ]
        query = include_all_info(task, additions)

        old_id = retrieval_samples(query)

        new_query = userQuery(
            ID='temp',
            task=task,
            additional_information=additions
        )

        if old_id is not None:
            CONFIG.environment = ENVIRONMENT.Refine_oneshot
            # run_refine_oneshot_mode(cfg, new_query, old_id=old_id, new_query_id='21-2')
            run_refine_oneshot_mode(cfg, new_query, old_id=old_id, new_query_id=None)
            return
        else:
            CONFIG.environment = ENVIRONMENT.Development

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