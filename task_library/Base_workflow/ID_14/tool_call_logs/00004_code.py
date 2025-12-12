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
  comments: Manual trigger to start the workflow when user clicks the button.
  TODOs: 
    - Test the trigger
    - Verify it activates mainWorkflow
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a funny assistant.'}, {'role': 'user', 'content': 'Tell me a joke within 30 words.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Why don’t scientists trust atoms? Because they make up everything! Even this joke—guess it’s all just a bunch of tiny laughs!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Generate a joke within 30 words using AI completion with a prompt.
  TODOs: 
    - Test joke generation output
    - Refine prompt if joke is too long or irrelevant
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
[{'json': {'text': 'Why don’t scientists trust atoms? Because they make up everything! Even this joke—guess it’s all just a bunch of tiny laughs!'}}]

3.Output:
[{'json': {'id': '19aed3137913791d', 'threadId': '19aed3137913791d', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send the generated joke email to qwuqwuqwu@gmail.com with subject and content from input_data.
  TODOs: 
    - Test sending email
    - Verify email received with correct content
  """
  params = { 'emailType': 'text',
             'message': '={{$json["text"]}}',
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
[{'json': {'id': '19aed3137913791d', 'threadId': '19aed3137913791d', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input):
    """
    comments: Workflow to generate a joke using AI and send it via Gmail when manually triggered.
    TODOs: 
      - Test end-to-end workflow
      - Verify joke length and email delivery
    """
    # Step 1: Build AI input with prompt
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a funny assistant."},
                {"role": "user", "content": "Tell me a joke within 30 words."}
            ]
        }
    }]

    # Step 2: Call AI completion action
    ai_output = action_0(ai_input)

    # Step 3: Extract joke text
    joke_text = ai_output[0]["json"]["choices"][0]["text"].strip()

    # Step 4: Prepare email input
    email_input = [{"json": {"text": joke_text}}]

    # Step 5: Send email
    email_output = action_1(email_input)

    return email_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""