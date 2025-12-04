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
  comments: 定义手动触发器，用户点击按钮触发工作流
  TODOs: 
    - 测试触发器是否正常触发
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
  comments: 读取指定Google Sheets文档和工作表的所有行数据，获取业务流数据
  TODOs: 
    - 测试读取数据是否正确
    - 根据返回数据调整后续处理
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
[{'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': '你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。'}, {'role': 'user', 'content': '业务描述: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': '业务流类型: to C（to Customer）'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务面向消费者个人，属于to C（to Customer）业务流。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务面向消费者，属于to C（to Customer）业务流。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述针对的是个人用户，提供个人理财管理工具，帮助用户管理个人财务、跟踪支出和制定预算，属于面向消费者的服务。\n\n业务流类型：to C（to Customer）'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务面向个人用户提供在线课程和教育资源，属于to C（to Customer）业务流。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述是为企业提供定制的软件解决方案，帮助企业优化运营和提升生产力，属于面向企业的服务。因此，业务流类型是 to B（to Business）。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述面向企业客户，提供云基础设施服务，属于to B（to Business）业务流。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述主要是为企业提供数据分析和商业智能解决方案，帮助企业做出明智决策和提升整体绩效，因此业务流类型是 to B（to Business）。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述的服务对象是“帮助企业自动化重复任务和简化工作流程”，明显面向的是企业客户，属于to B（to Business）业务流。'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': '该业务描述面向企业，提供定制化的企业集成解决方案，帮助企业连接各种系统和应用，实现数据流和通信的优化。因此，业务流类型是 to B（to Business）。'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 修正AI输入消息构造，确保传递正确的业务描述给AI
  TODOs: 
    - 测试修正后的AI调用效果
    - 验证筛选逻辑是否正确
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 主工作流，触发后读取Google Sheets数据，调用AI判断业务流类型，筛选to B类型并返回
    TODOs:
      - 测试整个工作流的连接和数据流
      - 处理Google Sheets读取为空的情况
      - 优化AI输入消息构造
    """
    # 1. 调用Google Sheets读取动作
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        # 如果读取为空，直接返回空列表
        return []

    # 2. 构造AI输入数据，基于描述字段（Description）
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "你是一个业务流分类助手。请根据业务描述判断业务流类型，是to B（to Business）还是to C（to Customer）。"},
            {"role": "user", "content": f"业务描述: {description}"}
        ]
        ai_input.append({"json": {"messages": messages}})

    # 3. 调用AI完成动作
    ai_output = action_1(ai_input)

    # 4. 根据AI结果筛选出业务流类型为to B的项
    to_b_items = []
    for i, ai_item in enumerate(ai_output):
        ai_text = ai_item['json']['choices'][0]['text'].lower()
        if 'to b' in ai_text or 'tob' in ai_text:
            to_b_items.append(sheet_data[i])

    # 5. 返回筛选的to B项
    return to_b_items




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""