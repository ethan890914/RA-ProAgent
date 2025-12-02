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
  comments: Trigger the workflow manually on button click.
  TODOs: 
    - Test trigger activation
    - Verify output data format
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
  comments: Read all rows from the specified Google Sheet containing news headlines.
  TODOs: 
    - Test reading headlines
    - Verify output data format
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
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Meta in Talks to Buy Google’s AI Chips'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Gotham FC Wins 2025 NWSL Championship'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': '5th Khelo India University Games Kick Off in Jaipur'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Sport'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Classify each news headline as technology or sport using AI.
  TODOs: 
    - Build messages input in workflow
    - Test AI classification
  """
  params = {}  # to be Implemented
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
[{'json': {'text': 'News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}}, {'json': {'text': 'News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}}, {'json': {'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}}, {'json': {'text': 'News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}}, {'json': {'text': 'News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}}, {'json': {'text': 'News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}}, {'json': {'text': 'News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}}, {'json': {'text': 'News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}}, {'json': {'text': 'News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}}, {'json': {'text': 'News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.149819', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Qdh', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.149819'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.292989', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'L+B3', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.292989'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.439149', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'MK8', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.439149'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.567029', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'GW=', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.567029'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.692969', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 't8s', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.692969'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.828709', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '45qoD', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615185.828709'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.975709', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Llp4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615185.975709'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.131769', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'YNcE', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.131769'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.287659', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '2Huum', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.287659'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.412189', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'tSN09', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.412189'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Send classification results as Slack messages to #general channel with proper parameters.
  TODOs: 
    - Test sending messages to Slack
    - Verify message format in Slack
    - Handle Slack API errors
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.149819', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Qdh', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.149819'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.292989', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'L+B3', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.292989'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.439149', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'MK8', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.439149'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.567029', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'GW=', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.567029'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.692969', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 't8s', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}]}]}]}, 'message_timestamp': '1764615185.692969'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.828709', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '45qoD', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615185.828709'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615185.975709', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Llp4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615185.975709'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.131769', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'YNcE', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.131769'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.287659', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '2Huum', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.287659'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764615186.412189', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'tSN09', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}]}]}]}, 'message_timestamp': '1764615186.412189'}, 'pairedItem': {'item': 9}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to read news headlines from Google Sheets, classify with AI, and send results to Slack.
    TODOs:
      - Test end-to-end workflow
      - Verify Slack message delivery
      - Handle empty or malformed data
    """
    # Step 1: Read news headlines from Google Sheets
    news_data = action_0(trigger_input)

    # Step 2: Build aiCompletion input messages
    ai_input = []
    for item in news_data:
        headline = item['json'].get('Headlines', '')
        messages_data = [
            {"role": "system", "content": "You are a news classifier. Classify as technology or sport."},
            {"role": "user", "content": headline}
        ]
        ai_input.append({"json": {"messages": messages_data}})

    # Step 3: Call aiCompletion action
    ai_output = action_1(ai_input)

    # Step 4: Parse AI output and prepare Slack messages
    slack_input = []
    for i, item in enumerate(ai_output):
        headline = news_data[i]['json'].get('Headlines', '')
        ai_text = item['json']['choices'][0]['text'].lower()
        category = "technology" if "technology" in ai_text else "sport"
        slack_text = f"News: {headline}\nCategory: {category}"
        slack_input.append({"json": {"text": slack_text}})

    # Step 5: Send messages to Slack channel #general
    slack_output = action_2(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""