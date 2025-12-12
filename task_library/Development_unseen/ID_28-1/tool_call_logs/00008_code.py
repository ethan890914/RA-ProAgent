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
  comments: Manual trigger to start the workflow
  TODOs: 
    - Test the trigger
    - Ensure it activates mainWorkflow
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["searchMethod"]: enum[string] = "name": Search Method. Whether to search for the file/folder name or use a query string . Available values:
  0.0 value=="name": Search File/Folder Name
  0.1 value=="query": Advanced Search
1 params["queryString"]: string = "", Activate(Not Required) when (searchMethod in ['query']), otherwise do not provide: Query String. Use the Google query strings syntax to search for a specific set of files or folders. <a href="https://developers.google.com/drive/api/v3/search-files" target="_blank">Learn more</a>.(e.g. not name contains 'hello')
2 params["returnAll"]: boolean = False: Return All. Whether to return all results or only up to a given limit
3 params["limit"]: number = 50, Activate(Not Required) when (returnAll in [False]), otherwise do not provide: Limit. Max number of results to return
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
def action_0(input_data):
  """
  comments: Search for the file 'abc-news_chunked_1day_articles_2025-11-11_1.csv' in the specified folder by folderId using query
  TODOs: 
    - Test file search with folderId input
    - Verify query string correctness
  """
  params = { 'limit': 1,
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
def action_1(input_data):
  """
  comments: Download the file from Google Drive using fileId
  TODOs: 
    - Test file download
    - Check binary content extraction
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="googleDrive", resource="file", operation="download")
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_2(input_data):
  """
  comments: Send the line count message to Slack channel #news
  TODOs: 
    - Format message text
    - Test Slack message sending
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["searchMethod"]: enum[string] = "name": Search Method. Whether to search for the file/folder name or use a query string . Available values:
  0.0 value=="name": Search File/Folder Name
  0.1 value=="query": Advanced Search
1 params["queryString"]: string = "", Activate(Not Required) when (searchMethod in ['query']), otherwise do not provide: Query String. Use the Google query strings syntax to search for a specific set of files or folders. <a href="https://developers.google.com/drive/api/v3/search-files" target="_blank">Learn more</a>.(e.g. not name contains 'hello')
2 params["returnAll"]: boolean = False: Return All. Whether to return all results or only up to a given limit
3 params["limit"]: number = 50, Activate(Not Required) when (returnAll in [False]), otherwise do not provide: Limit. Max number of results to return
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
def action_3(input_data):
  """
  comments: Search for folder named 'ProAgentWorkspace' using googleDrive fileFolder search to get folderId
  TODOs: 
    - Implement search query with folder name
    - Test folder search
  """
  params = {'limit': 1, 'queryString': '', 'returnAll': False, 'searchMethod': 'name'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
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
    comments: Workflow to download a file from Google Drive, count lines, and send message to Slack
    TODOs:
      - Implement folder search function later
      - Test full workflow
    """
    import base64

    # For now, simulate folderId input (since folder search not defined)
    # Expect trigger_input to have folderId in json
    folder_id = None
    if len(trigger_input) > 0 and 'folderId' in trigger_input[0]['json']:
        folder_id = trigger_input[0]['json']['folderId']
    else:
        # For testing, provide a dummy folderId or raise error
        raise ValueError("folderId not provided in trigger input")

    # Prepare input for file search
    file_search_input = [{"json": {"folderId": folder_id}}]

    # Search for the file
    file_search_output = action_0(file_search_input)
    if len(file_search_output) == 0:
        raise ValueError("File not found in folder")

    file_id = file_search_output[0]['json'].get('id')
    if not file_id:
        raise ValueError("File id not found in search output")

    # Prepare input for download action
    download_input = file_search_output  # file_search_output contains id field

    # Download the file
    download_output = action_1(download_input)
    if len(download_output) == 0:
        raise ValueError("Download output empty")

    # Extract base64 content
    base64_content = download_output[0].get('binary', {}).get('data', {}).get('data')
    if not base64_content:
        raise ValueError("No binary data found in download output")

    # Decode base64
    file_bytes = base64.b64decode(base64_content)
    file_text = file_bytes.decode('utf-8')

    # Count lines
    line_count = len(file_text.splitlines())

    # Format message
    file_name = 'abc-news_chunked_1day_articles_2025-11-11_1.csv'
    message_text = f"File: {file_name} | Line count: {line_count}"

    # Prepare input for Slack
    slack_input = [{"json": {"text": message_text}}]

    # Send message
    slack_output = action_2(slack_input)

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
            # For testing, provide a dummy folderId or raise error
-->         raise ValueError("folderId not provided in trigger input")
------------------------
ValueError: folderId not provided in trigger input

You can also see the runnning result for all functions in there comments.
"""