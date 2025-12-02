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
  comments: Trigger the workflow manually by the user.
  TODOs: 
    - Test manual trigger
    - Ensure it starts the workflow correctly
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
  comments: Read all rows from the commercial sheet in Google Sheets using the provided document ID and sheet name.
  TODOs: 
    - Test reading data
    - Verify output data format
    - Ensure data contains expected columns
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
  comments: Use AI to classify each commercial entry description by passing messages from input data.
  TODOs: 
    - Test classification AI call
    - Verify classification output
  """
  params = {
             "messages": "={{$json[\"messages\"]}}"
           }
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.107249', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'OuR', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nProfit: 40000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764646990.107249'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.316449', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ergvZ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nProfit: 25000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764646990.316449'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.437049', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'nvEY', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nProfit: -10000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764646990.437049'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.555679', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'EM+OJ', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nProfit: -400.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764646990.555679'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.678379', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '9uL', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nProfit: 2000.0\nCategory: to Customer'}]}]}]}, 'message_timestamp': '1764646990.678379'}, 'pairedItem': {'item': 4}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646990.825459', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Ye1', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764646990.825459'}, 'pairedItem': {'item': 5}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646991.067199', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '6bB', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764646991.067199'}, 'pairedItem': {'item': 6}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646991.202189', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'J1q', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764646991.202189'}, 'pairedItem': {'item': 7}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646991.499509', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '+Rnz', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764646991.499509'}, 'pairedItem': {'item': 8}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764646991.632039', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '6hUq6', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nCategory: to Business'}]}]}]}, 'message_timestamp': '1764646991.632039'}, 'pairedItem': {'item': 9}}]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Send messages to Slack channel #general with classification results, using the text field from input data.
  TODOs: 
    - Test Slack message sending
    - Verify message format in Slack
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "general"
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
[{'json': {'choices': [{'text': 'Summary:\nThe e-commerce marketplace operates an online platform where consumers can browse and purchase a wide variety of products from multiple brands and sellers, providing a diverse shopping experience.\n\nReminder Email:\nSubject: Reminder: E-commerce Marketplace Operations\n\nDear Team,\n\nThis is a reminder about our ongoing operations of the e-commerce marketplace platform. Please ensure that the platform continues to offer a seamless shopping experience, featuring a wide range of products from various brands and sellers. Keep monitoring product listings, seller performance, and customer feedback to maintain high standards.\n\nBest regards,\n[Your Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nThe Online Food Delivery Service provides a convenient platform that allows consumers to order food from local restaurants and have it delivered directly to their doorstep.\n\nReminder Email:\nSubject: Reminder: Online Food Delivery Service Platform\n\nDear Team,\n\nThis is a friendly reminder about our Online Food Delivery Service platform, which offers consumers a convenient way to order food from local restaurants and receive it at their doorstep. Please ensure that all aspects of the service, including restaurant partnerships, order processing, and delivery logistics, are running smoothly to maintain customer satisfaction.\n\nBest regards,\n[Your Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nThe Online Travel Booking Portal is a comprehensive platform that allows consumers to conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Update and Optimize the Online Travel Booking Portal\n\nDear Team,\n\nThis is a reminder to review and update our Online Travel Booking Portal to ensure it continues to offer a seamless and comprehensive experience for our customers. Please focus on optimizing the booking processes for flights, hotels, and other travel-related services, and consider any new features or partnerships that could enhance user convenience.\n\nLet’s aim to complete this review by [insert deadline].\n\nBest regards,  \n[Your Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Summary:\nOffering users easy-to-use online tools and resources designed to help them manage personal finances, monitor expenses, and develop budgets effectively.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Management with Our Online Tools\n\nDear [User],\n\nWe wanted to remind you about the intuitive personal finance management tools available to help you take control of your finances. With our resources, you can easily track your expenses, create budgets, and manage your money more effectively.\n\nStart using these tools today to achieve your financial goals with confidence!\n\nBest regards,  \n[Your Company Name]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational resources designed to help users improve their skills and knowledge across multiple subjects.\n\nReminder Email:\nSubject: Reminder: Enhance Your Skills with Our Online Courses\n\nDear [Recipient's Name],\n\nWe wanted to remind you about our diverse selection of online courses and educational resources available on our platform. Whether you're looking to develop new skills or deepen your knowledge in various subjects, our courses are designed to support your learning journey.\n\nDon't miss out on the opportunity to grow and succeed. Visit our platform today to explore the courses that best suit your interests and goals.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Company Name]"}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data: List[Dict] =  [{...}]):
  """
  comments: Use AI to generate reminder emails for 'to Customer' entries.
  TODOs: 
    - Construct messages with system and user prompts
    - Test reminder email AI call
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
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nThe e-commerce marketplace operates an online platform where consumers can browse and purchase a wide variety of products from multiple brands and sellers, providing a diverse shopping experience.\n\nReminder Email:\nSubject: Reminder: E-commerce Marketplace Operations\n\nDear Team,\n\nThis is a reminder about our ongoing operations of the e-commerce marketplace platform. Please ensure that the platform continues to offer a seamless shopping experience, featuring a wide range of products from various brands and sellers. Keep monitoring product listings, seller performance, and customer feedback to maintain high standards.\n\nBest regards,\n[Your Name]'}}, {'json': {'sendTo': 'cc9008@nyu.edu', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nThe Online Food Delivery Service provides a convenient platform that allows consumers to order food from local restaurants and have it delivered directly to their doorstep.\n\nReminder Email:\nSubject: Reminder: Online Food Delivery Service Platform\n\nDear Team,\n\nThis is a friendly reminder about our Online Food Delivery Service platform, which offers consumers a convenient way to order food from local restaurants and receive it at their doorstep. Please ensure that all aspects of the service, including restaurant partnerships, order processing, and delivery logistics, are running smoothly to maintain customer satisfaction.\n\nBest regards,\n[Your Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nThe Online Travel Booking Portal is a comprehensive platform that allows consumers to conveniently book flights, hotels, and other travel-related services all in one place.\n\nReminder Email:\nSubject: Reminder: Update and Optimize the Online Travel Booking Portal\n\nDear Team,\n\nThis is a reminder to review and update our Online Travel Booking Portal to ensure it continues to offer a seamless and comprehensive experience for our customers. Please focus on optimizing the booking processes for flights, hotels, and other travel-related services, and consider any new features or partnerships that could enhance user convenience.\n\nLet’s aim to complete this review by [insert deadline].\n\nBest regards,  \n[Your Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': 'Summary:\nOffering users easy-to-use online tools and resources designed to help them manage personal finances, monitor expenses, and develop budgets effectively.\n\nReminder Email:\nSubject: Reminder: Enhance Your Financial Management with Our Online Tools\n\nDear [User],\n\nWe wanted to remind you about the intuitive personal finance management tools available to help you take control of your finances. With our resources, you can easily track your expenses, create budgets, and manage your money more effectively.\n\nStart using these tools today to achieve your financial goals with confidence!\n\nBest regards,  \n[Your Company Name]'}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': "'To Customer' commercial flows reminder", 'emailType': 'text', 'message': "Summary:\nThe Online Education and E-learning Platform provides a wide range of online courses and educational resources designed to help users improve their skills and knowledge across multiple subjects.\n\nReminder Email:\nSubject: Reminder: Enhance Your Skills with Our Online Courses\n\nDear [Recipient's Name],\n\nWe wanted to remind you about our diverse selection of online courses and educational resources available on our platform. Whether you're looking to develop new skills or deepen your knowledge in various subjects, our courses are designed to support your learning journey.\n\nDon't miss out on the opportunity to grow and succeed. Visit our platform today to explore the courses that best suit your interests and goals.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Company Name]"}}]

3.Output:
[{'json': {'id': '19add2890b356a8c', 'threadId': '19add2890b356a8c', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19add28929b32607', 'threadId': '19add28929b32607', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19add2896300c668', 'threadId': '19add2896300c668', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19add28986617ec9', 'threadId': '19add28986617ec9', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19add289f4811471', 'threadId': '19add289f4811471', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def action_4(input_data: List[Dict] =  [{...}]):
  """
  comments: Send reminder emails to corresponding managers via Gmail with subject and message from input data.
  TODOs: 
    - Test email sending
    - Verify email content and recipients
  """
  params = {
             "sendTo": "={{$json['sendTo']}}",
             "subject": "={{$json['subject']}}",
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
[{'json': {'id': '19add2890b356a8c', 'threadId': '19add2890b356a8c', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19add28929b32607', 'threadId': '19add28929b32607', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19add2896300c668', 'threadId': '19add2896300c668', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19add28986617ec9', 'threadId': '19add28986617ec9', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19add289f4811471', 'threadId': '19add289f4811471', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Main workflow to process commercial entries from Google Sheets, classify descriptions, send Slack messages, generate reminder emails for 'to Customer' entries, and send emails via Gmail.
    TODOs:
      - Test end-to-end workflow
      - Handle possible empty or missing fields
      - Validate AI outputs
    """
    # Step 1: Read data from Google Sheets
    commercial_data = action_0(trigger_input)  # read commercial sheet
    if not commercial_data or len(commercial_data) == 0:
        return []  # no data to process

    # Step 2: Calculate profit for each entry
    for item in commercial_data:
        json_data = item.get('json', {})
        try:
            cost = float(json_data.get('cost', 0))
        except Exception:
            cost = 0
        try:
            sales = float(json_data.get('sales', 0))
        except Exception:
            sales = 0
        profit = sales - cost
        json_data['profit'] = profit

    # Step 3: Prepare input for first AI classification
    ai_classify_input = []
    for item in commercial_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": description}
        ]
        ai_classify_input.append({"json": {"messages": messages}})

    # Step 4: Call AI classification
    ai_classify_output = action_1(ai_classify_input)

    # Step 5: Parse classification output and send Slack messages
    slack_messages = []
    for i, item in enumerate(ai_classify_output):
        classify_text = item['json'].get('choices', [{}])[0].get('text', '') if 'choices' in item['json'] else ''
        # simple parse category
        category = 'to Business' if 'to Business' in classify_text else ('to Customer' if 'to Customer' in classify_text else 'Unknown')
        commercial_entry = commercial_data[i]['json']
        commercial_entry['category'] = category
        description = commercial_entry.get('Description', '')
        profit = commercial_entry.get('profit', 0)
        slack_text = f"Commercial Entry: {description}\nProfit: {profit}\nCategory: {category}"
        slack_messages.append({"json": {"select": "channel", "channelId": {"mode": "name", "value": "general"}, "messageType": "text", "text": slack_text}})

    # Step 6: Send messages to Slack
    slack_output = action_2(slack_messages)

    # Step 7: Prepare input for second AI reminder generation for 'to Customer' entries
    ai_reminder_input = []
    customer_entries = []  # keep track of entries for sending email
    for item in commercial_data:
        if item['json'].get('category') == 'to Customer':
            description = item['json'].get('Description', '')
            manager = item['json'].get('Manager', '')
            messages = [
                {"role": "system", "content": "You are a summarizer and a reminder. Please summarize the provided commercial flows and write reminder emails for each flows."},
                {"role": "user", "content": description}
            ]
            ai_reminder_input.append({"json": {"messages": messages}})
            customer_entries.append({'manager': manager, 'description': description})

    # Step 8: Call AI reminder generation
    if ai_reminder_input:
        ai_reminder_output = action_3(ai_reminder_input)
    else:
        ai_reminder_output = []

    # Step 9: Send reminder emails via Gmail
    email_inputs = []
    for i, item in enumerate(ai_reminder_output):
        reminder_text = item['json'].get('choices', [{}])[0].get('text', '') if 'choices' in item['json'] else ''
        manager_email = customer_entries[i]['manager']
        if manager_email:
            email_inputs.append({"json": {
                "sendTo": manager_email,
                "subject": "'To Customer' commercial flows reminder",
                "emailType": "text",
                "message": reminder_text
            }})

    if email_inputs:
        email_output = action_4(email_inputs)
    else:
        email_output = []

    return email_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""