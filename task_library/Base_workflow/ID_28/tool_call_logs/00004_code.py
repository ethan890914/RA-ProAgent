"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: Trigger the workflow manually
  TODOs: 
    - Test the manual trigger
    - Use it as the main workflow trigger
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}, 'pairedItem': {'item': 0}}]

3.Output:
[{'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Search for the folder 'ProAgentWorkspace' by name using query string in Google Drive
  TODOs: 
    - Test folder search result with query string
    - Handle multiple results if needed
  """
  params = { 'limit': 1,
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'folderId': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe'}}]

3.Output:
[{'json': {'id': '1-ZdMcy9RHenVKWkzmXGVqf7TOumVQ_Km', 'name': 'abc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Search for the file 'abc-news_chunked_1day_articles_2025-11-11_1.csv' inside the folder 'ProAgentWorkspace' by folderId using query string in Google Drive
  TODOs: 
    - Test file search result
    - Verify folderId is correctly passed
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

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'id': '1-ZdMcy9RHenVKWkzmXGVqf7TOumVQ_Km', 'name': 'abc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}]

3.Output:
[]
"""
def action_2(input_data):
  """
  comments: Download the file from Google Drive using fileId
  TODOs: 
    - Test file download
    - Extract binary data
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
  comments: Send the extracted schema text to Slack channel #news
  TODOs: 
    - Format message text
    - Test Slack message sending
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedInner
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
  """
  comments: Workflow to download a specific file from Google Drive, extract its schema, and send to Slack #news channel
  TODOs: 
    - Test end-to-end workflow
    - Handle empty search results gracefully
  """
  # Step 1: Trigger manual
  manual_output = trigger_0(trigger_input)

  # Step 2: Search folder
  folder_output = action_0(manual_output)
  if not folder_output or len(folder_output) == 0:
    raise Exception("Folder 'ProAgentWorkspace' not found")

  folder_id = folder_output[0]['json']['id']

  # Step 3: Search file inside folder
  file_search_input = [{"json": {"folderId": folder_id}}]
  file_output = action_1(file_search_input)
  if not file_output or len(file_output) == 0:
    raise Exception("File 'abc-news_chunked_1day_articles_2025-11-11_1.csv' not found")

  file_id = file_output[0]['json']['id']

  # Step 4: Download file
  download_input = file_output  # pass directly because params use {{$json["id"]}}
  download_output = action_2(download_input)
  if not download_output or len(download_output) == 0:
    raise Exception("Failed to download file")

  # Step 5: Extract and decode Base64 content
  base64_content = download_output[0].get('binary', {}).get('data', {}).get('data')
  if not base64_content:
    raise Exception("No binary content found in downloaded file")

  import base64
  file_bytes = base64.b64decode(base64_content)
  file_text = file_bytes.decode('utf-8')

  # Step 6: Extract first line as schema
  first_line = file_text.splitlines()[0] if file_text else ""

  # Step 7: Format message
  filename = 'abc-news_chunked_1day_articles_2025-11-11_1.csv'
  message_text = f"{filename} schema:\n{first_line}"

  # Step 8: Send to Slack
  slack_input = [{"json": {"text": message_text}}]
  slack_output = action_3(slack_input)

  return slack_output



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}, 'pairedItem': {'item': 0}}]`
the output data of function `action_0` is: `[{'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[{'json': {'id': '1-ZdMcy9RHenVKWkzmXGVqf7TOumVQ_Km', 'name': 'abc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_2` is: `[]`
the output data of function `action_3` is: `[]`

------------------------
In Function: mainWorkflow
      download_input = file_output  # pass directly because params use {{$json["id"]}}
-->   download_output = action_2(download_input)
      if not download_output or len(download_output) == 0:
------------------------
In Function: transparent_action
      function = transparent_action(integration="googleDrive", resource="file", operation="download")
-->   output_data = function.run(input_data=input_data, params=params)
      return output_data
------------------------
n8nRunningException: Execution Failed: 
Output: Problem with execution 2424: The workflow has issues and cannot be executed for that reason. Please fix them first.. Aborting.
The workflow has issues and cannot be executed for that reason. Please fix them first. (execution 2424)
Error executing workflow. See log messages for details.

Execution error:
====================================
The workflow has issues and cannot be executed for that reason. Please fix them first.
undefined
WorkflowHasIssuesError: The workflow has issues and cannot be executed for that reason. Please fix them first.
    at WorkflowExecute.checkForWorkflowIssues (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1382:10)
    at WorkflowExecute.processRunExecutionData (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1461:8)
    at WorkflowExecute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:176:15)
    at ManualExecutionService.runManually (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/manual-execution.service.ts:157:27)
    at WorkflowRunner.runMainProcess (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:298:53)
    at WorkflowRunner.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:175:4)
    at Execute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/commands/execute.ts:95:23)
    at CommandRegistry.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/command-registry.ts:67:4)
    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/bin/n8n:63:2
The workflow has issues and cannot be executed for that reason. Please fix them first.


You can also see the runnning result for all functions in there comments.
"""