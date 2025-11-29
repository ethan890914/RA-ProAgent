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


@hydra.main(config_path="ProAgent/configs", config_name="generate_n8n_query")
def main(cfg: omegaconf.DictConfig):
    """
    The main function that runs the ReACTHandler.

    Args:
        cfg (omegaconf.DictConfig): The configuration object.
        
    Returns:
        None
    """
    
    recorder = RunningRecoder() # default root directory: ./records

    record_dir = None
    record_dir = "./apa_case"

    if record_dir != None:
        recorder.load_from_disk(record_dir, cfg)
        # this record_dir is the record history provided by the original paper, which is different from saving
        # directory of current round

    # slack put fixed string
    # query = userQuery(
    #     task="Whenever I trigger the Manual Trigger, execute the workflow, which send a message to the slack channel",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2. Choose #general for the Slack Channel.\n",
    #         "3. Message content: Hello World!.\n"
    #     ],
    #     refine_prompt=""
    # )

    # slack put messages from googleSheets
    # query = userQuery(
    #     task = "Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
    #         "2.2 The sheetName of Google is: commercial\n",
    #         "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Descrption\n"
    #     ],
    #     refine_prompt=""
    # )

    # query = userQuery(
    #     task="Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
    #         "2.2 The sheetName of Google is: commercial\n",
    #         "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Description\n",
    #         "3.1 For the AI completion, use this prompt: 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'\n",
    #         "3.2 Make sure the AI completion messages parameter is properly formatted as a JSON array\n"
    #     ],
    #     refine_prompt=""
    # )

    # query = userQuery(
    #     task="Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
    #         "2.2 The sheetName of Google is: commercial\n",
    #         "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Description\n",
    #         "3.1 The aiCompletion node should use the existing OpenAI credentials from n8n\n",
    #         "3.2 For the AI completion prompt, use: 'Classify this business description as B2B or B2C: {{$json.Description}}. Respond only: to B or to C'\n",
    #         "3.3 Make sure the messages parameter is formatted as a simple string for OpenAI compatibility\n"
    #     ],
    #     refine_prompt=""
    # )

    # # slack put messages from googleSheets
    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which read the data from googleSheets and send it to slack.",
        additional_information=[
            "1. All thoughts and comments should be in Chinese for me to understand.",
            "2.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
            "2.2 The sheetName of Google is: news",
            "2.3 The sheet has one title row with value \"Headlines\" and has ten news headlines below."
            "3.1 Choose #general for the Slack Channel.",
            "3.2 Send headlines you got from googlesheet row by row to slack. "
        ],
        refine_prompt=""
    )

    # slack put messages from googleSheets
    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a joke and send it to slack.",
        additional_information=[
            "1 Use n8n-nodes-base.aiCompletion to generate a joke within 30 words."
            "2.1 Send the generate joke to slack"
            "2.2 Choose #general for the Slack Channel."
        ],
        refine_prompt=""
    )

    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a joke and send it to slack.",
        additional_information=[
            "1 Use n8n-nodes-base.aiCompletion to generate a joke exceed 100 but within 200 words."
            "2.1 Send the generate joke to slack"
            "2.2 Choose #general for the Slack Channel."
        ],
        refine_prompt=""
    )

    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a small conversation between three people and send it to slack.",
        additional_information=[
            "1 Use n8n-nodes-base.aiCompletion to generate a small conversation between three people. Total word counts less than 500."
            "2.1 Send the generate joke to slack"
            "2.2 Choose #general for the Slack Channel."
        ],
        refine_prompt=""
    )

    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to determine the category of this news title and send it to slack.",
        additional_information=[
            "1.1 Use n8n-nodes-base.aiCompletion to determine the category of this news title"
            "1.2 news title: Multiple snowstorms to bear down on Northeast, Ohio Valley in early December"
            "2.1 Send the generate category to slack"
            "2.2 Choose #general for the Slack Channel."
            "2.3 Slack message format: 'News: [title]\nCategory: [category]"
        ],
        refine_prompt=""
    )
    #
    # slack put messages from googleSheets
    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to check if this news belongs to category technology or sport",
        additional_information=[
            "1. All thoughts and comments should be in Chinese for me to understand.",
            "2. news title: \"Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\"",
            "3. Use aiCompletion to check if this news title belongs to category technology or sport"
            "4.1 Send the generate category to slack"
            "4.2 Choose #general for the Slack Channel."
            "4.3 Slack message format: 'News: [title]\nCategory: [category]"
        ],
        refine_prompt=""
    )

    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each news headline as 'technology' or 'sport', and sends results to Slack. Each Slack message contains a single news-category pair.",
        additional_information=[
            "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
            "1.2 The sheetName of Google is: news",
            "1.3 The sheet has one title row with value \"Headlines\" and has ten news headlines below.",

            "2.1 For each headline from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
            "2.2 System prompt: 'You are a news classifier. Classify as technology or sport.'",
            "2.3 User prompt: Include the actual headline text",
            "2.4 aiCompletion should process each of the 10 headlines separately",

            "3.1 Parse aiCompletion output to extract the category (technology or sport)",
            "3.2 Send results to Slack channel #general",
            "3.3 Each Slack message format: 'News: [headline]\nCategory: [category]'",
            "3.4 Total 10 messages should be sent to Slack"
        ],
        refine_prompt=""
    )

    query = userQuery(
        task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each news headline as 'technology' or 'sport', and sends results to Slack. Each Slack message contains a single news-category pair.",
        additional_information=[
            "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
            "1.2 The sheetName of Google is: news",
            "1.3 The sheet has one title row with value \"Headlines\" and has ten news headlines below.",

            "2.1 For each headline from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
            "2.2 System prompt: 'You are a news classifier. Classify as technology or sport.'",
            "2.3 User prompt: Include the actual headline text",
            "2.4 aiCompletion should process each of the headlines separately",

            "3.1 Parse aiCompletion output to extract the category (technology or sport)",
            "3.2 Send results to Slack channel #general",
            "3.3 Each Slack message format: '[i]. News: [headline]\nCategory: [category]'",
            "3.4 i is the index of the news. start from 1"
        ],
        refine_prompt=""
    )

    # # slack put messages from googleSheets
    # query = userQuery(
    #     task="Whenever I trigger the Manual Trigger, execute the workflow, which read the data from googleSheets and send it to slack.",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
    #         "2.2 The sheetName of Google is: commercial\n"
    #         "3.1 Choose #general for the Slack Channel.\n",
    #         "3.2 Send what you got from googlesheet as a whole json structure string to slack. \n"
    #     ],
    #     refine_prompt=""
    # )

    # googleSheets
    # query = userQuery(
    #     task="Whenever I trigger the Manual Trigger, execute the workflow, which read the data from googleSheets and shows it.",
    #     additional_information=[
    #         "1. All thoughts and comments should be in Chinese for me to understand.\n",
    #         "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
    #         "2.2 The sheetName of Google is: commercial\n"
    #     ],
    #     refine_prompt=""
    # )

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

    compiler = Compiler(cfg, recorder)

    handler = ReACTHandler(cfg=cfg,
                            query=query,
                            compiler=compiler,
                            recorder=recorder)
    handler.run()

if __name__ == "__main__":
    main()