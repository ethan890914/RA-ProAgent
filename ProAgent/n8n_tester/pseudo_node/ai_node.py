
import json
from ProAgent.config import CONFIG

from ProAgent.agent.utils import _chat_completion_request


def run_ai_completion(params_list:list) -> str:
    """
    Generates AI completion responses.

    Args:
        params_list (list): A list containing the node parameters dictionary with 'messages' key.

    Returns:
        list: List of items with AI completion results in {"json": {"text": ...}} format.
    """
    return_list = []
    completion_kwargs = CONFIG.default_completion_kwargs

    # Extract messages from the first params dict
    if len(params_list) > 0 and 'messages' in params_list[0]:
        # params_list contains node parameters (e.g., [{"messages": "..."}])
        messages = params_list[0]['messages']
    else:
        # Fallback: empty messages
        messages = "[]"

    # Parse messages
    if isinstance(messages, str):
        messages_json = json.loads(messages)
    elif isinstance(messages, list):
        messages_json = messages
    else:
        messages_json = []

    # Generate AI completion (once, not per item in params_list)
    result = _chat_completion_request(messages=messages_json,
                                        functions=None,
                                        default_completion_kwargs=completion_kwargs,
                                        recorder=None)
    content = result["choices"][0]["message"]['content']
    return_list.append(
        {
            "json": {
                'text': content
            },
            "pairedItem": {
                "item": 0
            }
        })
    return return_list
