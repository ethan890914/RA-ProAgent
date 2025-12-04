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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: 调用AI完成，用于判断业务流类型（to B还是to C）
  TODOs: 
    - 构造AI输入消息
    - 测试AI响应是否符合预期
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
  comments: You need to give comments when implementing mainWorkflow
  TODOs: 
    - first define some actions
    - define a trigger
    - then implement this
  """
  print("Please call Workflow-implement first")
  raise NotImplementedError




"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[]`
the output data of function `action_1` is: `[]`

------------------------
In Function: mainWorkflow
      print("Please call Workflow-implement first")
-->   raise NotImplementedError
------------------------
NotImplementedError: 

You can also see the runnning result for all functions in there comments.
"""