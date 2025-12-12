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
    - Test the manual trigger functionality.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["query"]: string = "", Required: Query. The SQL query to execute. You can use n8n expressions and $1, $2, $3, etc to refer to the 'Query Parameters' set in options below.(e.g. SELECT id, name FROM product WHERE quantity > $1 AND price <= $2). You can't use expression.
1 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '92', 'title': "WATCH: New Arizona rep. says she'll sign Epstein files discharge petition", 'description': 'Rep. Adelita Grijalva, D-Ariz., was officially sworn in to the House on Wednesday, seven weeks after she won a special election.', 'content': '<ul><li>Death of penny by US Mint raises new questions about change  </li><li>Organization spreads kindness one free wheelchair at a time  </li><li>President Trump signs government funding bill into … [+4607 chars]', 'url': 'https://abcnews.go.com/Politics/video/new-arizona-rep-shell-sign-epstein-files-discharge-127469294', 'published_at': '2025-11-13T04:49:07.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'ABC News', 'url_to_image': 'https://i.abcnewsfe.com/a/18531a3b-a856-4f0b-a4e1-43a519b88918/251112_abc_social_grijalva1_hpMain_9x16.jpg?w=992', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.559Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '93', 'title': 'A penny short: US mints final 1-cent coins after over 230 years in circulation', 'description': 'The final one-cent coins were minted in Philadelphia on Wednesday.', 'content': "From here on out, a penny saved is more than just a penny earned; it's also a relic of history.  The final penny was minted on Wednesday at the Philadelphia Mint after over 230 years in circulation a… [+2910 chars]", 'url': 'https://abcnews.go.com/GMA/Living/penny-short-us-mints-final-1-cent-coins/story?id=127465330', 'published_at': '2025-11-13T04:15:07.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'Mason Leib', 'url_to_image': 'https://i.abcnewsfe.com/a/1a3ddda2-65a4-4a32-95f3-56da810cce77/last-penny-01-gty-jt-251112_1762981654655_hpMain_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.559Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '94', 'title': 'Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump', 'description': 'Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trumpgo.com', 'content': 'Email correspondence involving sex offender Jeffrey Epstein that referenced President Donald Trump was released Wednesday by Democrats on the House Committee on Oversight and Government Reform.  Of t… [+8008 chars]', 'url': 'https://abcnews.go.com/Politics/michael-wolff-journalist-emailed-jeffrey-epstein-donald-trump/story?id=127457861', 'published_at': '2025-11-13T04:08:16.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'Meredith Deliso', 'url_to_image': 'https://i.abcnewsfe.com/a/516c30c5-d2c8-429b-ba7e-37ec9c620592/michael-wolff-gty-jt-251112_1762971125829_hpMain_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.559Z'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Execute the SQL query to get the latest 3 bloomberg_articles records.
  TODOs: 
    - Test the query execution.
    - Verify the output data structure.
  """
  params = {'options': {}, 'query': 'SELECT * FROM bloomberg_articles ORDER BY published_at DESC LIMIT 3;'}
  function = transparent_action(integration="postgres", resource="database", operation="executeQuery")
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
[{'json': {'text': "1. Title: WATCH: New Arizona rep. says she'll sign Epstein files discharge petition\nAuthor: ABC News\npublished_at: 2025-11-13T04:49:07.000Z"}}, {'json': {'text': '2. Title: A penny short: US mints final 1-cent coins after over 230 years in circulation\nAuthor: Mason Leib\npublished_at: 2025-11-13T04:15:07.000Z'}}, {'json': {'text': '3. Title: Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump\nAuthor: Meredith Deliso\npublished_at: 2025-11-13T04:08:16.000Z'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954774.688649', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "1. Title: WATCH: New Arizona rep. says she'll sign Epstein files discharge petition\nAuthor: ABC News\npublished_at: 2025-11-13T04:49:07.000Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ZrA', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "1. Title: WATCH: New Arizona rep. says she'll sign Epstein files discharge petition\nAuthor: ABC News\npublished_at: 2025-11-13T04:49:07.000Z"}]}]}]}, 'message_timestamp': '1764954774.688649'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954775.594039', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. Title: A penny short: US mints final 1-cent coins after over 230 years in circulation\nAuthor: Mason Leib\npublished_at: 2025-11-13T04:15:07.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'M=0Z2', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. Title: A penny short: US mints final 1-cent coins after over 230 years in circulation\nAuthor: Mason Leib\npublished_at: 2025-11-13T04:15:07.000Z'}]}]}]}, 'message_timestamp': '1764954775.594039'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954776.632689', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '3. Title: Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump\nAuthor: Meredith Deliso\npublished_at: 2025-11-13T04:08:16.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'pwCst', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '3. Title: Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump\nAuthor: Meredith Deliso\npublished_at: 2025-11-13T04:08:16.000Z'}]}]}]}, 'message_timestamp': '1764954776.632689'}, 'pairedItem': {'item': 2}}]
"""
def action_1(input_data):
  """
  comments: Send formatted messages to Slack channel 'general' with proper parameters.
  TODOs: 
    - Test Slack message sending.
    - Verify messages appear in the 'general' channel.
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954774.688649', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "1. Title: WATCH: New Arizona rep. says she'll sign Epstein files discharge petition\nAuthor: ABC News\npublished_at: 2025-11-13T04:49:07.000Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ZrA', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "1. Title: WATCH: New Arizona rep. says she'll sign Epstein files discharge petition\nAuthor: ABC News\npublished_at: 2025-11-13T04:49:07.000Z"}]}]}]}, 'message_timestamp': '1764954774.688649'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954775.594039', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. Title: A penny short: US mints final 1-cent coins after over 230 years in circulation\nAuthor: Mason Leib\npublished_at: 2025-11-13T04:15:07.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'M=0Z2', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. Title: A penny short: US mints final 1-cent coins after over 230 years in circulation\nAuthor: Mason Leib\npublished_at: 2025-11-13T04:15:07.000Z'}]}]}]}, 'message_timestamp': '1764954775.594039'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764954776.632689', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '3. Title: Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump\nAuthor: Meredith Deliso\npublished_at: 2025-11-13T04:08:16.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'pwCst', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '3. Title: Who is Michael Wolff, the journalist who emailed with Jeffrey Epstein about Donald Trump\nAuthor: Meredith Deliso\npublished_at: 2025-11-13T04:08:16.000Z'}]}]}]}, 'message_timestamp': '1764954776.632689'}, 'pairedItem': {'item': 2}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to query latest 3 bloomberg_articles and send formatted messages to Slack channel 'general'.
    TODOs:
      - Handle empty query results gracefully.
      - Ensure correct message formatting.
    """
    # Step 1: Call the PostgreSQL query action
    query_output = action_0(trigger_input)

    # Step 2: Extract title, author, published_at from each record
    slack_messages = []
    for i, item in enumerate(query_output, start=1):
        json_data = item.get('json', {})
        title = json_data.get('title', 'No Title')
        author = json_data.get('author', 'Unknown')
        published_at = json_data.get('published_at', 'Unknown Date')
        message_text = f"{i}. Title: {title}\nAuthor: {author}\npublished_at: {published_at}"
        slack_messages.append({"json": {"text": message_text}})

    # Step 3: Send messages to Slack
    slack_output = action_1(slack_messages)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""