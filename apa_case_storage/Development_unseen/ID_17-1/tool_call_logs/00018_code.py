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
  comments: 定义一个手动触发器，用户点击后触发工作流执行。
  TODOs: 
    - 测试触发器是否能正确触发
    - 确保输出格式正确
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
  comments: 设置Google Sheets读取参数，指定文档ID和表单名称
  TODOs: 
    - 测试读取数据是否成功
    - 调试数据格式
  """
  params = { 'documentId': {'mode': 'id', 'value': '1yMInqpKdzm-ZC9bT0dH-HMIm4P3eAZ17K8Yn251MsJY'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'commercial'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
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
[{'json': {'message': '[\n  {\n    "json": {\n      "row_number": 2,\n      "Business Line": 1,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 10000,\n      "sales": 50000,\n      "Description": "E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 3,\n      "Business Line": 2,\n      "Manager": "cc9008@nyu.edu",\n      "cost": 5000,\n      "sales": 30000,\n      "Description": "Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 4,\n      "Business Line": 3,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 20000,\n      "sales": 10000,\n      "Description": "Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 5,\n      "Business Line": 4,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 8000,\n      "sales": 7600,\n      "Description": "Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 6,\n      "Business Line": 5,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 6000,\n      "sales": 8000,\n      "Description": "Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 7,\n      "Business Line": 6,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 20000,\n      "sales": 60000,\n      "Description": "Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 8,\n      "Business Line": 7,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 80000,\n      "sales": 100000,\n      "Description": "Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 9,\n      "Business Line": 8,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 4000,\n      "sales": 25000,\n      "Description": "Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 10,\n      "Business Line": 9,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 7500,\n      "sales": 4000,\n      "Description": "Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  },\n  {\n    "json": {\n      "row_number": 11,\n      "Business Line": 10,\n      "Manager": "qwuqwuqwu@gmail.com",\n      "cost": 5000,\n      "sales": 3000,\n      "Description": "Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication."\n    },\n    "pairedItem": {\n      "item": 0\n    }\n  }\n]'}}]

3.Output:
[{'json': {'id': '19af62343d5b370b', 'threadId': '19af62343d5b370b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 将Google Sheets读取的数据序列化为JSON字符串作为邮件内容，设置邮件发送参数并发送邮件
  TODOs: 
    - 测试邮件发送是否成功
    - 验证邮件内容格式
    - 调试邮件发送异常
  """
  params = { 'emailType': 'text',
             'message': '={{JSON.stringify($json)}}',
             'options': {},
             'sendTo': 'qwuqwuqwu@gmail.com',
             'subject': 'commercial flows'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19af62343d5b370b', 'threadId': '19af62343d5b370b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input):
    """
    comments: 手动触发后读取Google Sheets数据并发送邮件
    TODOs:
      - 测试整个流程
      - 确保邮件内容格式正确
    """
    import json
    trigger_output = trigger_0(None)
    sheet_data = action_0(trigger_output)
    # 将整个sheet_data序列化为JSON字符串
    content = json.dumps(sheet_data, ensure_ascii=False, indent=2)
    # 构造新的input_data，包含message字段
    email_input = [{"json": {"message": content}}]
    send_output = action_1(email_input)
    return send_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""