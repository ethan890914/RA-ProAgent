'''
openai.error.InvalidRequestError: The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766 (request id: 20231114074315131365776UGar1q65)
  Unable to generate ChatCompletion response
  Exception: The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766 (request id: 20231114074315131365776UGar1q65)
'''
import os
import traceback
from typing import Dict, List, Union
import json
import uuid
from colorama import Fore
import openai
from copy import deepcopy
import requests
import tiktoken
import time
from func_timeout import func_set_timeout
import func_timeout
import random
from ProAgent.config import CONFIG
from dotenv import load_dotenv
from openai import OpenAI
from ProAgent.loggers.logs import logger
from ProAgent.running_recorder import RunningRecoder
from ProAgent.utils import LLMStatusCode

load_dotenv()
def _chat_completion_request_atomic(**json_data):
    """
    Creates a chat completion request with the given JSON data.
    
    Args:
        **json_data: The JSON data for the chat completion request.
        
    Returns:
        The response from the OpenAI ChatCompletion API.
    """
    # openai.api_key = os.environ.get('OPENAI_API_KEY')
    # openai.api_base = os.environ.get('OPENAI_API_BASE')
    # openai.api_key = os.environ.get('GEMINI_API_KEY')
    # openai.api_base = os.environ.get('GEMINI_API_BASE')
    cleaned = []
    for msg in json_data["messages"]:
        if msg['role'] == 'assistant':
            cleaned.append(clean_message_for_gemini(msg))
        else:
            cleaned.append(msg)
    json_data["messages"] = cleaned
    print(json_data)

    client = OpenAI(
        api_key=os.environ.get('OPENAI_API_KEY'),
        base_url=os.environ.get('OPENAI_API_BASE'),
    )
    response = client.chat.completions.create(
        # model="gemini-2.5-flash",
        reasoning_effort="low",
                **json_data,
            )
    return response.model_dump_json()

@func_set_timeout(60)
def _chat_completion_request_without_retry(default_completion_kwargs, messages, functions=None,function_call=None, stop=None,restrict_cache_query=True ,recorder:RunningRecoder=None, **args):
    """
    Executes a chat completion request without retry.

    Args:
        default_completion_kwargs (dict): The default completion keyword arguments.
        messages (list): The list of messages.
        functions (list, optional): The list of functions.
        function_call (str, optional): The function call.
        stop (str, optional): The stop string.
        restrict_cache_query (bool, optional): Whether to restrict cache query.
        recorder (RunningRecoder, optional): The recorder object.
        **args: Additional keyword arguments.

    Returns:
        tuple: A tuple containing the response and the LLMStatusCode.

    Raises:
        Exception: If an exception occurs during the execution.
    """
    for message in messages:
        if "content" not in message.keys():
            message["content"] = ""

    json_data = default_completion_kwargs
    json_data["messages"] = messages

    json_data.update(args)
    if stop is not None:
        json_data.update({"stop": stop})
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})

    try:

        if recorder:
            response = recorder.query_llm_inout(restrict_cache_query=restrict_cache_query,
                                                base_kwargs = default_completion_kwargs,
                                                messages=messages, 
                                                functions=functions, 
                                                function_call=function_call, 
                                                stop = stop,
                                                other_args = args,
                                                )
        else:
            response = None

        if response == None:
            response = _chat_completion_request_atomic(**json_data)
            print(response)
            response = json.loads(str(response))
        if recorder:
            recorder.regist_llm_inout(base_kwargs = default_completion_kwargs,
                                    messages=messages, 
                                    functions=functions, 
                                    function_call=function_call, 
                                    stop = stop,
                                    other_args = args,
                                    output_data = response)
        
        return response, LLMStatusCode.SUCCESS
    
    except Exception as e:
        traceback.print_exc()
        logger.info("Unable to generate ChatCompletion response")
        logger.info(f"Exception: {e}")
        if recorder:
            recorder.regist_llm_inout(base_kwargs = default_completion_kwargs,
                                    messages=messages, 
                                    functions=functions, 
                                    function_call=function_call, 
                                    stop = stop,
                                    other_args = args,
                                    output_data=f"Exception: {e}")
        return e, LLMStatusCode.ERROR

def _chat_completion_request(**args):
    """
    Generates a chat completion request with the given arguments and attempts to retrieve the completed output.

    Args:
        **args: Additional keyword arguments for the chat completion request.

    Returns:
        The completed output if the request is successful, otherwise None.
    """

    for i in range(3):
        if i > 0:
            logger.info(f"LLM retry for the {i+1}'th time")

        try:
            output, output_code = _chat_completion_request_without_retry(**args)
            if output_code == LLMStatusCode.SUCCESS:
                return output
        except func_timeout.exceptions.FunctionTimedOut: #TLE
            logger.info(f"LLM response time out")
            continue

def transform_gemini_tool_function(f):
        gemini_tool = {
        "type" : "function",
        "function": f
        }
        return gemini_tool


def clean_message_for_gemini(message):
    """Remove OpenAI-specific fields that Gemini doesn't support"""
    cleaned = {
        'role': message['role'],
        'content': message.get('content'),
    }

    # Only include tool_calls if present and not None
    if message.get('tool_calls'):
        cleaned['tool_calls'] = message['tool_calls']

    # Remove None content (Gemini requires content or tool_calls)
    if cleaned['content'] is None:
        cleaned.pop('content')

    return cleaned


def normalize_tool_call_arguments(tool_calls):
    """Convert Gemini's object arguments to JSON strings (OpenAI format)"""
    if not tool_calls:
        return tool_calls

    for tool_call in tool_calls:
        if 'function' in tool_call:
            args = tool_call['function'].get('arguments')

            # If arguments is a dict/object, convert to JSON string
            if isinstance(args, dict):
                tool_call['function']['arguments'] = json.dumps(args)
            elif args is None:
                tool_call['function']['arguments'] = "{}"

    return tool_calls



