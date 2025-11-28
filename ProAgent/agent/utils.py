'''
Fixed utils.py for ProAgent - Proper hybrid OpenAI/Gemini support
Switch between APIs by setting API_PROVIDER in environment variables
'''
import os
import traceback
from typing import Dict, List, Union
import json
import uuid
from colorama import Fore
import openai  # Keep original OpenAI import
from copy import deepcopy
import requests
import tiktoken
import time
from func_timeout import func_set_timeout
import func_timeout
import random
from ProAgent.config import CONFIG

from ProAgent.loggers.logs import logger
from ProAgent.running_recorder import RunningRecoder
from ProAgent.utils import LLMStatusCode

# Import Gemini agent (only when needed)
_gemini_available = False
try:
    from ProAgent.agent.gemini_agent import gemini_chat_completion_create
    _gemini_available = True
except ImportError:
    _gemini_available = False


def get_api_provider():
    """Determine which API provider to use based on environment variable"""
    return os.getenv('API_PROVIDER', 'openai').lower()


def _chat_completion_request_atomic(**json_data):
    """
    Creates a chat completion request with the given JSON data.
    Now supports both OpenAI and Gemini APIs based on configuration.
    
    Args:
        **json_data: The JSON data for the chat completion request.
        
    Returns:
        The response from the selected API (OpenAI or Gemini).
    """
    api_provider = get_api_provider()
    
    if api_provider in ['gemini', 'gemini-flash']:
        # Use Gemini API
        if not _gemini_available:
            raise ImportError("Gemini agent not available. Install google-generativeai and ensure gemini_agent.py is present.")
        
        response = gemini_chat_completion_create(**json_data)
        return response
    
    else:
        # Use OpenAI API (original code)
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_base = os.environ.get('OPENAI_API_BASE')

        response = openai.ChatCompletion.create(**json_data)
        return response


@func_set_timeout(60)
def _chat_completion_request_without_retry(default_completion_kwargs, messages, functions=None,function_call=None, stop=None,restrict_cache_query=True ,recorder:RunningRecoder=None, **args):
    """
    Executes a chat completion request without retry.
    Now supports both OpenAI and Gemini APIs.

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
    api_provider = get_api_provider()
    
    for message in messages:
        if "content" not in message.keys():
            message["content"] = ""

    json_data = default_completion_kwargs.copy()
    json_data["messages"] = messages

    json_data.update(args)
    if stop is not None:
        json_data.update({"stop": stop})
    if functions is not None:
        json_data.update({"functions": functions})
    if function_call is not None:
        json_data.update({"function_call": function_call})

    try:

        if recorder and hasattr(recorder, 'query_llm_inout'):
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
            
            # Handle different response formats - KEY FIX!
            if api_provider == 'openai':
                # OpenAI returns a response object that needs to be converted to dict
                response = json.loads(str(response))
            # Gemini already returns dict format - no parsing needed!

        if recorder and hasattr(recorder, 'regist_llm_inout'):
            recorder.regist_llm_inout(base_kwargs = default_completion_kwargs,
                                    messages=messages, 
                                    functions=functions, 
                                    function_call=function_call, 
                                    stop = stop,
                                    other_args = args,
                                    output_data = response)
        
        return response, LLMStatusCode.SUCCESS

    # Handle API-specific errors
    except Exception as e:
        error_str = str(e)
        traceback.print_exc()
        
        if api_provider == 'gemini':
            # Gemini-specific error handling
            if "api key" in error_str.lower() or "authentication" in error_str.lower():
                logger.error("Gemini API authentication error")
                logger.error(f"Please set the GEMINI_API_KEY environment variable: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
                    recorder.regist_llm_inout(base_kwargs=default_completion_kwargs,
                                              messages=messages,
                                              functions=functions,
                                              function_call=function_call,
                                              stop=stop,
                                              other_args=args,
                                              output_data=f"GeminiAuthError: {e}")
                return e, LLMStatusCode.AUTH_ERROR
            elif "quota" in error_str.lower() or "rate" in error_str.lower():
                logger.info("Gemini API quota/rate limit error")
                logger.info(f"Exception: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
                    recorder.regist_llm_inout(base_kwargs=default_completion_kwargs,
                                              messages=messages,
                                              functions=functions,
                                              function_call=function_call,
                                              stop=stop,
                                              other_args=args,
                                              output_data=f"GeminiRateLimit: {e}")
                return e, LLMStatusCode.API_FAILURE
            else:
                logger.info("Unable to generate ChatCompletion response due to Gemini API error")
                logger.info(f"Exception: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
                    recorder.regist_llm_inout(base_kwargs=default_completion_kwargs,
                                              messages=messages,
                                              functions=functions,
                                              function_call=function_call,
                                              stop=stop,
                                              other_args=args,
                                              output_data=f"GeminiError: {e}")
                return e, LLMStatusCode.ERROR
        
        else:
            # OpenAI-specific error handling (original code)

            # Catch the specific AuthenticationError
            if hasattr(openai.error, 'AuthenticationError') and isinstance(e, openai.error.AuthenticationError):
                logger.error("OpenAI AuthenticationError: API key not provided or invalid.")
                logger.error(f"Please set the OPENAI_API_KEY environment variable or set it in code: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
                    recorder.regist_llm_inout(base_kwargs=default_completion_kwargs,
                                              messages=messages,
                                              functions=functions,
                                              function_call=function_call,
                                              stop=stop,
                                              other_args=args,
                                              output_data=f"OpenAIAuthError: {e}")
                return e, LLMStatusCode.AUTH_ERROR

            # Catch other OpenAI API errors (e.g., APIError, RateLimitError)
            elif hasattr(openai.error, 'OpenAIError') and isinstance(e, openai.error.OpenAIError):
                logger.info("Unable to generate ChatCompletion response due to OpenAI API error")
                logger.info(f"Exception: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
                    recorder.regist_llm_inout(base_kwargs=default_completion_kwargs,
                                              messages=messages,
                                              functions=functions,
                                              function_call=function_call,
                                              stop=stop,
                                              other_args=args,
                                              output_data=f"OpenAIError: {e}")
                return e, LLMStatusCode.API_FAILURE

            else:
                # Generic error handling
                logger.info("Unable to generate ChatCompletion response")
                logger.info(f"Exception: {e}")
                if recorder and hasattr(recorder, 'regist_llm_inout'):
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
    Now supports both OpenAI and Gemini APIs.

    Args:
        **args: Additional keyword arguments for the chat completion request.

    Returns:
        The completed output if the request is successful, otherwise None.
    """
    api_provider = get_api_provider()
    
    # Log which API we're using
    if hasattr(args.get('recorder'), 'llm_interface_id'):
        logger.info(f"Using {api_provider.upper()} API for LLM request")

    for i in range(5):
        if i > 0:
            logger.info(f"LLM retry for the {i+1}'th time")

        try:
            output, output_code = _chat_completion_request_without_retry(**args)
            logger.info(f"LLM testing")
            if output_code == LLMStatusCode.SUCCESS:
                logger.info(f"LLM output success")
                return output
            elif output_code == LLMStatusCode.AUTH_ERROR:
                logger.info(f"LLM AuthenticationError")
                logger.info(f"Starting 60-second sleep...")
                time.sleep(60)
                logger.info(f"Sleep finished.")
            elif api_provider == 'openai' and hasattr(openai.error, 'OpenAIError') and output_code == openai.error.OpenAIError:
                logger.info(f"LLM OpenAIError")
                logger.info(f"Starting 60-second sleep...")
                time.sleep(60)
                logger.info(f"Sleep finished.")
            else:
                logger.info(f"LLM API_FAILURE")
                logger.info(f"Starting 60-second sleep...")
                time.sleep(60)
                logger.info(f"Sleep finished.")

        except func_timeout.exceptions.FunctionTimedOut: #TLE
            logger.info(f"LLM response time out")
            print("Starting 60-second sleep...")
            time.sleep(60)
            print("Sleep finished.")
            continue
