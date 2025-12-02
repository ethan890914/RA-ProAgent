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
  comments: Trigger the workflow manually by user action.
  TODOs: 
    - Implement the trigger to activate the workflow.
    - Test the manual trigger.
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Search for the folder named 'ProAgentWorkspace' in Google Drive.
  TODOs: 
    - Test the search results to confirm the folder is found.
    - If folder ID is found, next step is to list files inside that folder.
  """
  params = { 'filter': {},
             'limit': 50,
             'options': {},
             'queryString': "name='ProAgentWorkspace' and mimeType='application/vnd.google-apps.folder'",
             'returnAll': True,
             'searchMethod': 'query'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'text': 'Files in ProAgentWorkspace:\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- 00005_code.py (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)\n'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764651906.324619', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Files in ProAgentWorkspace:\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- 00005_code.py (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)\n', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '1cI', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Files in ProAgentWorkspace:\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- 00005_code.py (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)'}]}]}]}, 'message_timestamp': '1764651906.324619'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Send a message to Slack channel #general with the given text content.
  TODOs: 
    - Test Slack message sending with dynamic text.
    - Verify message formatting in Slack channel.
  """
  params = { 'channelId': {'mode': 'name', 'value': 'general'},
             'messageType': 'text',
             'otherOptions': {},
             'select': 'channel',
             'text': '={{$json["text"]}}'}
  function = transparent_action(integration="slack", resource="message", operation="post")
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'queryString': "'1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe' in parents and trashed=false"}}]

3.Output:
[{'json': {'id': '1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD', 'name': 'Copy of 00005_code.py'}, 'pairedItem': {'item': 0}}, {'json': {'id': '16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi', 'name': '00005_code.py'}, 'pairedItem': {'item': 0}}]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Search files inside a folder by folder ID query string in Google Drive.
  TODOs: 
    - Test the search with folder ID query string.
    - Integrate action_2 in mainWorkflow.
    - Verify the file list returned is correct.
  """
  params = { 'filter': {},
             'limit': 100,
             'options': {},
             'queryString': '={{$json["queryString"]}}',
             'returnAll': True,
             'searchMethod': 'query'}
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764651906.324619', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Files in ProAgentWorkspace:\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- 00005_code.py (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)\n', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '1cI', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Files in ProAgentWorkspace:\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- 00005_code.py (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)'}]}]}]}, 'message_timestamp': '1764651906.324619'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered manually, lists all files in the 'ProAgentWorkspace' folder in Google Drive, and sends the file list to Slack #general channel.
    TODOs:
      - Use action_2 for file search inside folder.
      - Format message for Slack.
      - Handle empty folder or folder not found cases.
    """
    # Step 1: Manual trigger input
    # Step 2: Search for folder named 'ProAgentWorkspace'
    folder_search_results = action_0(trigger_input)
    if not folder_search_results or len(folder_search_results) == 0:
        # Folder not found, send message to Slack
        slack_message = [{"json": {"text": "Folder 'ProAgentWorkspace' not found in Google Drive."}}]
        slack_response = action_1(slack_message)
        return slack_response
    
    # Extract folder ID from first found folder
    folder_id = folder_search_results[0]["json"].get("id")
    if not folder_id:
        slack_message = [{"json": {"text": "Folder 'ProAgentWorkspace' found but no ID available."}}]
        slack_response = action_1(slack_message)
        return slack_response

    # Step 3: Prepare input for action_2 with query string
    query_files = f"'{folder_id}' in parents and trashed=false"
    action_2_input = [{"json": {"queryString": query_files}}]

    # Step 4: Search files inside the folder by folder ID using action_2
    files_search_results = action_2(action_2_input)

    # Step 5: Format the file list message
    if not files_search_results or len(files_search_results) == 0:
        message_text = "No files found in 'ProAgentWorkspace' folder."
    else:
        message_text = "Files in ProAgentWorkspace:\n"
        for file_item in files_search_results:
            file_json = file_item.get("json", {})
            file_name = file_json.get("name", "Unnamed")
            file_id = file_json.get("id", "No ID")
            message_text += f"- {file_name} (ID: {file_id})\n"

    # Step 6: Send the message to Slack
    slack_message = [{"json": {"text": message_text}}]
    slack_response = action_1(slack_message)

    return slack_response




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""