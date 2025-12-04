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
  comments: Trigger the workflow manually by user click.
  TODOs: 
    - Test trigger activation.
    - Ensure output format matches workflow input.
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
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Read commercial entries from Google Sheets with specified document ID and sheet name.
  TODOs: 
    - Test reading and output schema.
    - Verify data correctness.
  """
  params = {
             "documentId": {
               "mode": "id",
               "value": "1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c"
             },
             "sheetName": {
               "mode": "id",
               "value": "commercial"
             },
             "filtersUI": {},
             "options": {}
           }
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Classify each Description as 'to Business' or 'to Customer'.
  TODOs: 
    - Build input messages in workflow.
    - Parse classification output.
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
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
[{'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}}, {'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'general'}, 'messageType': 'text', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645927.916699', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '7CT', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764645927.916699'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.058439', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ErDe', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764645928.058439'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.192199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'dORP', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764645928.192199'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.330969', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '7AC4', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764645928.330969'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.460839', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'iOp', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764645928.460839'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.597669', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'w3E', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764645928.597669'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.727179', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Esd', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764645928.727179'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645928.874629', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'W+K', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764645928.874629'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645929.006139', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '83VI+', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764645929.006139'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764645929.133919', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'jGmv', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764645929.133919'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Send each commercial entry's classification result to Slack channel #general with correct parameters.
  TODOs: 
    - Test Slack message sending after fixing parameters.
    - Verify message delivery and formatting.
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "={{$json[\"channelName\"] || \"general\"}}"
             },
             "messageType": "text",
             "text": "={{$json[\"text\"]}}"
           }
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows.'}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Summary:\nThe e-commerce marketplace operates an online platform that enables consumers to purchase a diverse range of products from multiple brands and sellers, facilitating a broad and convenient shopping experience.\n\nReminder Email:\nSubject: Reminder: Ongoing Operations and Updates for E-commerce Marketplace\n\nDear Team,\n\nThis is a friendly reminder about our ongoing operations of the e-commerce marketplace platform. Please ensure that all systems are running smoothly to provide consumers with a seamless shopping experience across our wide range of products and sellers.\n\nKindly review the current seller listings, product availability, and customer feedback to maintain high service standards. Let’s continue to support various brands and sellers effectively to drive growth and customer satisfaction.\n\nThank you for your attention and dedication.\n\nBest regards,  \n[Your Name]  \n[Your Position]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nThe Online Food Delivery Service provides a convenient platform that allows consumers to order food from local restaurants and have it delivered directly to their doorstep.\n\nReminder Email:\nSubject: Reminder: Ensure Smooth Operation of Our Online Food Delivery Service\n\nDear Team,\n\nThis is a reminder to regularly monitor and maintain the efficiency of our Online Food Delivery Service platform. Please ensure that the ordering system is functioning smoothly, restaurant listings are up to date, and delivery operations are timely and reliable.\n\nLet’s continue providing our customers with a seamless and convenient food ordering experience.\n\nBest regards,\n[Your Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Travel Booking Portal is a comprehensive platform that allows consumers to conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Enhance Your Travel Experience with Our Online Booking Portal\n\nDear [Recipient's Name],\n\nWe wanted to remind you about our comprehensive Online Travel Booking Portal, designed to make your travel planning seamless and convenient. Whether you're looking to book flights, hotels, or other travel-related services, our platform offers everything you need in one place.\n\nStart exploring and planning your next trip with ease today!\n\nBest regards,  \n[Your Name]  \n[Your Company]"}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nOnline Personal Finance Management Tools offer users intuitive features and resources to manage their personal finances effectively. These tools help in tracking expenses and creating budgets to promote better financial planning.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Health with Our Personal Finance Tools\n\nDear [User],\n\nWe wanted to remind you about the powerful online personal finance management tools available to help you take control of your finances. With our intuitive platform, you can easily track your expenses and create budgets tailored to your needs.\n\nStart managing your personal finances more effectively today!\n\nBest regards,  \n[Your Company Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational resources designed to help users improve their skills and knowledge across various subjects.\n\nReminder Email:\nSubject: Reminder: Explore Our Online Courses to Enhance Your Skills\n\nDear [User],\n\nWe hope you're doing well! This is a friendly reminder to take advantage of our diverse range of online courses and educational resources available on our platform. Whether you want to develop new skills or deepen your knowledge in various subjects, we have something tailored for you.\n\nVisit our platform today and continue your learning journey!\n\nBest regards,  \n[Your Company Name] Team"}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data: List[Dict] =  [{...}]):
  """
  comments: Generate reminder email content for 'to Customer' entries.
  TODOs: 
    - Build input messages in workflow.
    - Parse reminder content output.
  """
  params = {}  # to be Implemented
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
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'To Customer commercial flows reminder', 'emailType': 'text', 'message': 'Summary:\nThe e-commerce marketplace operates an online platform that enables consumers to purchase a diverse range of products from multiple brands and sellers, facilitating a broad and convenient shopping experience.\n\nReminder Email:\nSubject: Reminder: Ongoing Operations and Updates for E-commerce Marketplace\n\nDear Team,\n\nThis is a friendly reminder about our ongoing operations of the e-commerce marketplace platform. Please ensure that all systems are running smoothly to provide consumers with a seamless shopping experience across our wide range of products and sellers.\n\nKindly review the current seller listings, product availability, and customer feedback to maintain high service standards. Let’s continue to support various brands and sellers effectively to drive growth and customer satisfaction.\n\nThank you for your attention and dedication.\n\nBest regards,  \n[Your Name]  \n[Your Position]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'To Customer commercial flows reminder', 'emailType': 'text', 'message': 'Summary:\nThe Online Food Delivery Service provides a convenient platform that allows consumers to order food from local restaurants and have it delivered directly to their doorstep.\n\nReminder Email:\nSubject: Reminder: Ensure Smooth Operation of Our Online Food Delivery Service\n\nDear Team,\n\nThis is a reminder to regularly monitor and maintain the efficiency of our Online Food Delivery Service platform. Please ensure that the ordering system is functioning smoothly, restaurant listings are up to date, and delivery operations are timely and reliable.\n\nLet’s continue providing our customers with a seamless and convenient food ordering experience.\n\nBest regards,\n[Your Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'To Customer commercial flows reminder', 'emailType': 'text', 'message': "Summary:\nThe Online Travel Booking Portal is a comprehensive platform that allows consumers to conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Enhance Your Travel Experience with Our Online Booking Portal\n\nDear [Recipient's Name],\n\nWe wanted to remind you about our comprehensive Online Travel Booking Portal, designed to make your travel planning seamless and convenient. Whether you're looking to book flights, hotels, or other travel-related services, our platform offers everything you need in one place.\n\nStart exploring and planning your next trip with ease today!\n\nBest regards,  \n[Your Name]  \n[Your Company]"}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'To Customer commercial flows reminder', 'emailType': 'text', 'message': 'Summary:\nOnline Personal Finance Management Tools offer users intuitive features and resources to manage their personal finances effectively. These tools help in tracking expenses and creating budgets to promote better financial planning.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Health with Our Personal Finance Tools\n\nDear [User],\n\nWe wanted to remind you about the powerful online personal finance management tools available to help you take control of your finances. With our intuitive platform, you can easily track your expenses and create budgets tailored to your needs.\n\nStart managing your personal finances more effectively today!\n\nBest regards,  \n[Your Company Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'To Customer commercial flows reminder', 'emailType': 'text', 'message': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational resources designed to help users improve their skills and knowledge across various subjects.\n\nReminder Email:\nSubject: Reminder: Explore Our Online Courses to Enhance Your Skills\n\nDear [User],\n\nWe hope you're doing well! This is a friendly reminder to take advantage of our diverse range of online courses and educational resources available on our platform. Whether you want to develop new skills or deepen your knowledge in various subjects, we have something tailored for you.\n\nVisit our platform today and continue your learning journey!\n\nBest regards,  \n[Your Company Name] Team"}}]

3.Output:
[{'json': {'id': '19add185c3d09eb0', 'threadId': '19add185c3d09eb0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19add185f04c632b', 'threadId': '19add185f04c632b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19add186010e2560', 'threadId': '19add186010e2560', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19add1865be2e225', 'threadId': '19add1865be2e225', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19add1868745eeda', 'threadId': '19add1868745eeda', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def action_4(input_data: List[Dict] =  [{...}]):
  """
  comments: Send reminder emails to specified email address with required parameters set.
  TODOs: 
    - Test email sending functionality.
    - Verify email content and delivery.
  """
  params = {
             "sendTo": "qwuqwuqwu@gmail.com",
             "subject": "To Customer commercial flows reminder",
             "emailType": "text",
             "message": "={{$json['message']}}"
           }
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19add185c3d09eb0', 'threadId': '19add185c3d09eb0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19add185f04c632b', 'threadId': '19add185f04c632b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19add186010e2560', 'threadId': '19add186010e2560', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19add1865be2e225', 'threadId': '19add1865be2e225', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19add1868745eeda', 'threadId': '19add1868745eeda', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to process commercial entries: read, classify, send Slack messages, generate and send reminder emails.
    TODOs:
      - Test end-to-end workflow
      - Refine AI prompt and parsing if needed
      - Handle empty or error cases gracefully
    """
    # Step 1: Read commercial entries from Google Sheets
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        return []  # No data to process

    # Step 2: Calculate profit = sales - cost for each entry
    for item in sheet_data:
        cost = float(item['json'].get('cost', 0))
        sales = float(item['json'].get('sales', 0))
        profit = sales - cost
        item['json']['profit'] = profit

    # Step 3: Build first AI input messages for classification
    ai_input_classify = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": description}
        ]
        ai_input_classify.append({"json": {"messages": messages}})

    # Step 4: Call first aiCompletion for classification
    classify_results = action_1(ai_input_classify)

    # Step 5: Parse classification results and add category to each item
    for i, item in enumerate(sheet_data):
        ai_text = classify_results[i]['json']['choices'][0]['text'].strip().lower() if i < len(classify_results) else ""
        if 'to business' in ai_text:
            category = 'to Business'
        elif 'to customer' in ai_text:
            category = 'to Customer'
        else:
            category = 'Unknown'
        item['json']['category'] = category

    # Step 6: Send Slack messages for each entry
    slack_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        profit = item['json'].get('profit', 0)
        category = item['json'].get('category', 'Unknown')
        text = f"Commercial Entry: {description}\nProfit: {profit}\nCategory: {category}"
        slack_input.append({"json": {"select": "channel", "channelId": {"mode": "name", "value": "general"}, "messageType": "text", "text": text}})
    slack_results = action_2(slack_input)

    # Step 7: Filter 'to Customer' entries for reminder emails
    to_customer_entries = [item for item in sheet_data if item['json'].get('category') == 'to Customer']
    if not to_customer_entries:
        return slack_results  # No emails to send

    # Step 8: Build second AI input messages for reminder emails
    ai_input_reminder = []
    for item in to_customer_entries:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows."},
            {"role": "user", "content": description}
        ]
        ai_input_reminder.append({"json": {"messages": messages}})

    # Step 9: Call second aiCompletion for reminder email content
    reminder_results = action_3(ai_input_reminder)

    # Step 10: Send reminder emails via Gmail
    gmail_input = []
    for i, item in enumerate(to_customer_entries):
        reminder_content = reminder_results[i]['json']['choices'][0]['text'].strip() if i < len(reminder_results) else ""
        gmail_input.append({"json": {
            "sendTo": "qwuqwuqwu@gmail.com",
            "subject": "To Customer commercial flows reminder",
            "emailType": "text",
            "message": reminder_content
        }})
    gmail_results = action_4(gmail_input)

    return gmail_results




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""