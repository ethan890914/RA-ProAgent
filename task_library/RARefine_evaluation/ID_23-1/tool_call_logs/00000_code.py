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
  comments: Trigger the workflow manually by user.
  TODOs: 
    - Test manual trigger functionality.
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
  comments: Update the Google Sheet documentId to the new one as per user query.
  TODOs: 
    - Test reading data from new Google Sheet document.
    - Verify data correctness.
  """
  params = { 'documentId': {'mode': 'id', 'value': '1yMInqpKdzm-ZC9bT0dH-HMIm4P3eAZ17K8Yn251MsJY'},
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
  comments: Perform AI completion for classifying commercial entry descriptions.
  TODOs: 
    - Build messages input in workflow.
    - Test classification.
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141276.917109', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '3S0Pe', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141276.917109'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141277.857079', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '+EQEl', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141277.857079'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141279.067689', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Ilyu', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141279.067689'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141279.988199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'rTGA', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141279.988199'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141281.042689', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'm8LHx', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1765141281.042689'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141281.955599', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'm31v', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141281.955599'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141283.003569', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'NtgjM', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141283.003569'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141283.898459', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'xYA', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141283.898459'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141284.793069', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'SBTE', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141284.793069'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1765141285.900699', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 's+I', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1765141285.900699'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data):
  """
  comments: Send messages to Slack channel #general with proper parameters.
  TODOs: 
    - Test Slack message sending
    - Verify messages appear in #general channel
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Summary:\nThe e-commerce marketplace operates an online platform where consumers can browse and purchase a wide variety of products from multiple brands and sellers in one convenient location.\n\nReminder Email:\nSubject: Reminder: E-commerce Marketplace Operations\n\nDear Team,\n\nThis is a friendly reminder about our ongoing operations of the e-commerce marketplace. Please ensure that the platform continues to provide a seamless shopping experience for consumers by maintaining a diverse range of products from various brands and sellers. Regularly check for product updates, seller compliance, and customer satisfaction to keep the marketplace running smoothly.\n\nBest regards,\n[Your Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Food Delivery Service provides a convenient platform for consumers to order food from local restaurants and have it delivered directly to their doorstep, ensuring a seamless and efficient dining experience.\n\nReminder Email:\nSubject: Reminder: Enhance Your Experience with Our Online Food Delivery Service\n\nDear [Customer Name],\n\nWe hope you're enjoying the convenience of ordering your favorite meals from local restaurants through our platform. Just a friendly reminder that we're here to make your dining experience effortless and enjoyable, with quick and reliable food delivery right to your doorstep.\n\nIf you haven't placed an order recently, why not explore our diverse restaurant options today? Your next delicious meal is just a few clicks away!\n\nBest regards,  \n[Your Company Name] Team"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Travel Booking Portal provides a comprehensive platform where consumers can conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Enhance Your Experience with Our Online Travel Booking Portal\n\nDear [Customer Name],\n\nWe hope you're enjoying the convenience of our Online Travel Booking Portal! Don't forget, you can easily book flights, hotels, and other travel-related services all in one place to make your travel planning seamless.\n\nIf you have any questions or need assistance, our support team is here to help.\n\nHappy travels!\n\nBest regards,  \n[Your Company Name] Team"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nThe flow involves offering users easy-to-use online personal finance management tools that help them monitor their expenses, manage their finances, and create budgets effectively.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Management with Our Online Tools\n\nDear [User],\n\nWe wanted to remind you about our intuitive online personal finance management tools designed to help you take control of your finances. With our resources, you can easily track your expenses, manage your budget, and make informed financial decisions.\n\nLog in today to start managing your personal finances more effectively!\n\nBest regards,  \n[Your Company Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational materials designed to help users improve their skills and knowledge across multiple subjects.\n\nReminder Email:\nSubject: Reminder: Enhance Your Skills with Our Online Courses\n\nDear [Recipient's Name],\n\nWe hope this message finds you well. This is a friendly reminder about our Online Education and E-learning Platform, where you can access a variety of courses and educational resources tailored to help you enhance your skills and knowledge in numerous subjects.\n\nDon't miss the opportunity to learn at your own pace and advance your expertise. Visit our platform today to explore the courses available.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Company Name]"}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data):
  """
  comments: Perform AI completion for generating reminder emails for 'to Customer' entries.
  TODOs: 
    - Build messages input in workflow.
    - Test reminder email generation.
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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nThe e-commerce marketplace operates an online platform where consumers can browse and purchase a wide variety of products from multiple brands and sellers in one convenient location.\n\nReminder Email:\nSubject: Reminder: E-commerce Marketplace Operations\n\nDear Team,\n\nThis is a friendly reminder about our ongoing operations of the e-commerce marketplace. Please ensure that the platform continues to provide a seamless shopping experience for consumers by maintaining a diverse range of products from various brands and sellers. Regularly check for product updates, seller compliance, and customer satisfaction to keep the marketplace running smoothly.\n\nBest regards,\n[Your Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': "Summary:\nThe Online Food Delivery Service provides a convenient platform for consumers to order food from local restaurants and have it delivered directly to their doorstep, ensuring a seamless and efficient dining experience.\n\nReminder Email:\nSubject: Reminder: Enhance Your Experience with Our Online Food Delivery Service\n\nDear [Customer Name],\n\nWe hope you're enjoying the convenience of ordering your favorite meals from local restaurants through our platform. Just a friendly reminder that we're here to make your dining experience effortless and enjoyable, with quick and reliable food delivery right to your doorstep.\n\nIf you haven't placed an order recently, why not explore our diverse restaurant options today? Your next delicious meal is just a few clicks away!\n\nBest regards,  \n[Your Company Name] Team"}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': "Summary:\nThe Online Travel Booking Portal provides a comprehensive platform where consumers can conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Enhance Your Experience with Our Online Travel Booking Portal\n\nDear [Customer Name],\n\nWe hope you're enjoying the convenience of our Online Travel Booking Portal! Don't forget, you can easily book flights, hotels, and other travel-related services all in one place to make your travel planning seamless.\n\nIf you have any questions or need assistance, our support team is here to help.\n\nHappy travels!\n\nBest regards,  \n[Your Company Name] Team"}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nThe flow involves offering users easy-to-use online personal finance management tools that help them monitor their expenses, manage their finances, and create budgets effectively.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Management with Our Online Tools\n\nDear [User],\n\nWe wanted to remind you about our intuitive online personal finance management tools designed to help you take control of your finances. With our resources, you can easily track your expenses, manage your budget, and make informed financial decisions.\n\nLog in today to start managing your personal finances more effectively!\n\nBest regards,  \n[Your Company Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational materials designed to help users improve their skills and knowledge across multiple subjects.\n\nReminder Email:\nSubject: Reminder: Enhance Your Skills with Our Online Courses\n\nDear [Recipient's Name],\n\nWe hope this message finds you well. This is a friendly reminder about our Online Education and E-learning Platform, where you can access a variety of courses and educational resources tailored to help you enhance your skills and knowledge in numerous subjects.\n\nDon't miss the opportunity to learn at your own pace and advance your expertise. Visit our platform today to explore the courses available.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Company Name]"}}]

3.Output:
[{'json': {'id': '19afa9eec529796e', 'threadId': '19afa9eec529796e', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19afa9ef02942bda', 'threadId': '19afa9ef02942bda', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19afa9ef65b8618b', 'threadId': '19afa9ef65b8618b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19afa9efb596b65b', 'threadId': '19afa9efb596b65b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19afa9f01fb460d5', 'threadId': '19afa9f01fb460d5', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def action_4(input_data):
  """
  comments: Send reminder emails with proper parameters extracted from input_data fields.
  TODOs: 
    - Test Gmail email sending
    - Verify emails are received at the specified address
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
[{'json': {'id': '19afa9eec529796e', 'threadId': '19afa9eec529796e', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19afa9ef02942bda', 'threadId': '19afa9ef02942bda', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19afa9ef65b8618b', 'threadId': '19afa9ef65b8618b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19afa9efb596b65b', 'threadId': '19afa9efb596b65b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19afa9f01fb460d5', 'threadId': '19afa9f01fb460d5', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to process commercial entries from Google Sheets, classify descriptions, send Slack messages, and email reminders.
    TODOs:
      - Implement stepwise data processing
      - Test AI classification and reminder generation
      - Test Slack and Gmail message sending
    """
    # Step 1: Read data from Google Sheets
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        # No data read, return early
        return []

    # Step 2: Calculate profit = sales - cost for each entry
    # The sheet columns: Business Line, Manager, cost, sales, Description
    processed_data = []
    for item in sheet_data:
        json_data = item.get('json', {})
        cost = json_data.get('cost')
        sales = json_data.get('sales')
        description = json_data.get('Description')
        # Convert cost and sales to float safely
        try:
            cost_val = float(cost)
        except (TypeError, ValueError):
            cost_val = 0.0
        try:
            sales_val = float(sales)
        except (TypeError, ValueError):
            sales_val = 0.0
        profit = sales_val - cost_val
        processed_data.append({
            'Description': description,
            'profit': profit
        })

    # Step 3: Build input for first aiCompletion (classification)
    ai_input_classify = []
    for item in processed_data:
        description = item['Description'] or ''
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": description}
        ]
        ai_input_classify.append({"json": {"messages": messages}})

    # Call first aiCompletion
    ai_classify_output = action_1(ai_input_classify)

    # Step 4: Parse classification results and combine with profit and description
    combined_results = []
    for idx, ai_item in enumerate(ai_classify_output):
        classify_text = ai_item.get('json', {}).get('choices', [{}])[0].get('text', '').strip().lower()
        # Determine category
        if 'to business' in classify_text:
            category = 'to Business'
        elif 'to customer' in classify_text:
            category = 'to Customer'
        else:
            category = 'Unknown'
        combined_results.append({
            'Description': processed_data[idx]['Description'],
            'profit': processed_data[idx]['profit'],
            'category': category
        })

    # Step 5: Send Slack messages for each entry
    slack_input = []
    for item in combined_results:
        text = f"Commercial Entry: {item['Description']}\nProfit: {item['profit']}\nCategory: {item['category']}"
        slack_input.append({"json": {"text": text}})

    slack_params = {
        "select": "channel",
        "channelId": {"mode": "name", "value": "general"},
        "messageType": "text",
        "text": "={{$json[\"text\"]}}"
    }
    slack_output = action_2(slack_input)

    # Step 6: Filter 'to Customer' entries for reminder emails
    to_customer_entries = [item for item in combined_results if item['category'] == 'to Customer']
    if not to_customer_entries:
        # No to Customer entries, finish workflow
        return slack_output

    # Step 7: Build input for second aiCompletion (reminder email content)
    ai_input_reminder = []
    for item in to_customer_entries:
        description = item['Description'] or ''
        messages = [
            {"role": "system", "content": "You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows."},
            {"role": "user", "content": description}
        ]
        ai_input_reminder.append({"json": {"messages": messages}})

    ai_reminder_output = action_3(ai_input_reminder)

    # Step 8: Parse reminder email content and send emails
    gmail_input = []
    for item in ai_reminder_output:
        reminder_content = item.get('json', {}).get('choices', [{}])[0].get('text', '').strip()
        gmail_input.append({
            "json": {
                "sendTo": "qwuqwuqwu@gmail.com",
                "subject": "'To Customer' commercial flows reminder",
                "emailType": "text",
                "message": reminder_content
            }
        })

    gmail_output = action_4(gmail_input)

    return gmail_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""