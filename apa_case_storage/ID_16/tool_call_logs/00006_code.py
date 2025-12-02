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
  comments: 手动触发器，用户点击按钮启动工作流
  TODOs: 
    - 实现触发器参数（无参数）
    - 测试触发器能否正常触发
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
  comments: 读取指定Google Sheet文档和工作表的数据，文档ID和工作表名称来自用户输入
  TODOs: 
    - 测试读取数据是否正确
    - 调整参数以适应实际数据格式
    - 准备数据传递给Slack发送动作
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
[{'json': {'text': '[{"row_number": 2, "Business Line": 1, "Manager": "qwuqwuqwu@gmail.com", "cost": 10000, "sales": 50000, "Description": "E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers."}, {"row_number": 3, "Business Line": 2, "Manager": "cc9008@nyu.edu", "cost": 5000, "sales": 30000, "Description": "Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep."}, {"row_number": 4, "Business Line": 3, "Manager": "qwuqwuqwu@gmail.com", "cost": 20000, "sales": 10000, "Description": "Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently."}, {"row_number": 5, "Business Line": 4, "Manager": "qwuqwuqwu@gmail.com", "cost": 8000, "sales": 7600, "Description": "Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets."}, {"row_number": 6, "Business Line": 5, "Manager": "qwuqwuqwu@gmail.com", "cost": 6000, "sales": 8000, "Description": "Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects."}, {"row_number": 7, "Business Line": 6, "Manager": "qwuqwuqwu@gmail.com", "cost": 20000, "sales": 60000, "Description": "Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity."}, {"row_number": 8, "Business Line": 7, "Manager": "qwuqwuqwu@gmail.com", "cost": 80000, "sales": 100000, "Description": "Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently."}, {"row_number": 9, "Business Line": 8, "Manager": "qwuqwuqwu@gmail.com", "cost": 4000, "sales": 25000, "Description": "Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance."}, {"row_number": 10, "Business Line": 9, "Manager": "qwuqwuqwu@gmail.com", "cost": 7500, "sales": 4000, "Description": "Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs."}, {"row_number": 11, "Business Line": 10, "Manager": "qwuqwuqwu@gmail.com", "cost": 5000, "sales": 3000, "Description": "Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication."}]'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764620016.808529', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '{"text":"[{\\"row_number\\": 2, \\"Business Line\\": 1, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 10000, \\"sales\\": 50000, \\"Description\\": \\"E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\\"}, {\\"row_number\\": 3, \\"Business Line\\": 2, \\"Manager\\": \\"<mailto:cc9008@nyu.edu|cc9008@nyu.edu>\\", \\"cost\\": 5000, \\"sales\\": 30000, \\"Description\\": \\"Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\\"}, {\\"row_number\\": 4, \\"Business Line\\": 3, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 20000, \\"sales\\": 10000, \\"Description\\": \\"Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\\"}, {\\"row_number\\": 5, \\"Business Line\\": 4, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 8000, \\"sales\\": 7600, \\"Description\\": \\"Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\\"}, {\\"row_number\\": 6, \\"Business Line\\": 5, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 6000, \\"sales\\": 8000, \\"Description\\": \\"Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\\"}, {\\"row_number\\": 7, \\"Business Line\\": 6, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 20000, \\"sales\\": 60000, \\"Description\\": \\"Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\\"}, {\\"row_number\\": 8, \\"Business Line\\": 7, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 80000, \\"sales\\": 100000, \\"Description\\": \\"Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\\"}, {\\"row_number\\": 9, \\"Business Line\\": 8, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 4000, \\"sales\\": 25000, \\"Description\\": \\"Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\\"}, {\\"row_number\\": 10, \\"Business Line\\": 9, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 7500, \\"sales\\": 4000, \\"Description\\": \\"Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\\"}, {\\"row_number\\": 11, \\"Business Line\\": 10, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 5000, \\"sales\\": 3000, \\"Description\\": \\"Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\\"}]"}', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'b7HC', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '{"text":"[{\\"row_number\\": 2, \\"Business Line\\": 1, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 10000, \\"sales\\": 50000, \\"Description\\": \\"E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\\"}, {\\"row_number\\": 3, \\"Business Line\\": 2, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:cc9008@nyu.edu', 'text': 'cc9008@nyu.edu'}, {'type': 'text', 'text': '\\", \\"cost\\": 5000, \\"sales\\": 30000, \\"Description\\": \\"Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\\"}, {\\"row_number\\": 4, \\"Business Line\\": 3, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 20000, \\"sales\\": 10000, \\"Description\\": \\"Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\\"}, {\\"row_number\\": 5, \\"Business Line\\": 4, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 8000, \\"sales\\": 7600, \\"Description\\": \\"Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\\"}, {\\"row_number\\": 6, \\"Business Line\\": 5, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 6000, \\"sales\\": 8000, \\"Description\\": \\"Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\\"}, {\\"row_number\\": 7, \\"Business Line\\": 6, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 20000, \\"sales\\": 60000, \\"Description\\": \\"Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\\"}, {\\"row_number\\": 8, \\"Business Line\\": 7, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 80000, \\"sales\\": 100000, \\"Description\\": \\"Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\\"}, {\\"row_number\\": 9, \\"Business Line\\": 8, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 4000, \\"sales\\": 25000, \\"Description\\": \\"Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\\"}, {\\"row_number\\": 10, \\"Business Line\\": 9, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 7500, \\"sales\\": 4000, \\"Description\\": \\"Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\\"}, {\\"row_number\\": 11, \\"Business Line\\": 10, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 5000, \\"sales\\": 3000, \\"Description\\": \\"Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\\"}]"}'}]}]}]}, 'message_timestamp': '1764620016.808529'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 将Google Sheets读取的数据转换为字符串并发送到Slack的#general频道，blocksUi字段设置为空数组字符串以满足必填要求
  TODOs: 
    - 测试消息发送是否成功
    - 调整消息格式以适应需求
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "general"
             },
             "messageType": "text",
             "text": "={{JSON.stringify($json)}}",
             "blocksUi": "[]",
             "attachments": [],
             "otherOptions": {}
           }
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C09UW58R413', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764620016.808529', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': '{"text":"[{\\"row_number\\": 2, \\"Business Line\\": 1, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 10000, \\"sales\\": 50000, \\"Description\\": \\"E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\\"}, {\\"row_number\\": 3, \\"Business Line\\": 2, \\"Manager\\": \\"<mailto:cc9008@nyu.edu|cc9008@nyu.edu>\\", \\"cost\\": 5000, \\"sales\\": 30000, \\"Description\\": \\"Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\\"}, {\\"row_number\\": 4, \\"Business Line\\": 3, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 20000, \\"sales\\": 10000, \\"Description\\": \\"Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\\"}, {\\"row_number\\": 5, \\"Business Line\\": 4, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 8000, \\"sales\\": 7600, \\"Description\\": \\"Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\\"}, {\\"row_number\\": 6, \\"Business Line\\": 5, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 6000, \\"sales\\": 8000, \\"Description\\": \\"Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\\"}, {\\"row_number\\": 7, \\"Business Line\\": 6, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 20000, \\"sales\\": 60000, \\"Description\\": \\"Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\\"}, {\\"row_number\\": 8, \\"Business Line\\": 7, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 80000, \\"sales\\": 100000, \\"Description\\": \\"Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\\"}, {\\"row_number\\": 9, \\"Business Line\\": 8, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 4000, \\"sales\\": 25000, \\"Description\\": \\"Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\\"}, {\\"row_number\\": 10, \\"Business Line\\": 9, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 7500, \\"sales\\": 4000, \\"Description\\": \\"Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\\"}, {\\"row_number\\": 11, \\"Business Line\\": 10, \\"Manager\\": \\"<mailto:qwuqwuqwu@gmail.com|qwuqwuqwu@gmail.com>\\", \\"cost\\": 5000, \\"sales\\": 3000, \\"Description\\": \\"Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\\"}]"}', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'b7HC', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': '{"text":"[{\\"row_number\\": 2, \\"Business Line\\": 1, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 10000, \\"sales\\": 50000, \\"Description\\": \\"E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\\"}, {\\"row_number\\": 3, \\"Business Line\\": 2, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:cc9008@nyu.edu', 'text': 'cc9008@nyu.edu'}, {'type': 'text', 'text': '\\", \\"cost\\": 5000, \\"sales\\": 30000, \\"Description\\": \\"Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\\"}, {\\"row_number\\": 4, \\"Business Line\\": 3, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 20000, \\"sales\\": 10000, \\"Description\\": \\"Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\\"}, {\\"row_number\\": 5, \\"Business Line\\": 4, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 8000, \\"sales\\": 7600, \\"Description\\": \\"Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\\"}, {\\"row_number\\": 6, \\"Business Line\\": 5, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 6000, \\"sales\\": 8000, \\"Description\\": \\"Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\\"}, {\\"row_number\\": 7, \\"Business Line\\": 6, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 20000, \\"sales\\": 60000, \\"Description\\": \\"Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\\"}, {\\"row_number\\": 8, \\"Business Line\\": 7, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 80000, \\"sales\\": 100000, \\"Description\\": \\"Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\\"}, {\\"row_number\\": 9, \\"Business Line\\": 8, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 4000, \\"sales\\": 25000, \\"Description\\": \\"Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\\"}, {\\"row_number\\": 10, \\"Business Line\\": 9, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 7500, \\"sales\\": 4000, \\"Description\\": \\"Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\\"}, {\\"row_number\\": 11, \\"Business Line\\": 10, \\"Manager\\": \\"'}, {'type': 'link', 'url': 'mailto:qwuqwuqwu@gmail.com', 'text': 'qwuqwuqwu@gmail.com'}, {'type': 'text', 'text': '\\", \\"cost\\": 5000, \\"sales\\": 3000, \\"Description\\": \\"Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\\"}]"}'}]}]}]}, 'message_timestamp': '1764620016.808529'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 该工作流由手动触发器启动，读取指定Google Sheets数据并将所有数据整合为一个字符串发送到Slack的#general频道
    TODOs:
      - 测试整体工作流是否正常执行
      - 验证数据整合和消息发送是否正确
    """
    # 调用Google Sheets读取动作
    sheets_data = action_0(trigger_input)

    # 将所有读取数据整合为一个字符串
    import json
    combined_json_str = json.dumps([item["json"] for item in sheets_data], ensure_ascii=False)

    # 构造单条输入数据传递给Slack发送动作
    slack_input = [{"json": {"text": combined_json_str}}]

    # 调用Slack消息发送动作，将整合后的字符串发送
    slack_output = action_1(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""