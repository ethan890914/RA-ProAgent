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
  comments: 手动触发器，用于启动整个工作流
  TODOs: 
    - 测试触发器是否能正常启动工作流
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
[{'json': {'messages': [{'role': 'system', 'content': '你是一个新闻分类助手。请判断以下新闻标题属于技术类还是体育类。只回复类别名称：technology或sport。'}, {'role': 'user', 'content': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'technology'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: 调用AI接口，判断新闻标题属于技术类还是体育类
  TODOs: 
    - 根据输入新闻标题构造messages参数
    - 测试AI接口调用和返回结果
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
[{'json': {'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764907597.467809', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Vcn', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}]}]}]}, 'message_timestamp': '1764907597.467809'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 配置Slack发送消息到#general频道，消息内容来自输入数据的text字段
  TODOs: 
    - 测试Slack消息发送功能
    - 确认消息格式正确
    - 确保消息发送到指定频道
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764907597.467809', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Vcn', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}]}]}]}, 'message_timestamp': '1764907597.467809'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 实现手动触发后，调用AI判断新闻标题分类，并发送结果到Slack #general频道
    TODOs: 
      - 构造aiCompletion输入消息
      - 调用AI接口
      - 处理AI返回结果
      - 发送格式化消息到Slack
    """
    # 1. 定义新闻标题
    news_title = "Google and Accel Launch AI Futures Fund to Back Indian AI Startups."

    # 2. 构造aiCompletion输入，messages字段
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "你是一个新闻分类助手。请判断以下新闻标题属于技术类还是体育类。只回复类别名称：technology或sport。"},
                {"role": "user", "content": news_title}
            ]
        }
    }]

    # 3. 调用AI分类动作
    ai_output = action_0(ai_input)

    # 4. 提取AI返回文本，清理多余字符
    raw_text = ai_output[0]["json"]["choices"][0]["text"].strip()
    # 去除可能的markdown代码块
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`\n ")
    category = raw_text.lower()

    # 5. 构造Slack消息文本
    slack_text = f"News: {news_title}\nCategory: {category}"

    # 6. 构造Slack输入格式
    slack_input = [{"json": {"text": slack_text}}]

    # 7. 发送消息到Slack
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""