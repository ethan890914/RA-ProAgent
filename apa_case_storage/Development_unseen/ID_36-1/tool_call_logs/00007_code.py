"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
None

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: Trigger the workflow manually by user
  TODOs: 
    - Test the trigger
    - Ensure it outputs the correct trigger input
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a professional PostgreSQL programmer, please only output a SQL string'}, {'role': 'user', 'content': "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3, and sort with column published_at"}]}}]

3.Output:
[{'json': {'choices': [{'text': '```sql\nSELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;\n```'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Generate SQL query using AI completion with system and user prompts
  TODOs: 
    - Implement the input messages array in the workflow
    - Test the AI completion output
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["query"]: string = "", Required: Query. The SQL query to execute. You can use n8n expressions and $1, $2, $3, etc to refer to the 'Query Parameters' set in options below.(e.g. SELECT id, name FROM product WHERE quantity > $1 AND price <= $2). You can't use expression.
1 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'query': 'SELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;'}}]

3.Output:
[{'json': {'id': '11', 'title': 'Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict', 'description': 'President Donald Trump has asked the U.S. Supreme Court to throw out a jury’s finding in a civil lawsuit that he sexually abused writer E', 'content': 'NEW YORK -- President Donald Trump asked the U.S. Supreme Court on Monday to throw out a jurys finding in a civil lawsuit that he sexually abused writer E. Jean Carroll at a Manhattan department stor… [+4136 chars]', 'url': 'https://abcnews.go.com/Politics/wireStory/trump-asks-supreme-court-throw-jean-carrolls-5-127395697', 'published_at': '2025-11-11T05:05:52.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'MICHAEL R. SISAK Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/61c5aacb-7df6-4edd-9030-6d68dfcdad11/wirestory_be62982deb6821b62e0471f5bea3e64d_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '10', 'title': 'Colombian governor says he survived an assasination attempt in oil-rich Arauca province', 'description': "The governor of Colombia's Arauca province says he survived an assassination attempt while traveling between towns", 'content': "BOGOTA, Colombia -- The governor of Colombias Arauca province said Monday that he survived an assassination attempt while traveling between two towns in the country's eastern plains.  Gov. Renson Mar… [+2474 chars]", 'url': 'https://abcnews.go.com/International/wireStory/colombian-governor-survived-assasination-attempt-oil-rich-arauca-127395816', 'published_at': '2025-11-11T05:13:29.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'MANUEL RUEDA Associated Press', 'url_to_image': 'https://s.abcnews.com/images/US/abc_news_default_2000x2000_update_16x9_992.jpg', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '9', 'title': "Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge", 'description': "A Wisconsin man accused of trying to burn down a congressman's office earlier this year because he was upset over the federal TikTok ban has pleaded no contest to felony arson", 'content': "MADISON, Wis. -- A Wisconsin man accused of trying to burn down a congressman's office earlier this year because he was upset over the federal TikTok ban has pleaded no contest to felony arson.  Caid… [+1900 chars]", 'url': 'https://abcnews.go.com/US/wireStory/wisconsin-man-accused-setting-fire-congressmans-office-pleads-127394781', 'published_at': '2025-11-11T05:21:53.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'TODD RICHMOND Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/1578314c-4a5e-4da7-9056-369e14d202b6/wirestory_77f915df025d38910414c26808f7a8c0_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Execute the SQL query generated by AI in PostgreSQL database with correct params
  TODOs: 
    - Test the query execution and output format
  """
  params = {'options': {}, 'query': 'SELECT * FROM bloomberg_articles ORDER BY published_at LIMIT 3;'}
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
[{'json': {'text': '1. Title: Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict\npublished_at: 2025-11-11T05:05:52.000Z'}}, {'json': {'text': '2. Title: Colombian governor says he survived an assasination attempt in oil-rich Arauca province\npublished_at: 2025-11-11T05:13:29.000Z'}}, {'json': {'text': "3. Title: Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge\npublished_at: 2025-11-11T05:21:53.000Z"}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079810.877649', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '1. Title: Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict\npublished_at: 2025-11-11T05:05:52.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '5Rcrp', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '1. Title: Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict\npublished_at: 2025-11-11T05:05:52.000Z'}]}]}]}, 'message_timestamp': '1765079810.877649'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079811.847089', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. Title: Colombian governor says he survived an assasination attempt in oil-rich Arauca province\npublished_at: 2025-11-11T05:13:29.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'bFfH', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. Title: Colombian governor says he survived an assasination attempt in oil-rich Arauca province\npublished_at: 2025-11-11T05:13:29.000Z'}]}]}]}, 'message_timestamp': '1765079811.847089'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079812.823269', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "3. Title: Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge\npublished_at: 2025-11-11T05:21:53.000Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'EHhG', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "3. Title: Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge\npublished_at: 2025-11-11T05:21:53.000Z"}]}]}]}, 'message_timestamp': '1765079812.823269'}, 'pairedItem': {'item': 2}}]
"""
def action_2(input_data):
  """
  comments: Send the formatted query results to Slack channel general with correct params
  TODOs: 
    - Test sending messages to Slack
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079810.877649', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '1. Title: Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict\npublished_at: 2025-11-11T05:05:52.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '5Rcrp', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '1. Title: Trump asks Supreme Court to throw out E. Jean Carroll’s $5 million verdict\npublished_at: 2025-11-11T05:05:52.000Z'}]}]}]}, 'message_timestamp': '1765079810.877649'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079811.847089', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '2. Title: Colombian governor says he survived an assasination attempt in oil-rich Arauca province\npublished_at: 2025-11-11T05:13:29.000Z', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'bFfH', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '2. Title: Colombian governor says he survived an assasination attempt in oil-rich Arauca province\npublished_at: 2025-11-11T05:13:29.000Z'}]}]}]}, 'message_timestamp': '1765079811.847089'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079812.823269', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "3. Title: Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge\npublished_at: 2025-11-11T05:21:53.000Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'EHhG', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "3. Title: Wisconsin man accused of setting fire to congressman's office pleads no contest to arson charge\npublished_at: 2025-11-11T05:21:53.000Z"}]}]}]}, 'message_timestamp': '1765079812.823269'}, 'pairedItem': {'item': 2}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to generate SQL query from AI, execute it in PostgreSQL, and send results to Slack
    TODOs:
      - Build aiCompletion input with system and user messages
      - Clean AI output SQL query
      - Format Slack messages
    """
    # Step 1: Start from manual trigger
    trigger_output = trigger_0(None)

    # Step 2: Build aiCompletion input
    ai_input = [{"json": {"messages": [
        {"role": "system", "content": "You are a professional PostgreSQL programmer, please only output a SQL string"},
        {"role": "user", "content": "Please write a SQL query, which select first three rows from table 'bloomberg_articles' and limit the rows to 3, and sort with column published_at"}
    ]}}]

    # Step 3: Call aiCompletion
    ai_output = action_0(ai_input)

    # Step 4: Extract and clean SQL query
    ai_text = ai_output[0]['json']['choices'][0]['text'].strip()
    # Remove markdown if present
    if ai_text.startswith('```'):
        ai_text = ai_text.split('\n', 1)[1] if '\n' in ai_text else ai_text[3:]
        if ai_text.endswith('```'):
            ai_text = ai_text[:-3]
        ai_text = ai_text.strip()

    # Step 5: Prepare input for PostgreSQL
    pg_input = [{"json": {"query": ai_text}}]

    # Step 6: Call PostgreSQL executeQuery
    pg_output = action_1(pg_input)

    # Step 7: Format Slack messages
    slack_input = []
    for i, row in enumerate(pg_output):
        title = row['json'].get('title', '')
        published_at = row['json'].get('published_at', '')
        message_text = f"{i+1}. Title: {title}\npublished_at: {published_at}"
        slack_input.append({"json": {"text": message_text}})

    # Step 8: Send messages to Slack
    slack_output = action_2(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""