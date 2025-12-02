"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: TriggerAcivatedSuccess
2.Input: 
[]

3.Output:
[{'json': {}}]
"""
def trigger_0():
  """
  comments: Trigger the workflow manually by user click.
  TODOs: 
    - Test the manual trigger works correctly.
    - Ensure the output format is compatible with the workflow.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant that generates a joke within 30 words.'}, {'role': 'user', 'content': 'Please generate a short joke within 30 words.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Why don’t scientists trust atoms? Because they make up everything!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Generate a joke within 30 words using aiCompletion. Pass 'messages' in input_data as list with one item containing 'json' key holding messages list. Params is empty dict.
  TODOs: 
    - Test AI completion with messages in input_data and empty params.
    - Verify joke text extraction.
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["sendTo"]: string = "", Required: To. The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com.(info@example.com)
1 params["subject"]: string = "", Required: Subject(Hello World!)
2 params["emailType"]: enum[string] = "text", Required: Email Type  You can't use expression.. Available values:
  2.0 value=="text": Text
  2.1 value=="html": HTML
3 params["message"]: string = "", Required: Message
4 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'ProAgent Joking', 'emailType': 'text', 'message': 'Why don’t scientists trust atoms? Because they make up everything!', 'options': {}}}]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Send the generated joke to the specified email address.
  TODOs: 
    - Set email recipient, subject, and content dynamically.
    - Test email sending with joke content.
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="gmail", resource="message", operation="send")
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
    comments: Workflow triggered manually, generate a joke using AI and send it by Gmail to a fixed email.
    TODOs:
      - Test the workflow end to end.
      - Handle possible empty or error AI output.
    """
    # Step 1: Build input_data for aiCompletion with messages
    ai_input = [{"json": {"messages": [
        {"role": "system", "content": "You are a helpful assistant that generates a joke within 30 words."},
        {"role": "user", "content": "Please generate a short joke within 30 words."}
    ]}}]

    # Step 2: Call AI Completion to generate joke
    ai_output = action_0(ai_input)

    # Step 3: Extract the joke text from ai_output
    joke_text = ""
    if ai_output and len(ai_output) > 0:
        try:
            joke_text = ai_output[0]["json"]["choices"][0]["text"].strip()
        except Exception as e:
            joke_text = "[Error extracting joke]"
    else:
        joke_text = "[No joke generated]"

    # Step 4: Prepare email input
    email_input = [{"json": {
        "sendTo": "qwuqwuqwu@gmail.com",
        "subject": "ProAgent Joking",
        "emailType": "text",
        "message": joke_text,
        "options": {}
    }}]

    # Step 5: Send email
    email_output = action_1(email_input)

    return email_output




"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[{'json': {'choices': [{'text': 'Why don’t scientists trust atoms? Because they make up everything!'}]}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[]`

------------------------
In Function: mainWorkflow
        # Step 5: Send email
-->     email_output = action_1(email_input)
------------------------
In Function: transparent_action
      function = transparent_action(integration="gmail", resource="message", operation="send")
-->   output_data = function.run(input_data=input_data, params=params)
      return output_data
------------------------
n8nRunningException: Execution Failed: 
Output: Problem with execution 893: The workflow has issues and cannot be executed for that reason. Please fix them first.. Aborting.
The workflow has issues and cannot be executed for that reason. Please fix them first. (execution 893)
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