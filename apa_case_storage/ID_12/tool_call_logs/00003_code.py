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
    - Ensure output format is correct for downstream actions
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
def action_0(input_data):
  """
  comments: Read news headlines from the specified Google Sheets document and sheet.
  TODOs: 
    - Test reading data from the sheet
    - Verify output data format
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'news'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Google and Accel Launch AI Futures Fund to Back Indian AI Startups'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Meta in Talks to Buy Google’s AI Chips'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Zoom Raises Forecast on Strong AI Companion 3.0 Adoption'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Gotham FC Wins 2025 NWSL Championship'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': '5th Khelo India University Games Kick Off in Jaipur'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as technology or sport.'}, {'role': 'user', 'content': 'South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Technology'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Sport'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'sport'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Use AI to classify each news headline as technology or sport.
  TODOs: 
    - Build messages array in workflow
    - Test classification results
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
[{'json': {'text': '1. News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}}, {'json': {'text': '2. News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}}, {'json': {'text': '3. News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}}, {'json': {'text': '4. News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}}, {'json': {'text': '5. News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}}, {'json': {'text': '6. News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}}, {'json': {'text': '7. News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}}, {'json': {'text': '8. News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}}, {'json': {'text': '9. News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}}, {'json': {'text': '10. News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909198.060899', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '1. News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'GIXFv', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '1. News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909198.060899'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909198.981209', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'r/8pD', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909198.981209'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909199.914379', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '3. News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'CFLJ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '3. News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909199.914379'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909200.831739', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '4. News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'b5ra', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '4. News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909200.831739'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909201.879139', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '5. News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'C7BQO', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '5. News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909201.879139'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909202.772979', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '6. News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'n7Bth', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '6. News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909202.772979'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909203.682039', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '7. News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ZLf9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '7. News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909203.682039'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909204.591199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '8. News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'BrV0b', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '8. News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909204.591199'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909205.506639', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '9. News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'hJy2B', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '9. News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909205.506639'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909206.402479', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '10. News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'NvT', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '10. News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909206.402479'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data):
  """
  comments: Send classification results to Slack channel #news with proper parameters.
  TODOs: 
    - Test Slack message sending
    - Verify message content and format
  """
  params = { 'channelId': {'mode': 'name', 'value': 'news'},
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
[{'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909198.060899', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '1. News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'GIXFv', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '1. News: Alphabet’s AI Stock Rally Puts Google on Track for $4 Trillion Valuation\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909198.060899'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909198.981209', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'r/8pD', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. News: Amazon Unveils “Leo Ultra,” Its Starlink Competitor for Enterprise\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909198.981209'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909199.914379', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '3. News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'CFLJ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '3. News: Google and Accel Launch AI Futures Fund to Back Indian AI Startups\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909199.914379'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909200.831739', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '4. News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'b5ra', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '4. News: Meta in Talks to Buy Google’s AI Chips\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909200.831739'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909201.879139', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '5. News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'C7BQO', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '5. News: Zoom Raises Forecast on Strong AI Companion 3.0 Adoption\nCategory: technology'}]}]}]}, 'message_timestamp': '1764909201.879139'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909202.772979', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '6. News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'n7Bth', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '6. News: Gotham FC Wins 2025 NWSL Championship\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909202.772979'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909203.682039', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '7. News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ZLf9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '7. News: NCAA Rejects Proposal to Allow College Athletes to Bet on Pro Sports\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909203.682039'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909204.591199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '8. News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'BrV0b', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '8. News: Connor McDavid’s Status Uncertain Ahead of Oilers vs. Stars Game\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909204.591199'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909205.506639', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '9. News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'hJy2B', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '9. News: 5th Khelo India University Games Kick Off in Jaipur\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909205.506639'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764909206.402479', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '10. News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'NvT', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '10. News: South Dakota State Men’s Basketball Joins Cancun Challenge Tournament in Mexico\nCategory: sport'}]}]}]}, 'message_timestamp': '1764909206.402479'}, 'pairedItem': {'item': 9}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to classify news headlines from Google Sheets and send results to Slack.
    TODOs: 
      - Test the entire workflow
      - Verify AI classification
      - Ensure Slack messages are formatted correctly
    """
    # Step 1: Start from manual trigger
    # trigger_input is not used as manual trigger output is empty

    # Step 2: Read news headlines from Google Sheets
    sheets_output = action_0(trigger_input)

    # Step 3: Extract headlines
    headlines = []
    for item in sheets_output:
        headline = item["json"].get("Headlines", "")
        if headline:
            headlines.append(headline)

    # Step 4: Build aiCompletion input
    ai_input = []
    for headline in headlines:
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as technology or sport."},
            {"role": "user", "content": headline}
        ]
        ai_input.append({"json": {"messages": messages}})

    # Step 5: Call aiCompletion
    ai_output = action_1(ai_input)

    # Step 6: Parse AI output and prepare Slack messages
    slack_input = []
    for i, item in enumerate(ai_output, 1):
        ai_text = item["json"]["choices"][0]["text"].strip().lower()
        # Simple classification parsing
        if "technology" in ai_text:
            category = "technology"
        elif "sport" in ai_text:
            category = "sport"
        else:
            category = "unknown"

        headline = headlines[i-1]
        message_text = f"{i}. News: {headline}\nCategory: {category}"
        slack_input.append({"json": {"text": message_text}})

    # Step 7: Send messages to Slack
    slack_output = action_2(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""