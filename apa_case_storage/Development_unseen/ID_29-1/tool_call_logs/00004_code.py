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
  comments: Manual trigger to start the workflow on user click.
  TODOs: 
    - Test the trigger to ensure it fires correctly.
    - Use this trigger as input to the main workflow.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["method"]: enum[string] = "GET": Method. The request method to use . Available values:
  0.0 value=="DELETE": DELETE
  0.1 value=="GET": GET
  0.2 value=="HEAD": HEAD
  0.3 value=="OPTIONS": OPTIONS
  0.4 value=="PATCH": PATCH
  0.5 value=="POST": POST
  0.6 value=="PUT": PUT
1 params["url"]: string = "", Required: URL. The URL to make the request to(http://example.com/index.html)
2 params["sendQuery"]: boolean = False: Send Query Parameters. Whether the request has query params or not. You can't use expression.
3 params["specifyQuery"]: enum[string] = "keypair", Activate(Not Required) when (sendQuery in [True]), otherwise do not provide: Specify Query Parameters . Available values:
  3.0 value=="keypair": Using Fields Below
  3.1 value=="json": Using JSON
4 params["queryParameters"]: dict[str,list[dict[str,any]]] = {'parameters': [{'name': '', 'value': ''}]}, Activate(Not Required) when (sendQuery in [True] and specifyQuery in ['keypair']), otherwise do not provide: Query Parameters(Add Parameter) . properties description:
  ...hidden...
5 params["sendHeaders"]: boolean = False: Send Headers. Whether the request has headers or not. You can't use expression.
6 params["specifyHeaders"]: enum[string] = "keypair", Activate(Not Required) when (sendHeaders in [True]), otherwise do not provide: Specify Headers . Available values:
  6.0 value=="keypair": Using Fields Below
  6.1 value=="json": Using JSON
7 params["headerParameters"]: dict[str,list[dict[str,any]]] = {'parameters': [{'name': '', 'value': ''}]}, Activate(Not Required) when (sendHeaders in [True] and specifyHeaders in ['keypair']), otherwise do not provide: Header Parameters(Add Parameter) . properties description:
  ...hidden...
8 params["sendBody"]: boolean = False: Send Body. Whether the request has a body or not. You can't use expression.
9 params["contentType"]: enum[string] = "json", Activate(Not Required) when (sendBody in [True]), otherwise do not provide: Body Content Type. Content-Type to use to send body parameters . Available values:
  9.0 value=="form-urlencoded": Form Urlencoded
  9.1 value=="multipart-form-data": Form-Data
  9.2 value=="json": JSON
  9.3 value=="binaryData": n8n Binary Data
  9.4 value=="raw": Raw
10 params["specifyBody"]: enum[string] = "keypair", Activate(Not Required) when (sendBody in [True] and contentType in ['form-urlencoded']), otherwise do not provide: Specify Body . Available values:
  10.0 value=="keypair": Using Fields Below
  10.1 value=="string": Using Single Field
11 params["bodyParameters"]: dict[str,list[dict[str,any]]] = {'parameters': [{'name': '', 'value': ''}]}, Activate(Not Required) when (sendBody in [True] and contentType in ['form-urlencoded'] and specifyBody in ['keypair']), otherwise do not provide: Body Parameters(Add Parameter) . properties description:
  ...hidden...
12 params["body"]: string = "", Activate(Not Required) when (sendBody in [True] and contentType in ['raw']), otherwise do not provide: Body()
13 params["inputDataFieldName"]: string = "", Activate(Not Required) when (sendBody in [True] and contentType in ['binaryData']), otherwise do not provide: Input Data Field Name. The name of the incoming field containing the binary file data to be processed. You can't use expression.
14 params["rawContentType"]: string = "", Activate(Not Required) when (sendBody in [True] and contentType in ['raw']), otherwise do not provide: Content Type(text/html)
15 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'status': 'ok', 'totalResults': 69, 'articles': [{'source': {'id': None, 'name': 'Kotaku'}, 'author': 'Zack Zwiezen', 'title': 'Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku', 'description': 'I mean, most of these doors look more like vulvas to me...', 'url': 'https://kotaku.com/metroid-prime-4-players-discovering-vagina-vulva-doors-2000651050', 'urlToImage': 'https://kotaku.com/app/uploads/2025/12/metroid-vaginaas-1200x675.jpg', 'publishedAt': '2025-12-05T22:44:18Z', 'content': 'Metroid Prime 4 Beyond is more mature than your average Nintendo-published first-party game. So players were expecting some violence, sci-fi monsters, and guns. What they might not have been expectin… [+2853 chars]'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Fetch 1 technology news headline from the US using NewsAPI with proper parameters and API key.
  TODOs: 
    - Test the action to verify news is fetched correctly.
    - Adjust parameters if needed based on test results.
  """
  params = { 'headerParameters': {'parameters': [{'name': 'X-Api-Key', 'value': '={{$credentials.httpHeaderAuth.value}}'}]},
             'method': 'GET',
             'queryParameters': { 'parameters': [ {'name': 'category', 'value': 'technology'},
                                                  {'name': 'country', 'value': 'us'},
                                                  {'name': 'pageSize', 'value': '1'}]},
             'sendBody': False,
             'sendHeaders': True,
             'sendQuery': True,
             'specifyHeaders': 'keypair',
             'specifyQuery': 'keypair',
             'url': 'https://newsapi.org/v2/top-headlines'}
  function = transparent_action(integration="httpRequest", resource="default", operation="default")
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
[{'json': {'text': 'Technology News: Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765075744.508219', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Technology News: Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'S36a1', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Technology News: Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku'}]}]}]}, 'message_timestamp': '1765075744.508219'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send the fetched news headline text to Slack channel #news, using the channel name and text parameter with expression.
  TODOs: 
    - Extract and format news headline text in mainWorkflow.
    - Test sending message to Slack.
    - Adjust channel or formatting if needed.
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
[{'json': {'ok': True, 'channel': 'C0A042T5ENT', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765075744.508219', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Technology News: Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'S36a1', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Technology News: Metroid Prime 4 Has A Lot Of Vaginal Doorways In It - Kotaku'}]}]}]}, 'message_timestamp': '1765075744.508219'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
  """
  comments: Connect manual trigger, fetch news from NewsAPI, and send the news headline to Slack channel #news.
  TODOs: 
    - Test the full workflow end-to-end.
    - Handle empty or missing news gracefully.
  """
  # Step 1: Call NewsAPI to get news
  news_output = action_0(trigger_input)

  # Step 2: Extract the first article's title
  if not news_output or not news_output[0]['json'].get('articles'):
    message_text = "No news found."
  else:
    articles = news_output[0]['json']['articles']
    if len(articles) == 0 or not articles[0].get('title'):
      message_text = "No news title found."
    else:
      message_text = f"Technology News: {articles[0]['title']}"

  # Step 3: Prepare Slack input
  slack_input = [{"json": {"text": message_text}}]

  # Step 4: Send message to Slack channel #news
  slack_output = action_1(slack_input)

  return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""