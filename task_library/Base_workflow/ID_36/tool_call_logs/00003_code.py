"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: TriggerAcivatedSuccess
2.Input: 
[]

3.Output:
[{'json': {}}]
"""
def trigger_0(input_data):
  """
  comments: Manual trigger to start the workflow
  TODOs: 
    - Test trigger activation
    - Verify output format
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a professional PostgreSQL programmer, please only output a SQL string'}, {'role': 'user', 'content': "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3"}]}}]

3.Output:
[{'json': {'choices': [{'text': '```sql\nSELECT * FROM bloomberg_articles LIMIT 3;\n```'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Use aiCompletion to generate SQL query from prompts
  TODOs: 
    - Build messages array in workflow
    - Test AI output format
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["query"]: string = "", Required: Query. The SQL query to execute. You can use n8n expressions and $1, $2, $3, etc to refer to the 'Query Parameters' set in options below.(e.g. SELECT id, name FROM product WHERE quantity > $1 AND price <= $2). You can't use expression.
1 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'query': 'SELECT * FROM bloomberg_articles LIMIT 3;'}}]

3.Output:
[{'json': {'id': '1', 'title': 'Canada loses measles elimination status after ongoing outbreaks', 'description': 'International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America', 'content': 'Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars]', 'url': 'https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798', 'published_at': '2025-11-11T07:45:36.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'DEVI SHASTRI AP health writer', 'url_to_image': 'https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '2', 'title': 'New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain', 'description': "New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation", 'content': 'WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars]', 'url': 'https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101', 'published_at': '2025-11-11T07:29:35.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'CHARLOTTE GRAHAM-MCLAY Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '3', 'title': '18 people sent to the hospital after mobile lounge crashes at Washington D.C.-area airport', 'description': 'Officials say a vehicle transporting passengers at a Washington, D.C.-area airport hit a dock at the building, sending 18 people to the hospital', 'content': 'DULLES, Va. -- A vehicle transporting passengers at a Washington, D.C.-area airport hit a dock at the building Monday afternoon, sending 18 people to the hospital, according to officials.  A mobile l… [+757 chars]', 'url': 'https://abcnews.go.com/US/wireStory/18-people-hospital-after-mobile-lounge-crashes-washington-127395823', 'published_at': '2025-11-11T05:29:55.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'The Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/0c39a82b-8829-405d-b4bc-73e9f29913c4/wirestory_0e2df632e6cc08375adc2895963bfcea_16x9.jpg?w=1600', 'content_length': 213, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Execute the SQL query generated by AI with correct raw string params including query and options
  TODOs: 
    - Test query execution
    - Handle query errors gracefully
  """
  params = {'options': {}, 'query': 'SELECT * FROM bloomberg_articles LIMIT 3;'}
  function = transparent_action(integration="postgres", resource="database", operation="executeQuery")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["select"]: enum[string] = "", Required: Send Message To(Select...) . Available values:
  0.0 value=="channel": Channel
  0.1 value=="user": User
1 params["channelId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required when (select in ['channel']), otherwise do not provide: Channel. The Slack channel to send to(Select a channel...) . "mode" should be one of ['id', 'name', 'url']: 
  1.0 params["channelId"]["value"](when "mode"="id"): string: By ID(C0122KQ70S7E)
  1.1 params["channelId"]["value"](when "mode"="name"): string: By Name(#general)
  1.2 params["channelId"]["value"](when "mode"="url"): string: By URL(https://app.slack.com/client/TS9594PZK/B0556F47Z3A)
2 params["user"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Activate(Not Required) when (select in ['user']), otherwise do not provide: User(Select a user...) . "mode" should be one of ['id', 'username']: 
  ...hidden...
3 params["messageType"]: enum[string] = "text": Message Type. Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more . Available values:
  3.0 value=="text": Simple Text Message. Supports basic Markdown
  3.1 value=="block": Blocks. Combine text, buttons, form elements, dividers and more in Slack 's visual builder
  3.2 value=="attachment": Attachments
4 params["text"]: string = "", Activate(Not Required) when (messageType in ['block']), otherwise do not provide: Notification Text. Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options".
5 params["blocksUi"]: string = "", Required when (messageType in ['block']), otherwise do not provide: Blocks. Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>
6 params["attachments"]: list[dict] = [{}], Activate(Not Required) when (messageType in ['attachment']), otherwise do not provide: Attachments(Add attachment item) . properties description:
  ...hidden...
7 params["otherOptions"]: dict = {}: Options. Other options to set(Add options) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'text': '1. Title: Canada loses measles elimination status after ongoing outbreaks\nAuthor: DEVI SHASTRI AP health writer'}}, {'json': {'text': '2. Title: New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain\nAuthor: CHARLOTTE GRAHAM-MCLAY Associated Press'}}, {'json': {'text': '3. Title: 18 people sent to the hospital after mobile lounge crashes at Washington D.C.-area airport\nAuthor: The Associated Press'}}]

3.Output:
[]
"""
def action_2(input_data):
  """
  comments: Send messages to Slack channel general
  TODOs: 
    - Format messages properly
    - Test Slack message sending
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedInner
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered by manual trigger, generates SQL query by AI, executes it on PostgreSQL, and sends results to Slack.
    TODOs:
      - Build aiCompletion input
      - Extract and clean SQL query
      - Execute query on PostgreSQL
      - Format and send Slack messages
    """
    # Step 1: Manual trigger output (empty json)
    # Step 2: Build aiCompletion input with messages
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a professional PostgreSQL programmer, please only output a SQL string"},
                {"role": "user", "content": "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3"}
            ]
        }
    }]

    # Step 3: Call aiCompletion action
    ai_output = action_0(ai_input)

    # Step 4: Extract and clean SQL query from AI output
    raw_query = ai_output[0]['json']['choices'][0]['text'].strip()
    # Remove markdown code block if any
    if raw_query.startswith('```'):
        raw_query = raw_query.split('\n', 1)[1] if '\n' in raw_query else raw_query[3:]
        if raw_query.endswith('```'):
            raw_query = raw_query[:-3]
        raw_query = raw_query.strip()

    # Step 5: Prepare input for PostgreSQL action
    pg_input = [{"json": {"query": raw_query}}]
    pg_params = {"query": raw_query, "options": {}}

    # Step 6: Call PostgreSQL executeQuery action
    pg_output = action_1(pg_input)

    # Step 7: Extract title and author from PostgreSQL output
    slack_messages = []
    for i, row in enumerate(pg_output, start=1):
        title = row['json'].get('title', '')
        author = row['json'].get('author', '')
        message_text = f"{i}. Title: {title}\nAuthor: {author}"
        slack_messages.append({"json": {"text": message_text}})

    # Step 8: Prepare Slack params
    slack_params = {
        "select": "channel",
        "channelId": {"mode": "name", "value": "general"},
        "messageType": "text",
        "text": "={{$json[\"text\"]}}"
    }

    # Step 9: Call Slack post message action
    slack_output = action_2(slack_messages)

    return slack_output



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[{'json': {'choices': [{'text': '```sql\nSELECT * FROM bloomberg_articles LIMIT 3;\n```'}]}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[{'json': {'id': '1', 'title': 'Canada loses measles elimination status after ongoing outbreaks', 'description': 'International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America', 'content': 'Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars]', 'url': 'https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798', 'published_at': '2025-11-11T07:45:36.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'DEVI SHASTRI AP health writer', 'url_to_image': 'https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '2', 'title': 'New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain', 'description': "New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation", 'content': 'WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars]', 'url': 'https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101', 'published_at': '2025-11-11T07:29:35.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'CHARLOTTE GRAHAM-MCLAY Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '3', 'title': '18 people sent to the hospital after mobile lounge crashes at Washington D.C.-area airport', 'description': 'Officials say a vehicle transporting passengers at a Washington, D.C.-area airport hit a dock at the building, sending 18 people to the hospital', 'content': 'DULLES, Va. -- A vehicle transporting passengers at a Washington, D.C.-area airport hit a dock at the building Monday afternoon, sending 18 people to the hospital, according to officials.  A mobile l… [+757 chars]', 'url': 'https://abcnews.go.com/US/wireStory/18-people-hospital-after-mobile-lounge-crashes-washington-127395823', 'published_at': '2025-11-11T05:29:55.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'The Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/0c39a82b-8829-405d-b4bc-73e9f29913c4/wirestory_0e2df632e6cc08375adc2895963bfcea_16x9.jpg?w=1600', 'content_length': 213, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_2` is: `[]`

------------------------
In Function: mainWorkflow
        # Step 9: Call Slack post message action
-->     slack_output = action_2(slack_messages)
------------------------
In Function: transparent_action
      function = transparent_action(integration="slack", resource="message", operation="post")
-->   output_data = function.run(input_data=input_data, params=params)
      return output_data
------------------------
n8nRunningException: Execution Failed: 
Output: Problem with execution 2526: The workflow has issues and cannot be executed for that reason. Please fix them first.. Aborting.
The workflow has issues and cannot be executed for that reason. Please fix them first. (execution 2526)
Error executing workflow. See log messages for details.

Execution error:
====================================
The workflow has issues and cannot be executed for that reason. Please fix them first.
undefined
WorkflowHasIssuesError: The workflow has issues and cannot be executed for that reason. Please fix them first.
    at WorkflowExecute.checkForWorkflowIssues (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1382:10)
    at WorkflowExecute.processRunExecutionData (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1461:8)
    at WorkflowExecute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:176:15)
    at ManualExecutionService.runManually (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/manual-execution.service.ts:157:27)
    at WorkflowRunner.runMainProcess (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:298:53)
    at WorkflowRunner.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:175:4)
    at Execute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/commands/execute.ts:95:23)
    at CommandRegistry.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/command-registry.ts:67:4)
    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/bin/n8n:63:2
The workflow has issues and cannot be executed for that reason. Please fix them first.


You can also see the runnning result for all functions in there comments.
"""