"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
None

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: Trigger the workflow manually by user
  TODOs: 
    - Test the trigger
    - Ensure it outputs the correct trigger input
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a professional PostgreSQL programmer, please only output a SQL string'}, {'role': 'user', 'content': "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3, and sort with column published_at"}]}}]

3.Output:
[{'json': {'choices': [{'text': '```sql\nSELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;\n```'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Generate SQL query using AI completion with system and user prompts
  TODOs: 
    - Implement the input messages array in the workflow
    - Test the AI completion output
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
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'query': 'SELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;'}}]

3.Output:
[]
"""
def action_1(input_data):
  """
  comments: Set params in action_1 with the actual SQL query string extracted from input_data, no expression used
  TODOs: 
    - Test the query execution and output format
  """
  params = {}  # to be Implemented
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_2(input_data):
  """
  comments: Send the formatted query results to Slack channel general
  TODOs: 
    - Format the Slack message properly
    - Test sending messages to Slack
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
    comments: Workflow to generate SQL query from AI, execute it in PostgreSQL, and send results to Slack
    TODOs:
      - Build aiCompletion input with system and user messages
      - Clean AI output SQL query
      - Format Slack messages
    """
    # Step 1: Start from manual trigger
    trigger_output = trigger_0(None)

    # Step 2: Build aiCompletion input
    ai_input = [{"json": {"messages": [
        {"role": "system", "content": "You are a professional PostgreSQL programmer, please only output a SQL string"},
        {"role": "user", "content": "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3, and sort with column published_at"}
    ]}}]

    # Step 3: Call aiCompletion
    ai_output = action_0(ai_input)

    # Step 4: Extract and clean SQL query
    ai_text = ai_output[0]['json']['choices'][0]['text'].strip()
    # Remove markdown if present
    if ai_text.startswith('```'):
        ai_text = ai_text.split('\n', 1)[1] if '\n' in ai_text else ai_text[3:]
        if ai_text.endswith('```'):
            ai_text = ai_text[:-3]
        ai_text = ai_text.strip()

    # Step 5: Prepare input for PostgreSQL
    pg_input = [{"json": {"query": ai_text}}]

    # Step 6: Call PostgreSQL executeQuery
    pg_output = action_1(pg_input)

    # Step 7: Format Slack messages
    slack_input = []
    for i, row in enumerate(pg_output):
        title = row['json'].get('title', '')
        published_at = row['json'].get('published_at', '')
        message_text = f"{i+1}. Title: {title}\npublished_at: {published_at}"
        slack_input.append({"json": {"text": message_text}})

    # Step 8: Send messages to Slack
    slack_output = action_2(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}, 'pairedItem': {'item': 0}}]`
the output data of function `action_0` is: `[{'json': {'choices': [{'text': '```sql\nSELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;\n```'}]}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[]`
the output data of function `action_2` is: `[]`

------------------------
In Function: mainWorkflow
        # Step 6: Call PostgreSQL executeQuery
-->     pg_output = action_1(pg_input)
------------------------
In Function: transparent_action
      function = transparent_action(integration="postgres", resource="database", operation="executeQuery")
-->   output_data = function.run(input_data=input_data, params=params)
      return output_data
------------------------
n8nRunningException: Execution Failed: 
Output: Problem with execution 3110: The workflow has issues and cannot be executed for that reason. Please fix them first.. Aborting.
The workflow has issues and cannot be executed for that reason. Please fix them first. (execution 3110)
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