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
  comments: Manual trigger to start the workflow when clicked.
  TODOs: 
    - Test manual trigger activation.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["documentId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Document . "mode" should be one of ['url', 'id']: 
  0.0 params["documentId"]["value"](when "mode"="url"): string: By URL
  0.1 params["documentId"]["value"](when "mode"="id"): string: By ID
1 params["sheetName"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Sheet . "mode" should be one of ['url', 'id']: 
  1.0 params["sheetName"]["value"](when "mode"="url"): string: By URL
  1.1 params["sheetName"]["value"](when "mode"="id"): string: By ID
2 params["filtersUI"]: dict[str,list[dict[str,any]]] = {}: Filters(Add Filter) . properties description:
  ...hidden...
3 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Read all rows from the specified Google Sheet document and sheetName.
  TODOs: 
    - Test reading Google Sheets data.
    - Verify data format for further processing.
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'commercial'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: First aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer'.
  TODOs: 
    - Build messages array in workflow.
    - Test AI classification.
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
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
[{'json': {'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}}, {'json': {'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}}, {'json': {'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}}, {'json': {'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}}, {'json': {'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}}, {'json': {'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}}, {'json': {'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}}, {'json': {'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}}, {'json': {'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}}, {'json': {'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141950.030729', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'dY3V', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141950.030729'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141951.074299', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'IUk', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141951.074299'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141952.329559', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '0tXuK', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141952.329559'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141953.403629', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'rZSE', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141953.403629'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141954.447079', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '4lvd5', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141954.447079'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141955.363049', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'HC59', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141955.363049'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141956.407249', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'I4t', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141956.407249'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141957.449459', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'eC7md', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141957.449459'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141958.517139', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ddz4h', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141958.517139'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141959.572089', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Qha', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141959.572089'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data):
  """
  comments: Send each classification result to Slack channel #general as a message with the text extracted from input_data.
  TODOs: 
    - Test Slack message sending.
    - Verify messages appear in #general channel.
  """
  params = { 'channelId': {'mode': 'name', 'value': 'general'},
             'messageType': 'text',
             'select': 'channel',
             'text': '={{$json["text"]}}'}
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': "Summary:\nEnterprise SaaS Solutions offers customized software designed to help businesses streamline their operations and boost productivity.\n\nReminder Email:\nSubject: Follow-up on Tailored Enterprise SaaS Solutions\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to follow up on our discussion about our Enterprise SaaS Solutions that are tailored to streamline your business operations and enhance productivity.\n\nPlease let me know if you have any questions or would like to schedule a demo to see how our solutions can benefit your organization.\n\nLooking forward to your response.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nCloud Infrastructure Services provide scalable and secure cloud computing solutions designed to help enterprises efficiently manage their data and applications.\n\nReminder Email:\nSubject: Reminder: Follow-up on Cloud Infrastructure Services Offering\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to remind you about our Cloud Infrastructure Services, which offer scalable and secure cloud computing solutions to help your enterprise efficiently manage data and applications.\n\nPlease let me know if you would like to discuss this further or schedule a demonstration.\n\nBest regards,  \n[Your Name]"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe commercial flow involves offering advanced data analytics tools and services designed to help businesses make informed decisions and enhance their overall performance through improved data insights.\n\nReminder Email:\nSubject: Follow-up on Data Analytics and Business Intelligence Solutions\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to follow up on our discussion regarding our advanced Data Analytics and Business Intelligence solutions. These tools and services are designed to empower your business with actionable insights, enabling better decision-making and improved overall performance.\n\nPlease let me know if you would like to schedule a demo or discuss how our solutions can be tailored to meet your specific needs.\n\nLooking forward to your response.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nBusiness Process Automation Services assist businesses in automating repetitive tasks and streamlining workflows. This leads to improved overall efficiency and reduced operational costs.\n\nReminder Email:\nSubject: Reminder: Explore Business Process Automation Services\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to remind you about our Business Process Automation Services designed to help your business automate repetitive tasks and streamline workflows. Implementing these services can significantly improve your operational efficiency and reduce costs.\n\nPlease let us know if you would like to discuss how we can tailor these solutions to your specific needs.\n\nBest regards,  \n[Your Name]  \n[Your Company]"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nCustomized Enterprise Integration Solutions provide tailored integration services that help businesses connect various systems and applications seamlessly. This enhances data flow and communication across the organization, improving overall efficiency.\n\nReminder Email:\nSubject: Follow-up on Customized Enterprise Integration Solutions\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to follow up regarding our Customized Enterprise Integration Solutions that offer tailored integration services to seamlessly connect your various systems and applications. This solution is designed to improve data flow and communication within your organization, enhancing operational efficiency.\n\nPlease let me know if you would like to discuss how we can customize these solutions to meet your specific business needs.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data):
  """
  comments: Second aiCompletion to generate reminder emails for 'to Customer' commercial flows.
  TODOs: 
    - Build messages array in workflow.
    - Test AI summarization and reminder generation.
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["sendTo"]: string = "", Required: To. The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com.(info@example.com)
1 params["subject"]: string = "", Required: Subject(Hello World!)
2 params["emailType"]: enum[string] = "text", Required: Email Type  You can't use expression.. Available values:
  2.0 value=="text": Text
  2.1 value=="html": HTML
3 params["message"]: string = "", Required: Message
4 params["options"]: dict = {}: Options(Add Option) . properties description:
  ...hidden...

This function has been executed for 5 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Business' commercial flows reminder", 'emailType': 'text', 'message': "Summary:\nCustomized Enterprise Integration Solutions provide tailored integration services that help businesses connect various systems and applications seamlessly. This enhances data flow and communication across the organization, improving overall efficiency.\n\nReminder Email:\nSubject: Follow-up on Customized Enterprise Integration Solutions\n\nDear [Recipient's Name],\n\nI hope this message finds you well. I wanted to follow up regarding our Customized Enterprise Integration Solutions that offer tailored integration services to seamlessly connect your various systems and applications. This solution is designed to improve data flow and communication within your organization, enhancing operational efficiency.\n\nPlease let me know if you would like to discuss how we can customize these solutions to meet your specific business needs.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"}}]

3.Output:
[{'json': {'id': '19afaa9e7d9d11b8', 'threadId': '19afaa9e7d9d11b8', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_4(input_data):
  """
  comments: Send reminder emails to corresponding managers with Gmail using extracted fields from input_data, fixing syntax errors in expression strings.
  TODOs: 
    - Test sending reminder emails after fixing syntax.
    - Verify emails received by managers without errors.
  """
  params = { 'emailType': 'text',
             'message': '={{$json["message"]}}',
             'sendTo': '={{$json["sendTo"]}}',
             'subject': '={{$json["subject"]}}'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
  """
  comments: Workflow triggered manually to process commercial entries, classify them, send Slack messages, generate reminders, and send emails.
  TODOs: 
    - Implement full data flow and transformations.
    - Test AI classification and email generation.
    - Verify Slack and Gmail message sending.
  """
  # Step 1: Read commercial entries from Google Sheets
  sheet_data = action_0(trigger_input)
  if not sheet_data or len(sheet_data) == 0:
    print("No data to process")
    return []  # No data to process

  # Extract rows (skip header if present)
  # Assuming first row is header
  rows = sheet_data
  # Calculate profit and prepare data with profit
  processed_entries = []
  for row in rows:
    json_data = row.get('json', {})
    try:
      cost = float(json_data.get('cost', 0))
      sales = float(json_data.get('sales', 0))
    except Exception:
      cost = 0.0
      sales = 0.0
    profit = sales - cost
    processed_entries.append({
      'Business Line': json_data.get('Business Line', ''),
      'Manager': json_data.get('Manager', ''),
      'cost': cost,
      'sales': sales,
      'Description': json_data.get('Description', ''),
      'profit': profit
    })
  print(f"Processed entries with profit: {processed_entries}")

  # Step 2: Build input for first aiCompletion to classify each Description
  ai_classify_input = []
  for entry in processed_entries:
    messages = [
      {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or 'to Customer'."},
      {"role": "user", "content": entry['Description']}
    ]
    ai_classify_input.append({"json": {"messages": messages}})

  ai_classify_output = action_1(ai_classify_input)
  print(f"AI classify output: {ai_classify_output}")

  # Step 3: Parse classification results and prepare Slack messages
  slack_messages = []
  classification_results = []
  for i, ai_item in enumerate(ai_classify_output):
    classification_text = ai_item['json']['choices'][0]['text'].strip() if 'choices' in ai_item['json'] else ''
    # Normalize classification text
    classification = 'to Business' if 'business' in classification_text.lower() else 'to Customer'
    classification_results.append(classification)

    entry = processed_entries[i]
    slack_text = f"Commercial Entry: {entry['Description']}\nProfit: {entry['profit']}\nCategory: {classification}"
    slack_messages.append({"json": {"text": slack_text}})
  print(f"Slack messages prepared: {slack_messages}")

  # Step 4: Send Slack messages
  if slack_messages:
    action_2(slack_messages)

  # Step 5: Filter entries for 'to Business' category for reminder emails
  to_business_entries = [processed_entries[i] for i, cat in enumerate(classification_results) if cat == 'to Business']

  # Step 6: Build input for second aiCompletion to generate reminders
  ai_reminder_input = []
  for entry in to_business_entries:
    messages = [
      {"role": "system", "content": "You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows."},
      {"role": "user", "content": entry['Description']}
    ]
    ai_reminder_input.append({"json": {"messages": messages}})

  ai_reminder_output = action_3(ai_reminder_input)
  print(f"AI reminder output: {ai_reminder_output}")

  # Step 7: Parse reminder content and send emails
  email_inputs = []
  for i, ai_item in enumerate(ai_reminder_output):
    reminder_content = ai_item['json']['choices'][0]['text'].strip() if 'choices' in ai_item['json'] else ''
    entry = to_business_entries[i]
    email_inputs.append({"json": {
      "sendTo": entry['Manager'],
      "subject": "'To Business' commercial flows reminder",
      "emailType": "text",
      "message": reminder_content
    }})
  print(f"Email inputs prepared: {email_inputs}")

  # Send emails
  if email_inputs:
    for email_input in email_inputs:
      action_4([email_input])

  return []



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""