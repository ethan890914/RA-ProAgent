import json
from ProAgent.agent.gpt4_function import OpenAIFunction
from ProAgent.agent.utils import _chat_completion_request, _chat_completion_request_without_retry
from ProAgent.config import CONFIG
from ProAgent.n8n_parser.workflow import n8nPythonWorkflow
from ProAgent.n8n_parser.node import n8nPythonNode
from ProAgent.n8n_tester.pseudo_node.ai_node import run_ai_completion
from ProAgent.n8n_tester.pseudo_node.utils import fill_return_data, replace_exp

agent = OpenAIFunction()

def run_pseudo_workflow(input_data: list, constant_workflow: n8nPythonWorkflow) -> list:
    """
    Run a pseudo workflow using the provided input data and constant workflow.

    Args:
        input_data (list): The input data for the pseudo workflow.
        constant_workflow (n8nPythonWorkflow): The constant workflow to be used.

    Returns:
        list: The final return data as a Python list.
    """
    # import pdb; pdb.set_trace()
    node_var:n8nPythonNode = constant_workflow['nodes'][-1]
    params_raw = node_var['parameters']

    if node_var['type'].split('.')[-1] == 'aiCompletion':
        # For aiCompletion, we need to merge params into input_data
        # If input_data is empty, use params to build it
        if not input_data or len(input_data) == 0:
            # Single-item case: params contains messages as JSON string
            # Build input_data from params
            messages = params_raw.get('messages', '')
            if isinstance(messages, str) and messages:
                # Parse JSON string to list/dict
                try:
                    messages_json = json.loads(messages)
                except:
                    messages_json = messages
                input_data = [{"json": {"messages": messages_json}}]
            else:
                # messages is already a list/dict
                input_data = [{"json": {"messages": messages}}]

        return_list = run_ai_completion(input_data)
    else:
        return_list = []

    # Return the list directly, not as a formatted string
    return return_list
