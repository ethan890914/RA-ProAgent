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
  comments: Manual trigger to start the workflow on user click.
  TODOs: 
    - Implement trigger function
    - Test trigger activation
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Read business flow data from the specified Google Sheet document and sheet name 'commercial'.
  TODOs: 
    - Test reading data
    - Verify output schema
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 调用AI完成节点，基于输入的messages进行业务流类型分类。
  TODOs: 
    - 完善AI调用参数
    - 测试AI分类功能
    - 确保参数格式正确
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {}}]

3.Output:
[]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: "主流程：手动触发，读取Google Sheet中的业务流数据，调用AI判断业务流类型，过滤并展示'to B'类型业务流。"
    TODOs: [
        "测试手动触发是否正常启动",
        "测试Google Sheets读取数据是否正确",
        "测试AI分类功能是否准确",
        "测试过滤逻辑是否正确",
        "整体流程测试"
    ]

    # 第一步：调用Google Sheets读取业务数据
    sheet_data = action_0(trigger_input)

    # 第二步：构建AI输入数据，基于每行的Description字段
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C"},
            {"role": "user", "content": f"Based on the description: {description}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C"}
        ]
        ai_input.append({"json": {"messages": messages}})

    # 第三步：调用AI完成节点进行分类
    ai_output = action_1(ai_input)

    # 第四步：过滤出业务类型为'to B'的项
    to_b_results = []
    for i, ai_item in enumerate(ai_output):
        ai_text = ai_item['json']['choices'][0]['text'].strip().lower()
        if ai_text == 'to b':
            to_b_results.append(sheet_data[i])

    # 返回过滤后的'to B'业务流数据
    return to_b_results




"""

The directly running result for now codes with print results are as following:


In Function: mainWorkflow
--> Execution failed, but line number could not be mapped to the workflow code (IndexError avoided).
Reported Line: N/A, Code Length: 38
------------------------
SyntaxError: unterminated triple-quoted string literal (detected at line 38) (<string>, line 2)

You can also see the runnning result for all functions in there comments.
"""