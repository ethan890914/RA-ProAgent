import logging
from typing import List, Dict
import json
from colorama import Fore, Style

from ProAgent.loggers.logs import logger
from ProAgent.agent.utils import _chat_completion_request, normalize_tool_call_arguments


class OpenAIFunction():
    def __init__(self):
        pass

    def parse(self, **args):
        """
        Parses the given arguments by making a chat completion request.

        Args:
            **args: The keyword arguments to be passed to the chat completion request.

        Returns:
            Tuple: A tuple containing the parsed content, function name, function arguments, and the original message.

        Raises:
            None.
        """
        retry_time = 1
        max_time = 1
        for i in range(max_time):
            output = _chat_completion_request(**args)

            if isinstance(output, Dict):
                usage = output["usage"]
                message = output["choices"][0]["message"]
                print(usage)

                # if "function_call" in message.keys():
                if "tool_calls" in message.keys():
                    break

                else:
                    args['messages'].append({"role": "assistant", "content": message['content']})
                    args['messages'].append({"role": 'user', "content": "No Function call here! You should always use a function call as your response."})
            retry_time += 1
            logger._log(f"{Fore.RED} Retry for the {retry_time}'th time{Style.RESET_ALL}")

        if retry_time > max_time:
            error_str = "Failed to generate chat response."
            logger._log(error_str, Fore.LIGHTBLACK_EX, level=logging.ERROR)
            raise TimeoutError(error_str)
        # if "function_call" in message.keys():
        # function_name = message["function_call"]["name"]
        # function_arguments = json.loads(message["function_call"]["arguments"], strict=False)
        function_name = "function_name"
        function_arguments = json.loads("{}")
        if message["tool_calls"]:
            message["tool_calls"] = normalize_tool_call_arguments(message["tool_calls"])
            function_name = message["tool_calls"][0]["function"]["name"]
            print("ARGUMENTS", json.loads(message["tool_calls"][0]["function"]["arguments"]))
            function_arguments = json.loads(message["tool_calls"][0]["function"]["arguments"], strict=False)
        print(function_name)
        content = ""
        if "content" in message.keys():
            content = message["content"]
        return content, function_name, function_arguments, message