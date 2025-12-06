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
    - Test the manual trigger activation.
    - Ensure it outputs the correct trigger input format.
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
[{'json': {}}]

3.Output:
[{'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Search for the folder named 'ProAgentWorkspace' in Google Drive using fileFolder search with searchMethod 'query' and proper queryString.
  TODOs: 
    - Test folder search and verify folder ID output
    - Use folder ID to search files in next step
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
def action_1(input_data):
  """
  comments: Send a formatted message to Slack channel #general with the list of files' names and IDs.
  TODOs: 
    - Format the message text properly.
    - Test sending the message to Slack channel #general.
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
def mainWorkflow(trigger_input):
    """
    comments: Main workflow triggered by manual trigger, lists files in 'ProAgentWorkspace' folder and sends the list to Slack #general.
    TODOs:
      - Handle empty folder search results gracefully.
      - Format file list message correctly.
      - Test end-to-end workflow.
    """
    # Step 1: Trigger manual trigger (though trigger_input is already from trigger)
    # We use trigger_input directly

    # Step 2: Search for the folder 'ProAgentWorkspace'
    folder_search_output = action_0(trigger_input)

    if not folder_search_output or len(folder_search_output) == 0:
        # No folder found
        message = "Folder 'ProAgentWorkspace' not found in Google Drive."
        slack_input = [{"json": {"text": message}}]
        slack_output = action_1(slack_input)
        return slack_output

    folder_item = folder_search_output[0]['json']
    folder_id = folder_item.get('id')

    if not folder_id:
        message = "Folder ID for 'ProAgentWorkspace' not found."
        slack_input = [{"json": {"text": message}}]
        slack_output = action_1(slack_input)
        return slack_output

    # Step 3: Search for files inside the folder
    file_search_input = [{"json": {"folderId": folder_id}}]
    files_output = action_2(file_search_input)

    # Step 4: Format the list of files
    if not files_output or len(files_output) == 0:
        message = "No files found in folder 'ProAgentWorkspace'."
        slack_input = [{"json": {"text": message}}]
        slack_output = action_1(slack_input)
        return slack_output

    file_lines = []
    for file_item in files_output:
        file_json = file_item['json']
        file_name = file_json.get('name', 'Unknown')
        file_id = file_json.get('id', 'Unknown')
        file_lines.append(f"- {file_name} (ID: {file_id})")

    message_text = "Files in ProAgentWorkspace:\n" + "\n".join(file_lines)

    slack_input = [{"json": {"text": message_text}}]

    # Step 5: Send to Slack
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[{'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[]`

------------------------
In Function: mainWorkflow
        file_search_input = [{"json": {"folderId": folder_id}}]
-->     files_output = action_2(file_search_input)
------------------------
NameError: name 'action_2' is not defined

You can also see the runnning result for all functions in there comments.
"""