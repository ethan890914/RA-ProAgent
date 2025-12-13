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
  comments: 手动触发器，作为工作流入口，触发后开始执行流程。
  TODOs: 
    - 测试触发器是否能正常触发
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
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: 读取Google Sheets中指定文档和表单的所有数据，获取商业流程数据。
  TODOs: 
    - 测试读取数据是否正确
    - 检查是否包含标题行
    - 确保包含cost和sales字段
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'commercial-small'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"}, {'role': 'user', 'content': "业务流程描述: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}]}}, {'json': {'messages': [{'role': 'system', 'content': "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"}, {'role': 'user', 'content': "业务流程描述: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}]}}, {'json': {'messages': [{'role': 'system', 'content': "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"}, {'role': 'user', 'content': "业务流程描述: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}]}}, {'json': {'messages': [{'role': 'system', 'content': "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"}, {'role': 'user', 'content': "业务流程描述: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}]}}, {'json': {'messages': [{'role': 'system', 'content': "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"}, {'role': 'user', 'content': "业务流程描述: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 调用AI完成，判断业务流程类型（to Business或to Customer）。
  TODOs: 
    - 构建AI输入消息
    - 测试AI返回结果
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'business_flow_type': 'to Business'}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 主流程，触发后读取Google Sheets数据，调用AI判断业务流程类型，若为'to Business'则显示。
    TODOs: 
      - 调试Google Sheets读取动作
      - 构建AI输入消息
      - 解析AI返回结果
    """
    # Step1: 读取Google Sheets数据
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        # 读取失败或无数据，返回提示
        return [{"json": {"result": "未读取到Google Sheets数据"}}]

    # Step2: 提取描述字段，构建AI输入
    descriptions = []
    for item in sheet_data:
        desc = item["json"].get("Description")
        if desc:
            descriptions.append(desc)
    if not descriptions:
        return [{"json": {"result": "无描述字段数据"}}]

    # 构建AI消息
    ai_input = []
    for desc in descriptions:
        messages = [
            {"role": "system", "content": "你是一个商业流程分析助手。根据描述判断业务流程类型，返回'to Business'或'to Customer'。"},
            {"role": "user", "content": f"业务流程描述: {desc}. 请告诉我这是'to Business'还是'to Customer'. 只返回'to Business'或'to Customer'。"}
        ]
        ai_input.append({"json": {"messages": messages}})

    # Step3: 调用AI完成判断类型
    ai_output = action_1(ai_input)
    if not ai_output:
        return [{"json": {"result": "AI未返回结果"}}]

    # Step4: 解析AI结果，若包含'to Business'则返回，否则不返回
    for item in ai_output:
        ai_text = item["json"].get("choices", [{}])[0].get("text", "").strip().lower()
        if "to business" in ai_text:
            return [{"json": {"business_flow_type": "to Business"}}]
    return [{"json": {"business_flow_type": "不是 to Business 类型"}}]



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""