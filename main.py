import json
import os

import hydra
import omegaconf
from dotenv import load_dotenv

from ProAgent.config import CONFIG
from ProAgent.handler.ReACT import ReACTHandler
from ProAgent.n8n_parser.compiler import Compiler
from ProAgent.router.utils import ENVIRONMENT
from ProAgent.running_recorder import RunningRecoder
from ProAgent.utils import userQuery
from execute_from_tool_calls import run
from proagent_rag import include_all_info, ProAgentRAG
from query_loader import query_loader

load_dotenv()
def run_refine_oneshot_mode(cfg, new_query, old_id):
    """
    Run ProAgent in refine_oneshot mode.

    Args:
        cfg: Configuration object
        new_query: new query to process
        old_id: ID of the old workflow to use as reference

    Returns:
        None
    """

    recorder = RunningRecoder()

    query_loader_ = query_loader()

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
    old_workflow_dir = os.path.join(current_dir, 'task_library/Base_workflow', f'ID_{old_id}')
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
    query_loader_ = query_loader()

    if CONFIG.environment == ENVIRONMENT.Production_quick:
        run("./task_library/Base_workflow/ID_21-2", cfg)
        return
    elif CONFIG.environment == ENVIRONMENT.Refine_oneshot:
        query = query_loader_.get_single_query(ID='21-2')
        run_refine_oneshot_mode(cfg, new_query=query, old_id='21')
        return
    elif CONFIG.environment == ENVIRONMENT.RARefine:
        rag = ProAgentRAG()

        # load from already set queries
        query_temp = query_loader_.get_single_query(ID='21-1')
        query = include_all_info(query_temp.task, query_temp.additional_information)
        task = query_temp.task
        additions = query_temp.additional_information

        src_ids = rag.retrieve_similar(query, top_k=1, threshold=0.8)
        del rag
        retrieve_workflow = src_ids[0] if len(src_ids) > 0 else None

        new_query = userQuery(
            ID='temp',
            task=task,
            additional_information=additions
        )

        if retrieve_workflow is not None:
            CONFIG.environment = ENVIRONMENT.Refine_oneshot
            print(f'Retrieved retrieve_workflow = {retrieve_workflow}')
            run_refine_oneshot_mode(cfg, new_query, old_id=retrieve_workflow)
            return
        else:
            CONFIG.environment = ENVIRONMENT.Development

    recorder = RunningRecoder() # default root directory: ./records

    record_dir = "./apa_case"

    if record_dir is not None:
        recorder.load_from_disk(record_dir, cfg)
        # this record_dir is the record history provided by the original paper, which is different from saving
        # directory of current round

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