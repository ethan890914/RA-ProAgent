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
  comments: Trigger the workflow manually to start the process.
  TODOs: 
    - Test the manual trigger.
    - Verify it activates the main workflow.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["searchMethod"]: enum[string] = "name": Search Method. Whether to search for the file/folder name or use a query string . Available values:
  0.0 value=="name": Search File/Folder Name
  0.1 value=="query": Advanced Search
1 params["queryString"]: string = "": Query String. Use the Google query strings syntax to search for a specific set of files or folders. <a href="https://developers.google.com/drive/api/v3/search-files" target="_blank">Learn more</a>.(e.g. not name contains 'hello')
2 params["returnAll"]: boolean = False: Return All. Whether to return all results or only up to a given limit
3 params["limit"]: number = 50: Limit. Max number of results to return
4 params["filter"]: dict = {}: Filter(Add Filter) . properties description:
  ...hidden...
5 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Search the folder named 'ProAgentWorkspace/newsapi_data/2025-11-11' in Google Drive by folder name.
  TODOs: 
    - Test folder search action with these parameters.
    - Verify the output contains the folder ID needed for next step.
  """
  params = { 'filter': {},
             'limit': 1,
             'options': {},
             'queryString': 'ProAgentWorkspace/newsapi_data/2025-11-11',
             'returnAll': False,
             'searchMethod': 'name'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["searchMethod"]: enum[string] = "name": Search Method. Whether to search for the file/folder name or use a query string . Available values:
  0.0 value=="name": Search File/Folder Name
  0.1 value=="query": Advanced Search
1 params["queryString"]: string = "": Query String. Use the Google query strings syntax to search for a specific set of files or folders. <a href="https://developers.google.com/drive/api/v3/search-files" target="_blank">Learn more</a>.(e.g. not name contains 'hello')
2 params["returnAll"]: boolean = False: Return All. Whether to return all results or only up to a given limit
3 params["limit"]: number = 50: Limit. Max number of results to return
4 params["filter"]: dict = {}: Filter(Add Filter) . properties description:
  ...hidden...
5 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Search the file 'abc-news_chunked_1day_articles_2025-11-11_1.csv' inside the folder found by folderId.
  TODOs: 
    - Test file search action with correct input_data containing folderId.
    - Verify output contains file ID for download.
  """
  params = { 'filter': {},
             'limit': 1,
             'options': {},
             'queryString': '=name = \'abc-news_chunked_1day_articles_2025-11-11_1.csv\' and \'{{$json["folderId"]}}\' in parents '
                            'and trashed = false',
             'returnAll': False,
             'searchMethod': 'query'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["fileId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: File. The file to download . "mode" should be one of ['url', 'id']: 
  0.0 params["fileId"]["value"](when "mode"="url"): string: Link(e.g. https://drive.google.com/file/d/1anGBg0b5re2VtF2bKu201_a-Vnz5BHq9Y4r-yBDAj5A/edit)
  0.1 params["fileId"]["value"](when "mode"="id"): string: ID(e.g. 1anGBg0b5re2VtF2bKu201_a-Vnz5BHq9Y4r-yBDAj5A)
1 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Download the file using file ID from file search result, extracting fileId from input data's json id field.
  TODOs: 
    - Test the download action and verify the binary content.
    - Decode Base64 content in workflow to get the file text.
  """
  params = {'fileId': {'mode': 'id', 'value': '={{$json["id"]}}'}, 'options': {}}
  function = transparent_action(integration="googleDrive", resource="file", operation="download")
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_3(input_data: List[Dict] =  [{...}]):
  """
  comments: Send a simple text message to Slack channel #news with the message text from input data.
  TODOs: 
    - Test Slack message sending.
    - Verify message content and channel.
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
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to download a specific file from Google Drive and send its schema to Slack channel #news.
    TODOs:
      - Test the full workflow end-to-end.
      - Handle empty search results gracefully.
      - Verify message formatting and Slack delivery.
    """
    # Step 1: Trigger input is empty json, start folder search with query method
    folder_search_input = trigger_input
    folder_search_params = { 'filter': {},
                             'limit': 1,
                             'options': {},
                             'queryString': "=name = '2025-11-11' and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
                             'returnAll': False,
                             'searchMethod': 'query'}
    folder_search_function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
    folder_search_output = folder_search_function.run(input_data=folder_search_input, params=folder_search_params)
    
    # Check if folder found
    if not folder_search_output or len(folder_search_output) == 0:
        return [{"json": {"error": "Folder not found."}}]
    
    folder_id = folder_search_output[0]["json"].get("id")
    if not folder_id:
        return [{"json": {"error": "Folder ID missing in folder search output."}}]
    
    # Step 2: Search file inside the folder
    file_search_input = [{"json": {"folderId": folder_id}}]
    file_search_output = action_1(file_search_input)
    
    if not file_search_output or len(file_search_output) == 0:
        return [{"json": {"error": "File not found in folder."}}]
    
    file_id = file_search_output[0]["json"].get("id")
    file_name = file_search_output[0]["json"].get("name", "")
    if not file_id:
        return [{"json": {"error": "File ID missing in file search output."}}]
    
    # Step 3: Download file
    file_download_input = file_search_output
    file_download_output = action_2(file_download_input)
    
    if not file_download_output or len(file_download_output) == 0:
        return [{"json": {"error": "File download failed or returned empty."}}]
    
    # Step 4: Extract and decode Base64 content
    base64_content = file_download_output[0].get('binary', {}).get('data', {}).get('data')
    if not base64_content:
        return [{"json": {"error": "No binary content found in downloaded file."}}]
    import base64
    file_bytes = base64.b64decode(base64_content)
    file_text = file_bytes.decode('utf-8')
    
    # Step 5: Extract the first line as schema
    first_line = file_text.splitlines()[0] if file_text else ""
    
    # Step 6: Format message for Slack
    message_text = f"{file_name} schema:\n{first_line}"
    slack_input = [{"json": {"text": message_text, "channelId": {"mode": "name", "value": "news"}}}]
    
    # Step 7: Send message to Slack
    slack_output = action_3(slack_input)
    
    return slack_output




"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[]`
the output data of function `action_1` is: `[]`
the output data of function `action_2` is: `[]`
the output data of function `action_3` is: `[]`

------------------------
In Function: mainWorkflow
                                 'searchMethod': 'query'}
-->     folder_search_function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
        folder_search_output = folder_search_function.run(input_data=folder_search_input, params=folder_search_params)
------------------------
NameError: name 'transparent_action' is not defined

You can also see the runnning result for all functions in there comments.
"""