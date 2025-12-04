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
  comments: 手动触发器，用户点击按钮触发工作流执行。
  TODOs: 
    - 测试触发器是否能正常触发
    - 验证触发器输出格式
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
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
[{'json': {'text': 'Hello World!'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764886198.987969', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Hello World!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'rfS', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Hello World!'}]}]}]}, 'message_timestamp': '1764886198.987969'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: 更新Slack发送消息动作，消息内容从输入数据读取，保持发送到#general频道。
  TODOs: 
    - 测试发送消息是否成功
    - 验证消息内容格式
    - 完善工作流实现
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764886198.987969', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Hello World!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'rfS', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Hello World!'}]}]}]}, 'message_timestamp': '1764886198.987969'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 手动触发后，发送固定消息到Slack频道#general。
    TODOs: 
      - 测试工作流执行
      - 验证消息发送成功
    """
    # 构造Slack消息输入，消息内容固定
    slack_input = [{"json": {"text": "Hello World!"}}]
    # 调用发送消息动作
    slack_output = action_0(slack_input)
    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""