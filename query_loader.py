from ProAgent.utils import userQuery

class query_loader():
    def __init__(self):
        self.queries = {}
        self.load_queries()
    def load_queries(self):
        # slack put fixed string
        query = userQuery(
            ID='default',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which send a message to the slack channel",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2. Choose #general for the Slack Channel.\n",
                "3. Message content: Hello World!.\n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # slack put fixed string
        query = userQuery(
            ID='1',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which send a message to the slack channel",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2. Choose #general for the Slack Channel.\n",
                "3. Message content: Hello World!.\n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # slack put messages from googleSheets
        query = userQuery(
            ID='2',
            task = "Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
                "2.2 The sheetName of Google is: commercial\n",
                "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Descrption\n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='3',
            task="Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
                "2.2 The sheetName of Google is: commercial\n",
                "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Description\n",
                "3.1 For the AI completion, use this prompt: 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'\n",
                "3.2 Make sure the AI completion messages parameter is properly formatted as a JSON array\n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='4',
            task="Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Based on the descriptions of the business flow, let the first aiCompletion determine the business flow type (to B or to C). If the business flow type is to B (to Business) just show it",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
                "2.2 The sheetName of Google is: commercial\n",
                "2.3 The sheet has a title row contains Business Line, Manager, cost, sales, and Description\n",
                "3.1 The aiCompletion node should use the existing OpenAI credentials from n8n\n",
                "3.2 For the AI completion prompt, use: 'Classify this business description as B2B or B2C: {{$json.Description}}. Respond only: to B or to C'\n",
                "3.3 Make sure the messages parameter is formatted as a simple string for OpenAI compatibility\n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # slack put messages from googleSheets
        query = userQuery(
            ID='5',
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
        self.load_single_query(query)

        # slack put messages from googleSheets
        query = userQuery(
            ID='6',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a joke and send it to slack.",
            additional_information=[
                "1 Use n8n-nodes-base.aiCompletion to generate a joke within 30 words."
                "1.2 Generate a new joke each time whenever I trigger the workflow. Don't hardcode the joke."
                "2.1 Send the generate joke to slack"
                "2.2 Choose #general for the Slack Channel."
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='7',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a joke and send it to slack.",
            additional_information=[
                "1 Use n8n-nodes-base.aiCompletion to generate a joke exceed 100 but within 200 words."
                "2.1 Send the generate joke to slack"
                "2.2 Choose #jokes for the Slack Channel."
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='8',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a small conversation between three people and send it to slack.",
            additional_information=[
                "1 Use n8n-nodes-base.aiCompletion to generate a small conversation between three people. Total word counts less than 500."
                "2.1 Send the generate joke to slack"
                "2.2 Choose #general for the Slack Channel."
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='9',
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
        self.load_single_query(query)
        #
        # slack put messages from googleSheets
        query = userQuery(
            ID='10',
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
        self.load_single_query(query)

        query = userQuery(
            ID ='11',
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
        self.load_single_query(query)

        query = userQuery(
            ID='12',
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
                "3.2 Send results to Slack channel #news",
                "3.3 Each Slack message format: '[i]. News: [headline]\nCategory: [category]'",
                "3.4 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='13',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which send an email to qwuqwuqwu@gmail.com",
            additional_information=[
                "1.2 email title: ProAgent testing",
                "1.1 email content: Hi qwuqwuqwu!"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='14',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which use aiCompletion to generate a joke and send it to qwuqwuqwu@gmail.com.",
            additional_information=[
                "1 Use n8n-nodes-base.aiCompletion to generate a joke within 30 words."
                "2.1 Send the generated joke to email address: qwuqwuqwu@gmail.com"
                "2.2 email title: ProAgent Joking",
                "2.3 email content: [joke]"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='15',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and sends each result to slack. Each slack message contains a single Description-category pair.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "2.2 System prompt: 'You are a news classifier. Classify as to Business or to Customer.'",
                "2.3 User prompt: Include the actual commercial entry's Description text",
                "2.4 aiCompletion should process each of the commercial entry separately",

                "3.1 Parse aiCompletion output to extract the category (to Business or to Customer)",
                "3.2 Send results to Slack channel #general",
                "3.3 Each Slack message format: '[i]. Commercial Entry: [Description]\nCategory: [category]'",
                "3.4 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # slack put messages from googleSheets
        query = userQuery(
            ID='16',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which read the data from googleSheets and send it to slack.",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
                "2.2 The sheetName of Google is: commercial\n"
                "3.1 Choose #general for the Slack Channel.\n",
                "3.2 Send what you got from googlesheet as a whole json structure string to slack. \n"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # googleSheets
        query = userQuery(
            ID='17',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which read the data from googleSheets and email it to qwuqwuqwu@gmail.com.",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.\n",
                "2.1 The documentId(id) of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c\n",
                "2.2 The sheetName of Google is: commercial\n"
                "3.1 Send what you got from googlesheet as a whole json structure string to qwuqwuqwu@gmail with Gmail."
                "3.2 email abstract: commercial flows"
                "3.3 email content: [content]"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='18',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and sends each result to qwuqwuqwu@gmail.com with Gmail. Each email message contains a single Description-category pair.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "2.2 System prompt: 'You are a news classifier. Classify as to Business or to Customer.'",
                "2.3 User prompt: Include the actual commercial entry's Description text",
                "2.4 aiCompletion should process each of the commercial entry separately",

                "3.1 Parse aiCompletion output to extract the category (to Business or to Customer)",
                "3.2 Send results with Gmail to qwuqwuqwu@gmail.com",
                "3.3 Each email abstract: [i]. Commercial Entry: [Description]",
                "3.3 Each email content format: '[i]. Commercial Entry: [Description]\nCategory: [category]'",
                "3.4 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='19',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and sends each result to qwuqwuqwu@gmail.com with Gmail. Each email message contains a single Description-category pair.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "2.2 System prompt: 'You are a news classifier. Classify as to Business or to Customer.'",
                "2.3 User prompt: Include the actual commercial entry's Description text",
                "2.4 aiCompletion should process each of the commercial entry separately",

                "3.1 Parse aiCompletion output to extract the category (to Business or to Customer)",
                "3.2 Send results with Gmail to qwuqwuqwu@gmail.com",
                "3.3 Only send to Customer category commercial entry, and ignore to Business one."
                "3.3 Each email abstract: [i]. Commercial Entry: [Description]",
                "3.3 Each email content format: '[i]. Commercial Entry: [Description]\nCategory: [category]'",
                "3.4 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='20',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and sends each result to slack. Each slack message contains a single Description-category pair.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "2.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
                "2.3 User prompt: Include the actual commercial entry's Description text",
                "2.4 aiCompletion should process each of the commercial entry separately",

                "3.1 Parse aiCompletion output to extract the category ('to Business' or 'to Customer')",
                "3.2 Send results to slack channel #general",
                "3.3 Only send 'to Business' category commercial entry, and ignore 'to Customer' one."
                "3.4 Each slack message format: '[i]. Commercial Entry: [Description]\nCategory: [category]'",
                "3.5 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='21',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and emails the result or send it to slack.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "2.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
                "2.3 User prompt: Include the actual commercial entry's Description text",
                "2.4 aiCompletion should process each of the commercial entry separately",

                "3.1 Parse aiCompletion output to extract the category ('to Business' or 'to Customer')",
                "3.2 If it's a 'to Business' commercial entry, then send it through slack."
                "3.3 If it's a 'to Customer' commercial entry, then send it through email."

                "4.1 slack format:"
                "4.2 Send results to slack channel #general",
                "4.3 Each slack message format: 'Commercial Entry: [Description]\nCategory: [category]'",

                "5.1 email format:"
                "5.2 Send results with Gmail to qwuqwuqwu@gmail.com",
                "5.3 Each email abstract: Commercial Entry: [Description]",
                "5.4 Each email content format: 'Commercial Entry: [Description]\nCategory: [category]'"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='22',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, calculate the profit of each entry(= sales - cost), uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and sends each result to slack. Each slack message contains a single pair of Description-profit-category.",
            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2 For each commercial entry from Google Sheets, calculate its profit(= sales - cost)",

                "3.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
                "3.2 System prompt: 'You are a news classifier. Classify as to Business or to Customer.'",
                "3.3 User prompt: Include the actual commercial entry's Description text",
                "3.4 aiCompletion should process each of the commercial entry separately",

                "4.1 Parse aiCompletion output to extract the category (to Business or to Customer)",
                "4.2 Send results(Description, profit, and category) to slack channel #general",
                "4.3 Each slack message format: '[i]. Commercial Entry: [Description]\n Profit: [profit]\n Category: [category]'",
                "4.4 i is the index of the news. start from 1"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='23',
            task="Whenever I trigger the Manual Trigger, execute the workflow,\
             which reads data from googleSheets, calculate the profit of each entry(= sales - cost),\
              uses first aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer',\
               and sends each result to slack. Each slack message contains a single pair of Description-profit-category. \
               After that, use the second aiCompletion to write a reminder email for each 'to Customer' commercial flow. \
               At the end, send those reminder emails to qwuqwuqwu@gmail.com with Gmail.",

            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2 For each commercial entry from Google Sheets, calculate its profit(= sales - cost)",

                "3.1 For each commercial entry from Google Sheets, create the first aiCompletion input with messages array containing system prompt and user prompt",
                "3.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
                "3.3 User prompt: Include the actual commercial entry's Description text",
                "3.4 The first aiCompletion should process each of the commercial entry separately",

                "4.1 Parse the first aiCompletion's output to extract the category ('to Business' or 'to Customer')",
                "4.2 Send results(Description, profit, and category) to slack channel #general",
                "4.3 Each slack message format: 'Commercial Entry: [Description]\n Profit: [profit]\n Category: [category]'",

                "5.1 Create the second aiCompletion input with messages array containing system prompt and user prompt",
                "5.2 System prompt: 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows",
                "5.4 User prompt: Include only the 'to Customer' commercial entry's Description text",
                "5.5 The second aiCompletion should process each of the commercial entry separately",

                "6.1 Parse the second aiCompletion output to extract the reminder content"
                "6.2 Send results to qwuqwuqwu@gmail.com wigh Gmail"
                "6.3 Each email abstract: 'To Customer' commercial flows reminder"
                "6.4 Each email content: [reminder content]"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='24',
            task="Whenever I trigger the Manual Trigger, execute the workflow,\
                         which reads data from googleSheets, calculate the profit of each entry(= sales - cost),\
                          uses first aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer',\
                           and sends each result to slack. Each slack message contains a single pair of Description-profit-category. \
                           After that, use the second aiCompletion to write a reminder email for each 'to Customer' commercial flow. \
                           At the end, send those reminder emails to corresponding Manager with Gmail.",

            additional_information=[
                "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "1.2 The sheetName of Google is: commercial",
                "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",

                "2 For each commercial entry from Google Sheets, calculate its profit(= sales - cost)",

                "3.1 For each commercial entry from Google Sheets, create the first aiCompletion input with messages array containing system prompt and user prompt",
                "3.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
                "3.3 User prompt: Include the actual commercial entry's Description text",
                "3.4 The first aiCompletion should process each of the commercial entry separately",

                "4.1 Parse the first aiCompletion's output to extract the category ('to Business' or 'to Customer')",
                "4.2 Send results(Description, profit, and category) to slack channel #general",
                "4.3 Each slack message format: 'Commercial Entry: [Description]\n Profit: [profit]\n Category: [category]'",

                "5.1 Create the second aiCompletion input with messages array containing system prompt and user prompt",
                "5.2 System prompt: 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows",
                "5.4 User prompt: Include only the 'to Customer' commercial entry's Description text",
                "5.5 The second aiCompletion should process each of the commercial entry separately",

                "6.1 Parse the second aiCompletion output to extract the reminder content"
                "6.2 Send results to the corresponding manager(which can be found in the googlesheet) wigh Gmail"
                "6.3 Each email abstract: 'To Customer' commercial flows reminder"
                "6.4 Each email content: [reminder content]"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # still working on this!!
        query = userQuery(
            ID='25',
            task="Whenever I trigger the Manual Trigger, execute the workflow, and read the business flow data from googleSheets, which contains cost and sales. Calculate the profit of the business flow (= sales - cost), and based on the descriptions of the business flow, let the first aiCompletion determine the business flow type ('to B' or 'to C'), and send profit or loss information to the business manager. If the business flow type is 'to B' (to Business), send a message to slack. If the business flow type is 'to C' (to Client), send a reminder email to the business flow manager, with the content generated by the second aiCompletion.",
            additional_information=[
                "1. All thoughts and comments should be in Chinese for me to understand.",
                "2.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
                "2.2 The sheetName of Google is: commercial",
                "2.3 The sheet contains business flow data with cost and sales columns",

                "3.1 Calculate profit for each business flow (profit = sales - cost)",

                "4.1 For each commercial entry from Google Sheets, create the first aiCompletion input with messages array containing system prompt and user prompt",
                "4.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
                "4.3 User prompt: Include the actual commercial entry's Description text",
                "4.4 The first aiCompletion should process each of the commercial entry separately",

                "5.1 For 'to B' business flows: send message to Slack channel #general",
                "5.2 Slack message format: 'Business Flow: [description]\nProfit: [calculated profit]\nType: to B'",

                "6.1 For 'to C' business flows: group them by different manager"
                
                "7.1 Create the second aiCompletion input with messages array containing system prompt and user prompt to generate reminder email content"
                "7.2 handle different group of business flows separately. For each manager:"
                "7.3 System prompt: 'You are an email writer. Generate reminder email content for business managers about client flows.'"
                "7.4 User prompt: Include all commercial entry's Description text for that manager"
                
                "8.1 Send reminder email to business flow manager with Gmail",
                "8.2 Email subject: 'Business Flow Reminder - to C'",
                "8.3 Email content: [content generated by second aiCompletion]"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # Google Drive - list files in ProAgentWorkspace folder
        query = userQuery(
            ID='26',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which lists all files in my Google Drive ProAgentWorkspace folder and sends the file list to Slack.",
            additional_information=[
                "1. Use googleDrive.file.list to list all files in the folder named 'ProAgentWorkspace'",
                "2. Send the list of files to Slack channel #general",
                "3. Each message should contain file name and file ID",
                "4. Message format: 'Files in ProAgentWorkspace:\n[list of files with names and IDs]'"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        # Google Drive - list files in ProAgentWorkspace folder
        query = userQuery(
            ID='27',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which first download the file 00005_code.txt from Google Drive, and then sends its content to slack.",
            additional_information=[
                "1. Use googleDrive to download the file '00005_code.txt' under folder 'ProAgentWorkspace'",
                "1.2 Search instruction: Use folder name to search for the specific folder."
                "1.2 Download instruction: Use fileId to download the file."
                "1.3 Decode the Base64 file content to get actual text"
                "2. Send the file content to Slack channel #general",
                "3. Message format: '00005_code.py:\n [file content]'"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

        query = userQuery(
            ID='28',
            task="Whenever I trigger the Manual Trigger, execute the workflow, which first download a file from Google Drive, and then sends parts of its content to slack.",
            additional_information=[
                "1. Use googleDrive to download the file 'abc-news_chunked_1day_articles_2025-11-11_1.csv' under folder 'ProAgentWorkspace/newsapi_data/2025-11-11'",
                "1.2 Search instruction: Use folder name to search for the specific folder."
                "1.2 Download instruction: Use fileId to download the file."
                "2.1 Decode the Base64 file content to get actual text"
                "2.2 The first line of this file is the schema for this csv file, Extract the schema"
                "2.3 Send the schema to Slack channel #news",
                "3. Message format: 'abc-news_chunked_1day_articles_2025-11-11_1.csv schema:\n [schema]'"
            ],
            refine_prompt=""
        )
        self.load_single_query(query)

    def load_single_query(self, userQuery):
        if userQuery.ID in self.queries:
            # overwrite the old query
            print(f'userQuery.ID = {userQuery.ID} is duplicated, the old query was overwritten!')
        self.queries[userQuery.ID] = userQuery

    def get_single_query(self, ID):
        if self.queries[ID] != None:
            return self.queries[ID]
        else:
            print('Query not existed!')
            assert False
            return self.queries['default']
