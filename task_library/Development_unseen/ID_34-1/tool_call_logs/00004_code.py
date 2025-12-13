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
  comments: Manual trigger to start the workflow on user click.
  TODOs: 
    - Test trigger activation
    - Verify output format
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
[{'json': {}, 'pairedItem': {'item': 0}}]

3.Output:
[{'json': {'id': '1', 'title': 'Canada loses measles elimination status after ongoing outbreaks', 'description': 'International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America', 'content': 'Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars]', 'url': 'https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798', 'published_at': '2025-11-11T07:45:36.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'DEVI SHASTRI AP health writer', 'url_to_image': 'https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}, {'json': {'id': '2', 'title': 'New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain', 'description': "New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation", 'content': 'WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars]', 'url': 'https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101', 'published_at': '2025-11-11T07:29:35.000Z', 'source_name': 'ABC News', 'source_id': 'abc-news', 'author': 'CHARLOTTE GRAHAM-MCLAY Associated Press', 'url_to_image': 'https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600', 'content_length': 214, 'export_date': '2025-11-28T18:28:32.556Z'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Execute SQL query on PostgreSQL to get data from bloomberg_articles table, limit 2 rows.
  TODOs: 
    - Test query execution
    - Verify output data format
  """
  params = {'options': {}, 'query': 'SELECT * FROM bloomberg_articles LIMIT 2;'}
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
[{'json': {'text': "PostgreSQL Query Result:\nid=1, title=Canada loses measles elimination status after ongoing outbreaks, description=International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America, content=Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars], url=https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798, published_at=2025-11-11T07:45:36.000Z, source_name=ABC News, source_id=abc-news, author=DEVI SHASTRI AP health writer, url_to_image=https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600, content_length=214, export_date=2025-11-28T18:28:32.556Z\nid=2, title=New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain, description=New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation, content=WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars], url=https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101, published_at=2025-11-11T07:29:35.000Z, source_name=ABC News, source_id=abc-news, author=CHARLOTTE GRAHAM-MCLAY Associated Press, url_to_image=https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600, content_length=214, export_date=2025-11-28T18:28:32.556Z"}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079105.410869', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "PostgreSQL Query Result:\nid=1, title=Canada loses measles elimination status after ongoing outbreaks, description=International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America, content=Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars], url=<https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798>, published_at=2025-11-11T07:45:36.000Z, source_name=ABC News, source_id=abc-news, author=DEVI SHASTRI AP health writer, url_to_image=<https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600>, content_length=214, export_date=2025-11-28T18:28:32.556Z\nid=2, title=New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain, description=New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation, content=WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars], url=<https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101>, published_at=2025-11-11T07:29:35.000Z, source_name=ABC News, source_id=abc-news, author=CHARLOTTE GRAHAM-MCLAY Associated Press, url_to_image=<https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600>, content_length=214, export_date=2025-11-28T18:28:32.556Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'sN+', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'PostgreSQL Query Result:\nid=1, title=Canada loses measles elimination status after ongoing outbreaks, description=International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America, content=Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars], url='}, {'type': 'link', 'url': 'https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798'}, {'type': 'text', 'text': ', published_at=2025-11-11T07:45:36.000Z, source_name=ABC News, source_id=abc-news, author=DEVI SHASTRI AP health writer, url_to_image='}, {'type': 'link', 'url': 'https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600'}, {'type': 'text', 'text': ", content_length=214, export_date=2025-11-28T18:28:32.556Z\nid=2, title=New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain, description=New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation, content=WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars], url="}, {'type': 'link', 'url': 'https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101'}, {'type': 'text', 'text': ', published_at=2025-11-11T07:29:35.000Z, source_name=ABC News, source_id=abc-news, author=CHARLOTTE GRAHAM-MCLAY Associated Press, url_to_image='}, {'type': 'link', 'url': 'https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600'}, {'type': 'text', 'text': ', content_length=214, export_date=2025-11-28T18:28:32.556Z'}]}]}]}, 'message_timestamp': '1765079105.410869'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send message to Slack channel #general with the text from input data.
  TODOs: 
    - Test Slack message sending
    - Verify message format in Slack
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765079105.410869', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "PostgreSQL Query Result:\nid=1, title=Canada loses measles elimination status after ongoing outbreaks, description=International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America, content=Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars], url=<https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798>, published_at=2025-11-11T07:45:36.000Z, source_name=ABC News, source_id=abc-news, author=DEVI SHASTRI AP health writer, url_to_image=<https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600>, content_length=214, export_date=2025-11-28T18:28:32.556Z\nid=2, title=New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain, description=New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation, content=WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars], url=<https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101>, published_at=2025-11-11T07:29:35.000Z, source_name=ABC News, source_id=abc-news, author=CHARLOTTE GRAHAM-MCLAY Associated Press, url_to_image=<https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600>, content_length=214, export_date=2025-11-28T18:28:32.556Z", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'sN+', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'PostgreSQL Query Result:\nid=1, title=Canada loses measles elimination status after ongoing outbreaks, description=International health experts say Canada is no longer measles-free because of ongoing outbreaks, as childhood vaccination rates fall and the highly contagious virus spreads across North and South America, content=Canada is no longer measles-free because of ongoing outbreaks, international health experts said Monday, as childhood vaccination rates fall and the highly contagious virus spreads across North and S… [+5742 chars], url='}, {'type': 'link', 'url': 'https://abcnews.go.com/Health/wireStory/canada-loses-measles-elimination-status-after-ongoing-outbreaks-127379798'}, {'type': 'text', 'text': ', published_at=2025-11-11T07:45:36.000Z, source_name=ABC News, source_id=abc-news, author=DEVI SHASTRI AP health writer, url_to_image='}, {'type': 'link', 'url': 'https://i.abcnewsfe.com/a/6b1aa275-9536-4ffa-8780-5721db4aaa4c/wirestory_1ac3a4bdc7546fac5d8e111bf5196e1e_16x9.jpg?w=1600'}, {'type': 'text', 'text': ", content_length=214, export_date=2025-11-28T18:28:32.556Z\nid=2, title=New Zealand will remove police from gun licensing but near-total semiautomatics ban to remain, description=New Zealand's government has announced changes to firearms laws Tuesday which include ending police officer involvement in gun regulation, content=WELLINGTON, New Zealand -- New Zealands government will end the involvement of police officers in regulating gun ownership, an official said Tuesday as she announced sweeping firearms law reforms.  T… [+4649 chars], url="}, {'type': 'link', 'url': 'https://abcnews.go.com/International/wireStory/new-zealand-remove-police-gun-licensing-total-semiautomatics-127399101'}, {'type': 'text', 'text': ', published_at=2025-11-11T07:29:35.000Z, source_name=ABC News, source_id=abc-news, author=CHARLOTTE GRAHAM-MCLAY Associated Press, url_to_image='}, {'type': 'link', 'url': 'https://i.abcnewsfe.com/a/cddcb8dd-ea47-4660-b550-2014a686970e/wirestory_f370885a43616f652410fe6d94768ef2_16x9.jpg?w=1600'}, {'type': 'text', 'text': ', content_length=214, export_date=2025-11-28T18:28:32.556Z'}]}]}]}, 'message_timestamp': '1765079105.410869'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered manually, executes SQL query on Postgres, sends formatted result to Slack #general channel.
    TODOs:
      - Test end-to-end workflow
      - Verify Slack message format
    """
    # Step 1: Start with manual trigger
    trigger_output = trigger_0(input_data=None)

    # Step 2: Execute SQL query
    query_output = action_0(trigger_output)

    # Step 3: Extract query result and format message
    # The query_output is a list of dicts with 'json' key containing row data
    rows = query_output
    if not rows:
        message_text = "PostgreSQL Query Result:\nNo data returned."
    else:
        # Format each row as string
        row_texts = []
        for row in rows:
            # Convert each row json to string key=value pairs
            kv_pairs = [f"{k}={v}" for k, v in row['json'].items()]
            row_text = ", ".join(kv_pairs)
            row_texts.append(row_text)
        message_text = "PostgreSQL Query Result:\n" + "\n".join(row_texts)

    # Step 4: Prepare Slack input
    slack_input = [{"json": {"text": message_text}}]

    # Step 5: Send message to Slack
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""