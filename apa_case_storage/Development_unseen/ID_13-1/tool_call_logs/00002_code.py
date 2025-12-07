"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: This trigger starts the workflow manually when the user clicks the button.
  TODOs: 
    - Test the manual trigger activation.
    - Ensure the trigger output format is correct.
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
[{'json': {}, 'pairedItem': {'item': 0}}]

3.Output:
[{'json': {'id': '19af57fece604a0d', 'threadId': '19af57fece604a0d', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Send an email to cc9008@nyu.edu with the subject 'ProAgent testing' and content 'Hi ProAgent!'.
  TODOs: 
    - Test sending email
    - Verify email delivery
    - Handle errors if any
  """
  params = { 'emailType': 'text',
             'message': 'Hi ProAgent!',
             'options': {},
             'sendTo': 'cc9008@nyu.edu',
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
[{'json': {'id': '19af57fece604a0d', 'threadId': '19af57fece604a0d', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: When the manual trigger is activated, send an email to cc9008@nyu.edu with the specified subject and content.
    TODOs:
      - Test the end-to-end workflow
      - Verify the email is sent successfully
    """
    # Step 1: Get trigger output
    trigger_output = trigger_0(trigger_input)

    # Step 2: Pass trigger output to send email action
    email_output = action_0(trigger_output)

    # Step 3: Return the email action output
    return email_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""