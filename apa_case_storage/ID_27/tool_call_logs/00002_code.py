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
    - Test manual trigger
    - Ensure it activates the workflow
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
  comments: Search for folder 'ProAgentWorkspace' in Google Drive using query string to find folder by name and mimeType
  TODOs: 
    - Test folder search action
    - Verify folder ID is returned
  """
  params = { 'filter': {},
             'limit': 1,
             'options': {},
             'queryString': "=name = 'ProAgentWorkspace' and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
             'returnAll': False,
             'searchMethod': 'query'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
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
def action_1(input_data):
  """
  comments: Search for file '00005_code.txt' in the specified folder
  TODOs: 
    - Implement file search with folderId and file name
    - Test file search action
  """
  params = {}  # to be Implemented
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
def action_2(input_data):
  """
  comments: Download file from Google Drive by fileId
  TODOs: 
    - Implement file download
    - Test file download and base64 content extraction
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
def action_3(input_data):
  """
  comments: Send the file content to Slack channel #general
  TODOs: 
    - Implement Slack message post
    - Test message format and delivery
  """
  params = {}  # to be Implemented
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
  comments: You need to give comments when implementing mainWorkflow
  TODOs: 
    - first define some actions
    - define a trigger
    - then implement this
  """
  print("Please call Workflow-implement first")
  raise NotImplementedError




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
      print("Please call Workflow-implement first")
-->   raise NotImplementedError
------------------------
NotImplementedError: 

You can also see the runnning result for all functions in there comments.
"""