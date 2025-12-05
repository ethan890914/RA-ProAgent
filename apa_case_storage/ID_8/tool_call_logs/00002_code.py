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
  comments: Manual trigger to start the workflow when user clicks.
  TODOs: 
    - Test trigger firing
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Generate a small conversation between three people. Total word counts less than 500.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Use AI to generate a small conversation between three people with total word count less than 500.
  TODOs: 
    - Build input messages in workflow
    - Test AI output format
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
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
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764907078.706589', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '0eQe', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!'}]}]}]}, 'message_timestamp': '1764907078.706589'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send the generated conversation to Slack #general channel as a text message with correct parameters.
  TODOs: 
    - Test Slack message sending
    - Verify message appears in #general channel
  """
  params = { 'channelId': {'mode': 'name', 'value': 'general'},
             'messageType': 'text',
             'select': 'channel',
             'text': '={{$json["text"]}}'}
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764907078.706589', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '0eQe', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a short conversation between three friends:\n\n---\n\n**Emma:** Hey guys, have you decided what movie we’re watching tonight?\n\n**Liam:** Not yet. I was thinking maybe something funny? I could use a good laugh.\n\n**Sophia:** Comedy sounds great! But I’m also in the mood for something with a bit of action.\n\n**Emma:** How about an action-comedy? Like one of those buddy cop movies?\n\n**Liam:** Perfect! I love those. Any favorites?\n\n**Sophia:** What about “Rush Hour”? It’s classic and always makes me laugh.\n\n**Emma:** Yes! And it’s not too long, so we can still grab some ice cream after.\n\n**Liam:** Ice cream sounds amazing. I’m in.\n\n**Sophia:** Me too. Let’s do it!\n\n---\n\nLet me know if you want a different style or topic!'}]}]}]}, 'message_timestamp': '1764907078.706589'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to generate a small conversation between three people using AI and send it to Slack #general channel.
    TODOs: 
      - Build AI input messages
      - Extract AI output text
      - Format Slack input
      - Test end-to-end
    """
    # Step 1: Build AI input messages
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Generate a small conversation between three people. Total word counts less than 500."}
            ]
        }
    }]

    # Step 2: Call AI completion action
    ai_output = action_0(ai_input)

    # Step 3: Extract conversation text from AI output
    conversation = ai_output[0]["json"]["choices"][0]["text"]

    # Step 4: Wrap conversation text for Slack input
    slack_input = [{"json": {"text": conversation}}]

    # Step 5: Send to Slack #general channel
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""