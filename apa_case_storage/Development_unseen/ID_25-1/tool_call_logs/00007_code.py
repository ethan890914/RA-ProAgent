"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: 手动触发器，用于启动整个工作流
  TODOs: 
    - 测试触发器是否能正常触发
    - 确保触发器输出格式正确
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
  comments: 读取Google Sheets中商业流数据，包含cost和sales列，配置文档ID和表单名称
  TODOs: 
    - 测试读取数据是否正确
    - 确保返回包含cost和sales字段
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
[{'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}], 'profit': 40000.0, 'description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}], 'profit': 25000.0, 'description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'manager': 'cc9008@nyu.edu'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}], 'profit': -10000.0, 'description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}], 'profit': -400.0, 'description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}], 'profit': 2000.0, 'description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}], 'profit': 40000.0, 'description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}], 'profit': 20000.0, 'description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}], 'profit': 21000.0, 'description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}], 'profit': -3500.0, 'description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.', 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Description: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}], 'profit': -2000.0, 'description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'manager': 'qwuqwuqwu@gmail.com'}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 调用AI完成商业流类型分类，输入包含描述文本
  TODOs: 
    - 构造AI输入messages数组
    - 测试分类结果
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are an email writer. Generate reminder email content for business managers about commercial entries. In your reminder, first give them a summary, and then lists all commercial entries description.'}, {'role': 'user', 'content': 'Descriptions:\nE-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nOnline Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nOnline Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nOnline Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}], 'manager': 'qwuqwuqwu@gmail.com'}}, {'json': {'messages': [{'role': 'system', 'content': 'You are an email writer. Generate reminder email content for business managers about commercial entries. In your reminder, first give them a summary, and then lists all commercial entries description.'}, {'role': 'user', 'content': 'Descriptions:\nOnline Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}], 'manager': 'cc9008@nyu.edu'}}]

3.Output:
[{'json': {'choices': [{'text': 'Subject: Reminder: Review of Commercial Entries for Your Business Management\n\nDear Business Managers,\n\nThis is a friendly reminder to review and familiarize yourselves with the key commercial entries relevant to our operations. Ensuring a clear understanding of these entries will help us align our strategies and optimize our business processes effectively.\n\nSummary of Commercial Entries:\n\n1. E-commerce Marketplace  \n2. Online Travel Booking Portal  \n3. Online Personal Finance Management Tools  \n4. Online Education and E-learning Platform  \n\nDetailed Descriptions:\n\n1. **E-commerce Marketplace**  \n   Operating an online platform for consumers to purchase a wide range of products from various brands and sellers. This entry focuses on facilitating seamless transactions, broad product availability, and an engaging user experience.\n\n2. **Online Travel Booking Portal**  \n   Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently. It aims to provide competitive pricing, ease of use, and reliable booking options.\n\n3. **Online Personal Finance Management Tools**  \n   Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets. This entry supports financial literacy and empowers users to make informed financial decisions.\n\n4. **Online Education and E-learning Platform**  \n   Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects. The platform focuses on accessibility, diverse content, and interactive learning experiences.\n\nPlease ensure that you review these entries thoroughly and consider how they impact your respective departments. Should you have any questions or require further information, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Subject: Reminder: Review of Commercial Entries – Online Food Delivery Service\n\nDear Business Managers,\n\nI hope this message finds you well. This is a friendly reminder to review the current commercial entries related to our service offerings. Keeping these entries up to date ensures clarity and consistency in our business communications and marketing efforts.\n\nSummary:\nWe currently have one key commercial entry that highlights our service in the food delivery sector.\n\nCommercial Entries Description:\n- Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\n\nPlease take a moment to review this entry and provide any updates or feedback by the end of this week.\n\nThank you for your attention and cooperation.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}]}, 'pairedItem': {'item': 0}}]
"""
def action_2(input_data):
  """
  comments: 调用AI生成给客户经理的提醒邮件内容，输入包含多个描述文本
  TODOs: 
    - 构造AI输入messages数组
    - 测试邮件内容生成
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_3(input_data):
  """
  comments: 向Slack频道发送商业流利润信息
  TODOs: 
    - 配置频道为#general
    - 测试消息发送
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="slack", resource="message", operation="post")
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
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': 'Commercial Flow Reminder - to Customer', 'emailType': 'text', 'message': 'Subject: Reminder: Review of Commercial Entries for Your Business Management\n\nDear Business Managers,\n\nThis is a friendly reminder to review and familiarize yourselves with the key commercial entries relevant to our operations. Ensuring a clear understanding of these entries will help us align our strategies and optimize our business processes effectively.\n\nSummary of Commercial Entries:\n\n1. E-commerce Marketplace  \n2. Online Travel Booking Portal  \n3. Online Personal Finance Management Tools  \n4. Online Education and E-learning Platform  \n\nDetailed Descriptions:\n\n1. **E-commerce Marketplace**  \n   Operating an online platform for consumers to purchase a wide range of products from various brands and sellers. This entry focuses on facilitating seamless transactions, broad product availability, and an engaging user experience.\n\n2. **Online Travel Booking Portal**  \n   Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently. It aims to provide competitive pricing, ease of use, and reliable booking options.\n\n3. **Online Personal Finance Management Tools**  \n   Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets. This entry supports financial literacy and empowers users to make informed financial decisions.\n\n4. **Online Education and E-learning Platform**  \n   Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects. The platform focuses on accessibility, diverse content, and interactive learning experiences.\n\nPlease ensure that you review these entries thoroughly and consider how they impact your respective departments. Should you have any questions or require further information, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}}]

3.Output:
[]
"""
def action_4(input_data):
  """
  comments: 发送提醒邮件给商业流经理，配置收件人、主题、邮件类型和邮件内容，emailType固定为'text'
  TODOs: 
    - 测试邮件发送功能
    - 确保邮件内容正确发送给对应经理
  """
  params = { 'emailType': 'text',
             'message': '={{$json["message"]}',
             'sendTo': '={{$json["sendTo"]}',
             'subject': '={{$json["subject"]}'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedInner
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 手动触发器触发，读取Google Sheets商业流数据，计算利润，调用AI分类商业流类型，分别发送Slack消息或邮件提醒
    TODOs:
      - 测试整体流程是否顺畅
      - 处理数据格式转换和分组
      - 完善AI输入消息构造
      - 测试Slack和邮件发送
    """
    # 1. 触发器触发
    trigger_output = trigger_0(trigger_input)

    # 2. 读取Google Sheets商业流数据
    sheet_data = action_0(trigger_output)
    if not sheet_data or len(sheet_data) == 0:
        return []

    # 3. 计算利润并构造第一轮AI分类输入
    ai_classify_input = []
    for item in sheet_data:
        json_data = item.get('json', {})
        cost = json_data.get('cost')
        sales = json_data.get('sales')
        description = json_data.get('Description', '')
        manager = json_data.get('Manager', '')

        # 计算profit，确保cost和sales为数字
        try:
            profit = float(sales) - float(cost)
        except Exception:
            profit = 0.0

        # 构造AI分类输入消息
        messages = [
            {"role": "system", "content": "You are a commercial flow classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": f"Description: {description}"}
        ]
        ai_classify_input.append({"json": {"messages": messages, "profit": profit, "description": description, "manager": manager}})

    # 4. 调用AI完成分类
    ai_classify_output = action_1(ai_classify_input)

    # 5. 处理分类结果，分组数据
    to_business_msgs = []
    to_customer_groups = {}

    for idx, ai_item in enumerate(ai_classify_output):
        classification_text = ai_item.get('json', {}).get('choices', [{}])[0].get('text', '').strip().lower()
        origin = ai_classify_input[idx]['json']
        profit = origin.get('profit', 0.0)
        description = origin.get('description', '')
        manager = origin.get('manager', '')

        # 判断分类
        if 'to business' in classification_text:
            # 构造Slack消息
            msg_text = f"Commercial Flow: {description}\nProfit: {profit}\nType: to Business"
            to_business_msgs.append({"json": {"text": msg_text}})
        elif 'to customer' in classification_text:
            # 分组
            if manager not in to_customer_groups:
                to_customer_groups[manager] = []
            to_customer_groups[manager].append(description)

    # 6. 对to Customer分组，调用第二轮AI生成邮件内容
    email_send_list = []
    for manager, descriptions in to_customer_groups.items():
        # 构造邮件内容AI输入
        summary_desc = '\n'.join(descriptions)
        messages = [
            {"role": "system", "content": "You are an email writer. Generate reminder email content for business managers about commercial entries. In your reminder, first give them a summary, and then lists all commercial entries description."},
            {"role": "user", "content": f"Descriptions:\n{summary_desc}"}
        ]
        email_send_list.append({"json": {"messages": messages, "manager": manager}})

    # 7. 调用AI生成邮件内容
    ai_email_output = action_2(email_send_list) if email_send_list else []

    # 8. 发送邮件
    for idx, email_item in enumerate(ai_email_output):
        content = email_item.get('json', {}).get('choices', [{}])[0].get('text', '')
        manager = email_send_list[idx]['json']['manager']
        if content and manager:
            email_input = [{"json": {"sendTo": manager, "subject": "Commercial Flow Reminder - to Customer", "emailType": "text", "message": content}}]
            action_4(email_input)

    # 9. 发送Slack消息
    if to_business_msgs:
        action_3(to_business_msgs)

    return []



"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}, 'pairedItem': {'item': 0}}]`
the output data of function `action_0` is: `[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}]`
the output data of function `action_1` is: `[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]`
the output data of function `action_2` is: `[{'json': {'choices': [{'text': 'Subject: Reminder: Review of Commercial Entries for Your Business Management\n\nDear Business Managers,\n\nThis is a friendly reminder to review and familiarize yourselves with the key commercial entries relevant to our operations. Ensuring a clear understanding of these entries will help us align our strategies and optimize our business processes effectively.\n\nSummary of Commercial Entries:\n\n1. E-commerce Marketplace  \n2. Online Travel Booking Portal  \n3. Online Personal Finance Management Tools  \n4. Online Education and E-learning Platform  \n\nDetailed Descriptions:\n\n1. **E-commerce Marketplace**  \n   Operating an online platform for consumers to purchase a wide range of products from various brands and sellers. This entry focuses on facilitating seamless transactions, broad product availability, and an engaging user experience.\n\n2. **Online Travel Booking Portal**  \n   Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently. It aims to provide competitive pricing, ease of use, and reliable booking options.\n\n3. **Online Personal Finance Management Tools**  \n   Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets. This entry supports financial literacy and empowers users to make informed financial decisions.\n\n4. **Online Education and E-learning Platform**  \n   Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects. The platform focuses on accessibility, diverse content, and interactive learning experiences.\n\nPlease ensure that you review these entries thoroughly and consider how they impact your respective departments. Should you have any questions or require further information, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Subject: Reminder: Review of Commercial Entries – Online Food Delivery Service\n\nDear Business Managers,\n\nI hope this message finds you well. This is a friendly reminder to review the current commercial entries related to our service offerings. Keeping these entries up to date ensures clarity and consistency in our business communications and marketing efforts.\n\nSummary:\nWe currently have one key commercial entry that highlights our service in the food delivery sector.\n\nCommercial Entries Description:\n- Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\n\nPlease take a moment to review this entry and provide any updates or feedback by the end of this week.\n\nThank you for your attention and cooperation.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]'}]}, 'pairedItem': {'item': 0}}]`
the output data of function `action_3` is: `[]`
the output data of function `action_4` is: `[]`

------------------------
In Function: mainWorkflow
                email_input = [{"json": {"sendTo": manager, "subject": "Commercial Flow Reminder - to Customer", "emailType": "text", "message": content}}]
-->             action_4(email_input)
------------------------
In Function: transparent_action
      function = transparent_action(integration="gmail", resource="message", operation="send")
-->   output_data = function.run(input_data=input_data, params=params)
      return output_data
------------------------
n8nRunningException: Execution Failed: 
Output: Execution was NOT successful. See log message for details.
Execution error:
====================================
{
  "data": {
    "startData": {},
    "resultData": {
      "runData": {
        "Start": [
          {
            "startTime": 1765071217845,
            "executionIndex": 0,
            "source": [],
            "hints": [],
            "executionTime": 2,
            "executionStatus": "success",
            "data": {
              "main": [
                [
                  {
                    "json": {},
                    "pairedItem": {
                      "item": 0
                    }
                  }
                ]
              ]
            }
          }
        ],
        "Code_Inject_Data": [
          {
            "startTime": 1765071217847,
            "executionIndex": 1,
            "source": [
              {
                "previousNode": "Start"
              }
            ],
            "hints": [
              {
                "message": "To make sure expressions after this node work, return the input items that produced each output item. <a target=\"_blank\" href=\"https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/\">More info</a>",
                "location": "outputPane"
              }
            ],
            "executionTime": 38,
            "executionStatus": "success",
            "data": {
              "main": [
                [
                  {
                    "json": {
                      "sendTo": "qwuqwuqwu@gmail.com",
                      "subject": "Commercial Flow Reminder - to Customer",
                      "emailType": "text",
                      "message": "Subject: Reminder: Review of Commercial Entries for Your Business Management\n\nDear Business Managers,\n\nThis is a friendly reminder to review and familiarize yourselves with the key commercial entries relevant to our operations. Ensuring a clear understanding of these entries will help us align our strategies and optimize our business processes effectively.\n\nSummary of Commercial Entries:\n\n1. E-commerce Marketplace  \n2. Online Travel Booking Portal  \n3. Online Personal Finance Management Tools  \n4. Online Education and E-learning Platform  \n\nDetailed Descriptions:\n\n1. **E-commerce Marketplace**  \n   Operating an online platform for consumers to purchase a wide range of products from various brands and sellers. This entry focuses on facilitating seamless transactions, broad product availability, and an engaging user experience.\n\n2. **Online Travel Booking Portal**  \n   Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently. It aims to provide competitive pricing, ease of use, and reliable booking options.\n\n3. **Online Personal Finance Management Tools**  \n   Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets. This entry supports financial literacy and empowers users to make informed financial decisions.\n\n4. **Online Education and E-learning Platform**  \n   Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects. The platform focuses on accessibility, diverse content, and interactive learning experiences.\n\nPlease ensure that you review these entries thoroughly and consider how they impact your respective departments. Should you have any questions or require further information, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"
                    },
                    "pairedItem": {
                      "item": 0
                    }
                  }
                ]
              ]
            }
          }
        ],
        "Target_Node": [
          {
            "startTime": 1765071217885,
            "executionIndex": 2,
            "source": [
              {
                "previousNode": "Code_Inject_Data"
              }
            ],
            "hints": [],
            "executionTime": 47,
            "executionStatus": "error",
            "error": {
              "level": "warning",
              "tags": {},
              "timestamp": 1765071217894,
              "context": {
                "itemIndex": 0
              },
              "functionality": "regular",
              "name": "NodeOperationError",
              "node": {
                "id": "6f0a831b-9982-431d-b15e-12c858445766",
                "name": "Target_Node",
                "position": [
                  400,
                  0
                ],
                "type": "n8n-nodes-base.gmail",
                "credentials": {
                  "gmailOAuth2": {
                    "id": "bHtMB5PbHhaIUNyl",
                    "name": "Gmail account"
                  }
                },
                "parameters": {
                  "preBuiltAgentsCalloutGmail": "",
                  "authentication": "oAuth2",
                  "resource": "message",
                  "operation": "send",
                  "sendTo": "={{$json[\"sendTo\"]}",
                  "subject": "={{$json[\"subject\"]}",
                  "emailType": "text",
                  "message": "={{$json[\"message\"]}",
                  "options": {}
                }
              },
              "messages": [],
              "message": "invalid syntax (item 0)",
              "stack": "NodeOperationError: invalid syntax (item 0)\n    at ExecuteContext.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-nodes-base/nodes/Google/Gmail/v2/GmailV2.node.ts:836:11)\n    at WorkflowExecute.executeNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1093:31)\n    at WorkflowExecute.runNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1274:22)\n    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1708:38\n    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:2324:11"
            }
          }
        ]
      },
      "lastNodeExecuted": "Target_Node",
      "error": {
        "level": "warning",
        "tags": {},
        "timestamp": 1765071217894,
        "context": {
          "itemIndex": 0
        },
        "functionality": "regular",
        "name": "NodeOperationError",
        "node": {
          "id": "6f0a831b-9982-431d-b15e-12c858445766",
          "name": "Target_Node",
          "position": [
            400,
            0
          ],
          "type": "n8n-nodes-base.gmail",
          "credentials": {
            "gmailOAuth2": {
              "id": "bHtMB5PbHhaIUNyl",
              "name": "Gmail account"
            }
          },
          "parameters": {
            "preBuiltAgentsCalloutGmail": "",
            "authentication": "oAuth2",
            "resource": "message",
            "operation": "send",
            "sendTo": "={{$json[\"sendTo\"]}",
            "subject": "={{$json[\"subject\"]}",
            "emailType": "text",
            "message": "={{$json[\"message\"]}",
            "options": {}
          }
        },
        "messages": [],
        "message": "invalid syntax (item 0)",
        "stack": "NodeOperationError: invalid syntax (item 0)\n    at ExecuteContext.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-nodes-base/nodes/Google/Gmail/v2/GmailV2.node.ts:836:11)\n    at WorkflowExecute.executeNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1093:31)\n    at WorkflowExecute.runNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1274:22)\n    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1708:38\n    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:2324:11"
      }
    },
    "executionData": {
      "contextData": {},
      "nodeExecutionStack": [
        {
          "node": {
            "id": "6f0a831b-9982-431d-b15e-12c858445766",
            "name": "Target_Node",
            "position": [
              400,
              0
            ],
            "type": "n8n-nodes-base.gmail",
            "credentials": {
              "gmailOAuth2": {
                "id": "bHtMB5PbHhaIUNyl",
                "name": "Gmail account"
              }
            },
            "parameters": {
              "preBuiltAgentsCalloutGmail": "",
              "authentication": "oAuth2",
              "resource": "message",
              "operation": "send",
              "sendTo": "={{$json[\"sendTo\"]}",
              "subject": "={{$json[\"subject\"]}",
              "emailType": "text",
              "message": "={{$json[\"message\"]}",
              "options": {}
            }
          },
          "data": {
            "main": [
              [
                {
                  "json": {
                    "sendTo": "qwuqwuqwu@gmail.com",
                    "subject": "Commercial Flow Reminder - to Customer",
                    "emailType": "text",
                    "message": "Subject: Reminder: Review of Commercial Entries for Your Business Management\n\nDear Business Managers,\n\nThis is a friendly reminder to review and familiarize yourselves with the key commercial entries relevant to our operations. Ensuring a clear understanding of these entries will help us align our strategies and optimize our business processes effectively.\n\nSummary of Commercial Entries:\n\n1. E-commerce Marketplace  \n2. Online Travel Booking Portal  \n3. Online Personal Finance Management Tools  \n4. Online Education and E-learning Platform  \n\nDetailed Descriptions:\n\n1. **E-commerce Marketplace**  \n   Operating an online platform for consumers to purchase a wide range of products from various brands and sellers. This entry focuses on facilitating seamless transactions, broad product availability, and an engaging user experience.\n\n2. **Online Travel Booking Portal**  \n   Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently. It aims to provide competitive pricing, ease of use, and reliable booking options.\n\n3. **Online Personal Finance Management Tools**  \n   Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets. This entry supports financial literacy and empowers users to make informed financial decisions.\n\n4. **Online Education and E-learning Platform**  \n   Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects. The platform focuses on accessibility, diverse content, and interactive learning experiences.\n\nPlease ensure that you review these entries thoroughly and consider how they impact your respective departments. Should you have any questions or require further information, feel free to reach out.\n\nBest regards,  \n[Your Name]  \n[Your Position]  \n[Your Contact Information]"
                  },
                  "pairedItem": {
                    "item": 0
                  }
                }
              ]
            ]
          },
          "source": {
            "main": [
              {
                "previousNode": "Code_Inject_Data"
              }
            ]
          }
        }
      ],
      "metadata": {},
      "waitingExecution": {},
      "waitingExecutionSource": {}
    }
  },
  "mode": "cli",
  "startedAt": "2025-12-07T01:33:37.842Z",
  "stoppedAt": "2025-12-07T01:33:37.932Z",
  "status": "running"
}
Error executing workflow. See log messages for details.

Execution error:
====================================
invalid syntax (item 0)
NodeOperationError: invalid syntax (item 0)
    at ExecuteContext.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-nodes-base/nodes/Google/Gmail/v2/GmailV2.node.ts:836:11)
    at WorkflowExecute.executeNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1093:31)
    at WorkflowExecute.runNode (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1274:22)
    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1708:38
    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:2324:11
invalid syntax (item 0)


You can also see the runnning result for all functions in there comments.
"""