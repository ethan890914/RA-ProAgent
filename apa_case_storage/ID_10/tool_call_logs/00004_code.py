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
  comments: 手动触发器，用户点击按钮时触发流程
  TODOs: 
    - 测试触发器是否能正常触发
    - 确认触发器输出格式
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
[{'json': {'messages': [{'role': 'system', 'content': '你是一个新闻分类助手，请判断以下新闻标题属于技术类(technology)还是体育类(sport)。'}, {'role': 'user', 'content': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'technology'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: 调用GPT模型，根据新闻标题判断类别是technology还是sport，参数使用n8n表达式字符串格式
  TODOs: 
    - 实现参数传递和调用
    - 测试返回结果格式
  """
  params = {
             "messages": "=[{\"role\":\"system\",\"content\":\"你是一个新闻分类助手，请判断以下新闻标题属于技术类(technology)还是体育类(sport)。\"},{\"role\":\"user\",\"content\":\"Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\"}]"
           }
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["select"]: enum[string] = "", Required: Send Message To(Select...) . Available values:
  0.0 value=="channel": Channel
  0.1 value=="user": User
1 params["channelId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Channel. The Slack channel to send to(Select a channel...) . "mode" should be one of ['id', 'name', 'url']: 
  1.0 params["channelId"]["value"](when "mode"="id"): string: By ID(C0122KQ70S7E)
  1.1 params["channelId"]["value"](when "mode"="name"): string: By Name(#general)
  1.2 params["channelId"]["value"](when "mode"="url"): string: By URL(https://app.slack.com/client/TS9594PZK/B0556F47Z3A)
2 params["user"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}: User(Select a user...) . "mode" should be one of ['id', 'username']: 
  ...hidden...
3 params["messageType"]: enum[string] = "text": Message Type. Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more . Available values:
  3.0 value=="text": Simple Text Message. Supports basic Markdown
  3.1 value=="block": Blocks. Combine text, buttons, form elements, dividers and more in Slack 's visual builder
  3.2 value=="attachment": Attachments
4 params["text"]: string = "": Notification Text. Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options".
5 params["blocksUi"]: string = "", Required: Blocks. Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>
6 params["attachments"]: list[dict] = [{}]: Attachments(Add attachment item) . properties description:
  ...hidden...
7 params["otherOptions"]: dict = {}: Options. Other options to set(Add options) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764614349.261579', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '9SD1', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}]}]}]}, 'message_timestamp': '1764614349.261579'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 发送消息到Slack的#general频道，消息内容动态来自输入数据的text字段
  TODOs: 
    - 完善参数传递
    - 测试消息发送
    - 验证频道和消息格式
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "general"
             },
             "messageType": "text",
             "text": "={{$json[\"text\"]}}"
           }
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764614349.261579', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '9SD1', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups.\nCategory: technology'}]}]}]}, 'message_timestamp': '1764614349.261579'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 手动触发触发器，调用AI判断新闻类别，并发送结果到Slack #general频道
    TODOs:
      - 测试手动触发器触发流程
      - 测试AI分类调用及结果解析
      - 测试Slack消息发送
    """
    # 调用aiCompletion，固定新闻标题
    ai_input = [{"json": {"messages": [
        {"role": "system", "content": "你是一个新闻分类助手，请判断以下新闻标题属于技术类(technology)还是体育类(sport)。"},
        {"role": "user", "content": "Google and Accel Launch AI Futures Fund to Back Indian AI Startups."}
    ]}}]
    ai_output = action_0(ai_input)

    # 解析AI返回文本，默认只取第一个结果
    ai_text = ai_output[0]["json"].get("choices", [{}])[0].get("text", "") if ai_output else ""

    # 简单判断分类关键词
    category = "technology" if "technology" in ai_text.lower() else "sport"

    # 构造Slack消息内容
    news_title = "Google and Accel Launch AI Futures Fund to Back Indian AI Startups."
    slack_message = f"News: {news_title}\nCategory: {category}"

    slack_input = [{"json": {"text": slack_message}}]

    # 设置Slack发送参数，频道为#general
    params = {
        "select": "channel",
        "channelId": {"mode": "name", "value": "general"},
        "messageType": "text",
        "text": slack_message
    }
    slack_output = action_1(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""