"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
None

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: Manual trigger to start the workflow when user clicks the button.
  TODOs: 
    - Test the manual trigger activation.
    - Ensure it outputs correct trigger data.
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
[{'json': {}, 'pairedItem': {'item': 0}}]

3.Output:
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Read commercial flow data from Google Sheets document with specified documentId and sheetName 'commercial'.
  TODOs: 
    - Test reading data and verify output format.
    - Ensure cost and sales columns are present in output.
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
[{'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}], 'profit': 40000.0, 'description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}], 'profit': 25000.0, 'description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'manager': 'cc9008@nyu.edu'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}], 'profit': -10000.0, 'description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}], 'profit': -400.0, 'description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}], 'profit': 2000.0, 'description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}], 'profit': 40000.0, 'description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}], 'profit': 20000.0, 'description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}], 'profit': 21000.0, 'description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}], 'profit': -3500.0, 'description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}], 'profit': -2000.0, 'description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'manager': 'qwuqwuqwu@gmail.com'}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Use AI to classify each commercial flow entry as 'to Business' or 'to Customer'.
  TODOs: 
    - Build messages input in workflow for each entry.
    - Test AI classification output.
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
[{'json': {'text': 'Commercial Flow: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nType: to Business'}}, {'json': {'text': 'Commercial Flow: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nType: to Business'}}, {'json': {'text': 'Commercial Flow: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nType: to Business'}}, {'json': {'text': 'Commercial Flow: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nType: to Business'}}, {'json': {'text': 'Commercial Flow: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nType: to Business'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935668.696229', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'fR5d2', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935668.696229'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935669.626299', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'N+xY', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935669.626299'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935670.624089', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'YZ7', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935670.624089'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935671.528489', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'jcsRb', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935671.528489'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935672.428599', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'sil', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935672.428599'}, 'pairedItem': {'item': 4}}]
"""
def action_2(input_data):
  """
  comments: Send message to Slack channel #general for commercial flows classified as 'to Business'.
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

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are an email writer. Generate reminder email content for business managers about commercial entries. In your reminder, first lists all commercial entries description, and then give them a summary.'}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}], 'manager': 'cc9008@nyu.edu'}}]

3.Output:
[{'json': {'choices': [{'text': 'Subject: Reminder: Review of Commercial Entries – Online Food Delivery Service\n\nDear Business Managers,\n\nThis is a friendly reminder to review the commercial entries related to our current projects. Below is the description of the key commercial entry for your reference:\n\n- Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\n\nSummary:\nThe Online Food Delivery Service is designed to enhance customer convenience by providing an easy-to-use platform connecting consumers with local restaurants. This service aims to expand our market reach and increase customer satisfaction through timely and reliable food delivery.\n\nPlease ensure that all relevant documentation and assessments related to this commercial entry are up to date. Should you have any questions or require further details, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}]}, 'pairedItem': {'item': 0}}]
"""
def action_3(input_data):
  """
  comments: Use AI to generate reminder email content for 'to Customer' commercial flows grouped by manager.
  TODOs: 
    - Build messages input in workflow for grouped entries.
    - Test AI email content generation.
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

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'sendTo': 'cc9008@nyu.edu', 'subject': 'Commercial Flow Reminder - to Customer', 'emailType': 'text', 'message': 'Subject: Reminder: Review of Commercial Entries – Online Food Delivery Service\n\nDear Business Managers,\n\nThis is a friendly reminder to review the commercial entries related to our current projects. Below is the description of the key commercial entry for your reference:\n\n- Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\n\nSummary:\nThe Online Food Delivery Service is designed to enhance customer convenience by providing an easy-to-use platform connecting consumers with local restaurants. This service aims to expand our market reach and increase customer satisfaction through timely and reliable food delivery.\n\nPlease ensure that all relevant documentation and assessments related to this commercial entry are up to date. Should you have any questions or require further details, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}}]

3.Output:
[{'json': {'id': '19aee5da6a6a0a3a', 'threadId': '19aee5da6a6a0a3a', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 0}}]
"""
def action_4(input_data):
  """
  comments: Send reminder email to business flow manager for 'to Customer' commercial flows.
  TODOs: 
    - Test sending email via Gmail after fixing params.
    - Verify emails are received by managers.
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
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935668.696229', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'fR5d2', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nProfit: 40000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935668.696229'}, 'pairedItem': {'item': 0}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935669.626299', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'N+xY', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nProfit: 20000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935669.626299'}, 'pairedItem': {'item': 1}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935670.624089', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'YZ7', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nProfit: 21000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935670.624089'}, 'pairedItem': {'item': 2}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935671.528489', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'jcsRb', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nProfit: -3500.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935671.528489'}, 'pairedItem': {'item': 3}}, {'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764935672.428599', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Commercial Flow: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nType: to Business', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'sil', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Commercial Flow: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nProfit: -2000.0\nType: to Business'}]}]}]}, 'message_timestamp': '1764935672.428599'}, 'pairedItem': {'item': 4}}, {'json': {'id': '19aee5d685f4dee3', 'threadId': '19aee5d685f4dee3', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19aee5da6a6a0a3a', 'threadId': '19aee5da6a6a0a3a', 'labelIds': ['UNREAD', 'SENT', 'INBOX']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 该workflow从手动触发开始，读取Google Sheets商业流数据，计算利润，调用AI分类，并根据分类结果发送Slack消息或邮件提醒。
    TODOs:
      - 测试整体流程的正确性。
      - 验证AI分类和邮件内容生成的准确性。
      - 验证Slack消息和邮件发送是否成功。
    """
    # 1. 手动触发，无需输入数据，直接调用
    trigger_output = trigger_0(None)

    # 2. 读取Google Sheets商业流数据
    sheet_data = action_0(trigger_output)
    if not sheet_data:
        # 无数据时直接返回
        return []

    # 3. 计算利润并准备AI分类输入
    ai_classify_input = []
    for item in sheet_data:
        json_data = item.get('json', {})
        cost = json_data.get('cost')
        sales = json_data.get('sales')
        description = json_data.get('Description') or json_data.get('description') or ''
        manager = json_data.get('Manager') or json_data.get('manager') or ''
        # 计算利润
        try:
            profit = float(sales) - float(cost)
        except Exception:
            profit = 0.0

        # 保存利润到json
        json_data['profit'] = profit

        # 构建AI分类消息
        messages = [
            {"role": "system", "content": "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": description}
        ]

        ai_classify_input.append({"json": {"messages": messages, "profit": profit, "description": description, "manager": manager}})

    # 4. 调用AI进行分类
    ai_classify_output = action_1(ai_classify_input)

    # 5. 根据分类结果处理数据
    to_business_msgs = []
    to_customer_groups = {}

    for idx, ai_item in enumerate(ai_classify_output):
        classification_raw = ai_item['json']['choices'][0]['text'].strip().lower()
        # 简单判断分类
        if 'business' in classification_raw:
            flow_type = 'to Business'
        elif 'customer' in classification_raw:
            flow_type = 'to Customer'
        else:
            flow_type = 'unknown'

        # 获取对应的商业流数据
        original_item = sheet_data[idx]
        json_data = original_item['json']
        profit = json_data.get('profit', 0.0)
        description = json_data.get('Description') or json_data.get('description') or ''
        manager = json_data.get('Manager') or json_data.get('manager') or ''

        if flow_type == 'to Business':
            # 构建Slack消息
            text = f"Commercial Flow: {description}\nProfit: {profit}\nType: {flow_type}"
            to_business_msgs.append({"json": {"text": text}})
        elif flow_type == 'to Customer':
            # 按经理分组
            if manager not in to_customer_groups:
                to_customer_groups[manager] = []
            to_customer_groups[manager].append(description)

    # 6. 发送Slack消息
    slack_output = []
    if to_business_msgs:
        slack_output = action_2(to_business_msgs)

    # 7. 为每个经理生成邮件提醒内容并发送邮件
    email_outputs = []
    for manager, descriptions in to_customer_groups.items():
        # 构建AI邮件内容生成输入
        user_prompt = "\n".join(descriptions)
        messages = [
            {"role": "system", "content": "You are an email writer. Generate reminder email content for business managers about commercial entries. In your reminder, first lists all commercial entries description, and then give them a summary."},
            {"role": "user", "content": user_prompt}
        ]
        ai_email_input = [{"json": {"messages": messages, "manager": manager}}]

        # 调用AI生成邮件内容
        ai_email_output = action_3(ai_email_input)

        # 提取邮件内容
        email_content = ai_email_output[0]['json']['choices'][0]['text'] if ai_email_output else ''

        # 构建邮件发送输入
        email_input = [{
            "json": {
                "sendTo": manager,
                "subject": "Commercial Flow Reminder - to Customer",
                "emailType": "text",
                "message": email_content
            }
        }]

        # 发送邮件
        email_output = action_4(email_input)
        email_outputs.extend(email_output)

    # 返回Slack和邮件发送的结果
    return slack_output + email_outputs



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""