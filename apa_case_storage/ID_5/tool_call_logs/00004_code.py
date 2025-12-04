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
  comments: 定义手动触发器，用户点击按钮时触发工作流。
  TODOs: 
    - 实现触发器逻辑
    - 测试触发器触发
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["documentId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Document . "mode" should be one of ['url', 'id']: 
  0.0 params["documentId"]["value"](when "mode"="url"): string: By URL
  0.1 params["documentId"]["value"](when "mode"="id"): string: By ID
1 params["sheetName"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Sheet . "mode" should be one of ['url', 'id']: 
  1.0 params["sheetName"]["value"](when "mode"="url"): string: By URL
  1.1 params["sheetName"]["value"](when "mode"="id"): string: By ID
2 params["filtersUI"]: dict[str,list[dict[str,any]]] = {}: Filters(Add Filter) . properties description:
  ...hidden...
3 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'row_number': 2, 'Headlines': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Headlines': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Headlines': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Headlines': 'Meta in Talks to Buy Google’s AI Chips'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Headlines': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Headlines': 'Gotham FC Wins 2025 NWSL Championship'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Headlines': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Headlines': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Headlines': '5th Khelo India University Games Kick Off in Jaipur'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Headlines': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: 配置Google Sheets读取动作，读取指定文档ID和工作表名称的数据。
  TODOs: 
    - 测试读取动作，确保能正确获取数据
    - 调试数据格式，确保后续处理正确
  """
  params = {
             "documentId": {
               "mode": "id",
               "value": "1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c"
             },
             "sheetName": {
               "mode": "id",
               "value": "news"
             },
             "filtersUI": {},
             "options": {}
           }
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
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
[{'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Meta in Talks to Buy Google’s AI Chips'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Gotham FC Wins 2025 NWSL Championship'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': '5th Khelo India University Games Kick Off in Jaipur'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.285309', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'AZ+3d', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}]}]}]}, 'message_timestamp': '1764602186.285309'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.451169', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'z7wOS', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}]}]}]}, 'message_timestamp': '1764602186.451169'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.591059', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '+Da+', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}]}]}]}, 'message_timestamp': '1764602186.591059'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.706359', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Meta in Talks to Buy Google’s AI Chips', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'haDoO', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Meta in Talks to Buy Google’s AI Chips'}]}]}]}, 'message_timestamp': '1764602186.706359'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.870449', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Btlzn', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}]}]}]}, 'message_timestamp': '1764602186.870449'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.998609', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Gotham FC Wins 2025 NWSL Championship', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'QnVK', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Gotham FC Wins 2025 NWSL Championship'}]}]}]}, 'message_timestamp': '1764602186.998609'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.119199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'JOjdZ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}]}]}]}, 'message_timestamp': '1764602187.119199'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.235079', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'NSq', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}]}]}]}, 'message_timestamp': '1764602187.235079'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.354109', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '5th Khelo India University Games Kick Off in Jaipur', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'CEh', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '5th Khelo India University Games Kick Off in Jaipur'}]}]}]}, 'message_timestamp': '1764602187.354109'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.494339', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'LyZ8', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}]}]}]}, 'message_timestamp': '1764602187.494339'}, 'pairedItem': {'item': 9}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 完善Slack发送消息动作参数，逐条发送新闻标题到#general频道。
  TODOs: 
    - 测试Slack消息发送功能
    - 调试参数格式
    - 确保消息能够成功发送到指定频道
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.285309', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'AZ+3d', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}]}]}]}, 'message_timestamp': '1764602186.285309'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.451169', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'z7wOS', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}]}]}]}, 'message_timestamp': '1764602186.451169'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.591059', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '+Da+', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}]}]}]}, 'message_timestamp': '1764602186.591059'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.706359', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Meta in Talks to Buy Google’s AI Chips', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'haDoO', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Meta in Talks to Buy Google’s AI Chips'}]}]}]}, 'message_timestamp': '1764602186.706359'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.870449', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Btlzn', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}]}]}]}, 'message_timestamp': '1764602186.870449'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602186.998609', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Gotham FC Wins 2025 NWSL Championship', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'QnVK', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Gotham FC Wins 2025 NWSL Championship'}]}]}]}, 'message_timestamp': '1764602186.998609'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.119199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'JOjdZ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}]}]}]}, 'message_timestamp': '1764602187.119199'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.235079', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'NSq', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}]}]}]}, 'message_timestamp': '1764602187.235079'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.354109', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '5th Khelo India University Games Kick Off in Jaipur', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'CEh', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '5th Khelo India University Games Kick Off in Jaipur'}]}]}]}, 'message_timestamp': '1764602187.354109'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764602187.494339', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'LyZ8', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}]}]}]}, 'message_timestamp': '1764602187.494339'}, 'pairedItem': {'item': 9}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 手动触发后，读取Google Sheets中news表的数据，并逐条发送新闻标题到Slack的#general频道。
    TODOs:
      - 测试手动触发是否正常
      - 确认读取数据正确
      - 确认Slack消息发送成功
    """
    # 第一步：调用读取Google Sheets数据动作
    sheets_data = action_0(trigger_input)

    # 第二步：构建Slack发送数据，逐条发送新闻标题
    slack_input = []
    for item in sheets_data:
        headline = item["json"].get("Headlines", "")
        slack_input.append({
            "json": {
                "select": "channel",
                "channelId": {"mode": "name", "value": "general"},
                "messageType": "text",
                "text": headline
            }
        })

    # 第三步：调用Slack发送消息动作
    slack_output = action_1(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""