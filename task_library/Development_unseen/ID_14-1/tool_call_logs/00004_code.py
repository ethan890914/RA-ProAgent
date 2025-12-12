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
  comments: Manual trigger to start the workflow on user action.
  TODOs: 
    - Test trigger activation
    - Provide example output
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Generate a joke about a tree within 30 words.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Why did the tree go to therapy? Because it couldn’t stop branching out and was feeling stumped about its roots!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Generate a joke about a tree within 30 words using AI completion. The prompt is built in the workflow, so params are empty.
  TODOs: 
    - Build the prompt in the mainWorkflow
    - Test AI completion output
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
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'joke': 'Why did the tree go to therapy? Because it couldn’t stop branching out and was feeling stumped about its roots!'}}]

3.Output:
[{'json': {'id': '19af58591a6b7a45', 'threadId': '19af58591a6b7a45', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send the generated joke to the specified email address with subject 'ProAgent Joking'. Set required params for Gmail send action.
  TODOs: 
    - Test email sending
    - Verify email content and subject
  """
  params = { 'emailType': 'text',
             'message': '={{$json["joke"]}}',
             'options': {},
             'sendTo': 'qwuqwuqwu@gmail.com',
             'subject': 'ProAgent Joking'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19af58591a6b7a45', 'threadId': '19af58591a6b7a45', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to generate a joke about a tree using AI completion and send it via Gmail.
    TODOs: 
      - Build AI completion input with prompt
      - Extract joke from AI output
      - Send joke via Gmail
      - Test end to end
    """
    # Step 1: Build AI completion input
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Generate a joke about a tree within 30 words."}
            ]
        }
    }]

    # Step 2: Call AI completion
    ai_output = action_0(ai_input)

    # Step 3: Extract joke text
    joke_text = ai_output[0]["json"]["choices"][0]["text"].strip()

    # Step 4: Wrap joke text for Gmail input
    gmail_input = [{"json": {"joke": joke_text}}]

    # Step 5: Send email
    gmail_output = action_1(gmail_input)

    return gmail_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""