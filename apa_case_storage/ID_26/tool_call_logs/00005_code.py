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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'text': 'Files in ProAgentWorkspace:\n- Introduction to LLM based Generative AI System - Project Presentation Schedule - Fall25 (ID: 12KJllj2CeReG1XvSUiNiOrvZKQxteL5ifug2e0apRrM)\n- Introduction to LLM based Generative AI System - Project Sign Up - Fall25 (ID: 1QrGRMGVuyLdT-1mZ-ydHLoUs2Jkm3Vbar-rzW6qDS98)\n- rpa_test_cc9008 (ID: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c)\n- GPU Project - Group 5 (ID: 1aD_TYm-NXKXqxeQsyejc42FurzOuUeKIrCVaBAm7Gkk)\n- GPU Report (ID: 198SYvt3ltaJpr5IRm8E2qAKHljtjblBqhRMW2ut1-6g)\n- 2025-11-11 (ID: 1xGC2oIIu_p_Vo1a7Y7U8PUoHV7URjw4X)\n- 2025-11-30 (ID: 1O6j-xFKeca_I7Jod92rgBP1qzCAzfsfQ)\n- newsapi_data (ID: 1iR2QEEY02kcCpTN0VGO8qk-VinGgHOQw)\n- 00005_code.txt (ID: 16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi)\n- Copy of 00005_code.py (ID: 1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD)\n- ProAgentWorkspace (ID: 1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe)\n- NYU template (ID: 1cJOo4sGi0yEt_WpwFoleQmrEegBe4J-7dgvsrHtUtew)\n- Copy of [VIEW ONLY] International Student Welcome to NYU Meeting-Fall, 2024 (ID: 1WvhgkGVxdkjB5l9kYiV31V0Qz6FBW92asA41arroRHU)\n- bloomberg_chunked_1day_articles_2025-11-30_1.csv (ID: 1z2r_s5Rr4SE3U2mbj2p9NmgopSAzhyZR)\n- bbc-news_chunked_1day_articles_2025-11-30_1.csv (ID: 1qNZWWf2hoOw0CRnQRBfBBzhX_PLYojSI)\n- wired_chunked_1day_articles_2025-11-30_1.csv (ID: 1dMocj8Cg1aen467_ajfqEFgqF1faIC2U)\n- the-times-of-india_chunked_1day_articles_2025-11-30_1.csv (ID: 1weOEU8oAMLZuiUdGPHngiKZKS6SUN3ja)\n- nbc-news_chunked_1day_articles_2025-11-30_1.csv (ID: 1HEGjSksg8W2VdonP61zZliLzvhoxpG59)\n- espn_chunked_1day_articles_2025-11-30_1.csv (ID: 1fEWblM93AxXucsV8qzX004DuGykByoPK)\n- fox-news_chunked_1day_articles_2025-11-30_1.csv (ID: 19ws59ubv-qc2KBjJWCLIwvtGbyn6LLSb)\n- usa-today_chunked_1day_articles_2025-11-30_1.csv (ID: 1VpiepvGBUdni8qE9AljbDEQIJ63JhyRJ)\n- fortune_chunked_1day_articles_2025-11-30_1.csv (ID: 18zLJY_XSO4Dwyb7KxiH9LGjazoPbpGVf)\n- the-verge_chunked_1day_articles_2025-11-30_1.csv (ID: 1j1LaLG1G9DoYbsQSKieRXpZNWuwBgaQe)\n- associated-press_chunked_1day_articles_2025-11-30_1.csv (ID: 1i3xOPGOty9Qm-O9DyFw1YR4mTrBagYIW)\n- cbs-news_chunked_1day_articles_2025-11-30_1.csv (ID: 1pHJbupDQWfBwWCYvXXQNdLviGhRTYLVS)\n- business-insider_chunked_1day_articles_2025-11-30_1.csv (ID: 1om50okrZiCIgxpo2jqYsuW3_QBsgGKbp)\n- abc-news_chunked_1day_articles_2025-11-30_1.csv (ID: 1QFwwSPm4x_a6J6cIZ5sOxjAdksEaAtnw)\n- techcrunch_chunked_1day_articles_2025-11-30_1.csv (ID: 115cE6S3iVhjX2hCkIkpjEph-3Qvpz4vr)\n- bloomberg_chunked_1day_articles_2025-11-11_1.csv (ID: 1SIvQuTPAlrKdpnuirQwG4NFDqtD10jv7)\n- the-washington-post_chunked_1day_articles_2025-11-11_1.csv (ID: 1hLWQfQFP8xidnugSTMnNuoEu_ah5aH7q)\n- bbc-news_chunked_1day_articles_2025-11-11_1.csv (ID: 1pdHEqHlfDvDwq3sVd8XHzrcbc5VlQFKY)\n- wired_chunked_1day_articles_2025-11-11_1.csv (ID: 1_3Nc8O1sLRo9_kAWHp_ajLUCJmOCqCgP)\n- the-times-of-india_chunked_1day_articles_2025-11-11_1.csv (ID: 1AGnQvBdrD5TeQh5x9q7Jkn6sBnmKCQ2y)\n- nbc-news_chunked_1day_articles_2025-11-11_1.csv (ID: 1oCW1O52icwQermuPxeBFPwPG1ZeeuCFZ)\n- espn_chunked_1day_articles_2025-11-11_1.csv (ID: 19r3NdV_3iXzYxYmbrd1UBgH_V-_OUvH3)\n- fox-news_chunked_1day_articles_2025-11-11_1.csv (ID: 1sXbL5czckK6UCJsAAlrSs6i1M_wNDssL)\n- usa-today_chunked_1day_articles_2025-11-11_1.csv (ID: 1iw2v_1LPfQCdxcyWpERUuOsMAKUuMlEj)\n- fortune_chunked_1day_articles_2025-11-11_1.csv (ID: 1Zzcxq0-1HiIvD0zKagWm83sy0_wV4qPp)\n- the-verge_chunked_1day_articles_2025-11-11_1.csv (ID: 1GYnKJmOUVHutoiURsDL5hnnSBaWAS_vF)\n- associated-press_chunked_1day_articles_2025-11-11_1.csv (ID: 1cKNVfHx8SkpYsVYiDSsXmfw9_aNE_g6Y)\n- cbs-news_chunked_1day_articles_2025-11-11_1.csv (ID: 1mIOWcF8JuDgH0dPARm_vXtJCyZ-MpJi8)\n- business-insider_chunked_1day_articles_2025-11-11_1.csv (ID: 19qHtMuphsqh-T07p1bSZcupxbThiIODR)\n- abc-news_chunked_1day_articles_2025-11-11_1.csv (ID: 1nVro3aesPbxKj0-lQZHjBVal5v-mA8h2)\n- techcrunch_chunked_1day_articles_2025-11-11_1.csv (ID: 1vk6sLlqGWR4KoAGA2bIE36prWEFAGxGu)\n- Midpoint project checkpoint (ID: 1XN5Hal5lPQzCaFfn9umi99NVShpOtEVlPv0vswUpPHU)\n- 截圖 2025-11-19 晚上10.16.30.png (ID: 1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS)\n- MSCS Program Options effective Fall 2024 (ID: 1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I)\n- BDAD Data Ingestion (ID: 1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA)\n- gpu_kernel_time_predictor.ipynb (ID: 1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7)'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764936308.276949', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '- 截圖 2025-11-19 晚上10.16.30.png (ID: 1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS)\n- MSCS Program Options effective Fall 2024 (ID: 1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I)\n- BDAD Data Ingestion (ID: 1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA)\n- gpu_kernel_time_predictor.ipynb (ID: 1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7)', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '4ew3V', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '- 截圖 2025-11-19 晚上10.16.30.png (ID: 1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS)\n- MSCS Program Options effective Fall 2024 (ID: 1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I)\n- BDAD Data Ingestion (ID: 1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA)\n- gpu_kernel_time_predictor.ipynb (ID: 1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7)'}]}]}]}, 'message_timestamp': '1764936308.276949'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send a formatted message to Slack channel #general with the list of files' names and IDs.
  TODOs: 
    - Test sending message to Slack #general channel
    - Verify message format and delivery
  """
  params = { 'channelId': {'mode': 'name', 'value': 'general'},
             'messageType': 'text',
             'select': 'channel',
             'text': '={{$json["text"]}}'}
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'folderId': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe'}}]

3.Output:
[{'json': {'id': '12KJllj2CeReG1XvSUiNiOrvZKQxteL5ifug2e0apRrM', 'name': 'Introduction to LLM based Generative AI System - Project Presentation Schedule - Fall25'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1QrGRMGVuyLdT-1mZ-ydHLoUs2Jkm3Vbar-rzW6qDS98', 'name': 'Introduction to LLM based Generative AI System - Project Sign Up - Fall25'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c', 'name': 'rpa_test_cc9008'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1aD_TYm-NXKXqxeQsyejc42FurzOuUeKIrCVaBAm7Gkk', 'name': 'GPU Project - Group 5'}, 'pairedItem': {'item': 0}}, {'json': {'id': '198SYvt3ltaJpr5IRm8E2qAKHljtjblBqhRMW2ut1-6g', 'name': 'GPU Report'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1xGC2oIIu_p_Vo1a7Y7U8PUoHV7URjw4X', 'name': '2025-11-11'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1O6j-xFKeca_I7Jod92rgBP1qzCAzfsfQ', 'name': '2025-11-30'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1iR2QEEY02kcCpTN0VGO8qk-VinGgHOQw', 'name': 'newsapi_data'}, 'pairedItem': {'item': 0}}, {'json': {'id': '16x4yKtd7fHeRe-b9a-RtBzI1XLxM2LQi', 'name': '00005_code.txt'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1dcrCCwVRMIIOID_5VVTkQZx-ffRBHPdD', 'name': 'Copy of 00005_code.py'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1Y27C7b4gHe4gLmlcD8rJhFDObez0U4Pe', 'name': 'ProAgentWorkspace'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1cJOo4sGi0yEt_WpwFoleQmrEegBe4J-7dgvsrHtUtew', 'name': 'NYU template'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1WvhgkGVxdkjB5l9kYiV31V0Qz6FBW92asA41arroRHU', 'name': 'Copy of [VIEW ONLY] International Student Welcome to NYU Meeting-Fall, 2024'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1z2r_s5Rr4SE3U2mbj2p9NmgopSAzhyZR', 'name': 'bloomberg_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1qNZWWf2hoOw0CRnQRBfBBzhX_PLYojSI', 'name': 'bbc-news_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1dMocj8Cg1aen467_ajfqEFgqF1faIC2U', 'name': 'wired_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1weOEU8oAMLZuiUdGPHngiKZKS6SUN3ja', 'name': 'the-times-of-india_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1HEGjSksg8W2VdonP61zZliLzvhoxpG59', 'name': 'nbc-news_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1fEWblM93AxXucsV8qzX004DuGykByoPK', 'name': 'espn_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '19ws59ubv-qc2KBjJWCLIwvtGbyn6LLSb', 'name': 'fox-news_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1VpiepvGBUdni8qE9AljbDEQIJ63JhyRJ', 'name': 'usa-today_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '18zLJY_XSO4Dwyb7KxiH9LGjazoPbpGVf', 'name': 'fortune_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1j1LaLG1G9DoYbsQSKieRXpZNWuwBgaQe', 'name': 'the-verge_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1i3xOPGOty9Qm-O9DyFw1YR4mTrBagYIW', 'name': 'associated-press_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1pHJbupDQWfBwWCYvXXQNdLviGhRTYLVS', 'name': 'cbs-news_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1om50okrZiCIgxpo2jqYsuW3_QBsgGKbp', 'name': 'business-insider_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1QFwwSPm4x_a6J6cIZ5sOxjAdksEaAtnw', 'name': 'abc-news_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '115cE6S3iVhjX2hCkIkpjEph-3Qvpz4vr', 'name': 'techcrunch_chunked_1day_articles_2025-11-30_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1SIvQuTPAlrKdpnuirQwG4NFDqtD10jv7', 'name': 'bloomberg_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1hLWQfQFP8xidnugSTMnNuoEu_ah5aH7q', 'name': 'the-washington-post_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1pdHEqHlfDvDwq3sVd8XHzrcbc5VlQFKY', 'name': 'bbc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1_3Nc8O1sLRo9_kAWHp_ajLUCJmOCqCgP', 'name': 'wired_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1AGnQvBdrD5TeQh5x9q7Jkn6sBnmKCQ2y', 'name': 'the-times-of-india_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1oCW1O52icwQermuPxeBFPwPG1ZeeuCFZ', 'name': 'nbc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '19r3NdV_3iXzYxYmbrd1UBgH_V-_OUvH3', 'name': 'espn_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1sXbL5czckK6UCJsAAlrSs6i1M_wNDssL', 'name': 'fox-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1iw2v_1LPfQCdxcyWpERUuOsMAKUuMlEj', 'name': 'usa-today_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1Zzcxq0-1HiIvD0zKagWm83sy0_wV4qPp', 'name': 'fortune_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1GYnKJmOUVHutoiURsDL5hnnSBaWAS_vF', 'name': 'the-verge_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1cKNVfHx8SkpYsVYiDSsXmfw9_aNE_g6Y', 'name': 'associated-press_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1mIOWcF8JuDgH0dPARm_vXtJCyZ-MpJi8', 'name': 'cbs-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '19qHtMuphsqh-T07p1bSZcupxbThiIODR', 'name': 'business-insider_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1nVro3aesPbxKj0-lQZHjBVal5v-mA8h2', 'name': 'abc-news_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1vk6sLlqGWR4KoAGA2bIE36prWEFAGxGu', 'name': 'techcrunch_chunked_1day_articles_2025-11-11_1.csv'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1XN5Hal5lPQzCaFfn9umi99NVShpOtEVlPv0vswUpPHU', 'name': 'Midpoint project checkpoint'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS', 'name': '截圖 2025-11-19 晚上10.16.30.png'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I', 'name': 'MSCS Program Options effective Fall 2024'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA', 'name': 'BDAD Data Ingestion'}, 'pairedItem': {'item': 0}}, {'json': {'id': '1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7', 'name': 'gpu_kernel_time_predictor.ipynb'}, 'pairedItem': {'item': 0}}]
"""
def action_2(input_data):
  """
  comments: Search for all files inside the folder with the given folder ID using query string.
  TODOs: 
    - Set searchMethod to 'query'.
    - Use queryString to search for files where 'folderId' is in parents.
    - Test the file search and verify output.
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="googleDrive", resource="fileFolder", operation="search")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764936308.276949', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '- 截圖 2025-11-19 晚上10.16.30.png (ID: 1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS)\n- MSCS Program Options effective Fall 2024 (ID: 1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I)\n- BDAD Data Ingestion (ID: 1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA)\n- gpu_kernel_time_predictor.ipynb (ID: 1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7)', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '4ew3V', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '- 截圖 2025-11-19 晚上10.16.30.png (ID: 1e7sMOtniv8DMIBxMZtjc4FuyBSpYEIoS)\n- MSCS Program Options effective Fall 2024 (ID: 1bazfO0tvkK09I73tW2tI36J1BvjswX3bBu-6bQBgJ6I)\n- BDAD Data Ingestion (ID: 1B3WBTpbZQwNgf5y7tpuamgdYPeTxt06vhhTYQOWRZSA)\n- gpu_kernel_time_predictor.ipynb (ID: 1FxHL2-dmTZ4HeAwtNtJ508Jt6U0oNx-7)'}]}]}]}, 'message_timestamp': '1764936308.276949'}, 'pairedItem': {'item': 0}}]
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




You can also see the runnning result for all functions in there comments.
"""