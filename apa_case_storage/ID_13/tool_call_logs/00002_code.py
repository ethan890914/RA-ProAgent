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
  comments: Manual trigger to start the workflow when user clicks the button.
  TODOs: 
    - Implement the trigger function with proper params.
    - Test the trigger function.
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
[{'json': {'id': '19adb6df69000e9a', 'threadId': '19adb6df69000e9a', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Send an email via Gmail API to the specified recipient with given subject and content.
  TODOs: 
    - Test sending email.
    - Handle errors and refine.
  """
  params = {
             "sendTo": "qwuqwuqwu@gmail.com",
             "subject": "ProAgent testing",
             "emailType": "text",
             "message": "Hi qwuqwuqwu!",
             "options": {}
           }
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19adb6df69000e9a', 'threadId': '19adb6df69000e9a', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Triggered manually, send an email to qwuqwuqwu@gmail.com with given subject and content.
    TODOs:
      - Test the workflow end-to-end
      - Handle errors if email sending fails
    """
    output_data = action_0(trigger_input)
    return output_data




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""