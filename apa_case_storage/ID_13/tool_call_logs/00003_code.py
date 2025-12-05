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
  comments: Trigger the workflow manually by user click.
  TODOs: 
    - Test the manual trigger.
    - Ensure it outputs the correct format for the workflow input.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
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
[{'json': {}}]

3.Output:
[{'json': {'id': '19aed2581ff49039', 'threadId': '19aed2581ff49039', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Send an email to qwuqwuqwu@gmail.com with subject 'ProAgent testing' and message 'Hi qwuqwuqwu!'.
  TODOs: 
    - Test sending email with given inputs.
    - Handle errors if email sending fails.
  """
  params = { 'emailType': 'text',
             'message': 'Hi qwuqwuqwu!',
             'options': {},
             'sendTo': 'qwuqwuqwu@gmail.com',
             'subject': 'ProAgent testing'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19aed2581ff49039', 'threadId': '19aed2581ff49039', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
  """
  comments: Connect manual trigger to Gmail send email action to send specified email.
  TODOs: 
    - Test the workflow end-to-end.
    - Verify email is sent correctly.
  """
  # The Gmail send action does not require any specific fields from trigger_input, so pass it directly.
  email_output = action_0(trigger_input)
  return email_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""