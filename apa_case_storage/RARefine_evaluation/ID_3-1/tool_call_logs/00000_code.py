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

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 12, 'Business Line': 11, 'Manager': 'cc9008@nyu.edu', 'cost': 50000, 'sales': 10000, 'Description': 'Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 13, 'Business Line': 12, 'Manager': 'cc9008@nyu.edu', 'cost': 30000, 'sales': 5000, 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 14, 'Business Line': 13, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 20000, 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 15, 'Business Line': 14, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7600, 'sales': 8000, 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 16, 'Business Line': 15, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 6000, 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 17, 'Business Line': 16, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 60000, 'sales': 20000, 'Description': 'Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 18, 'Business Line': 17, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 100000, 'sales': 80000, 'Description': 'Online Fitness Coaching & Wellness Apps: Providing tailored workout programs, virtual fitness classes, nutrition planning, and progress tracking through mobile apps.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 19, 'Business Line': 18, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 25000, 'sales': 4000, 'Description': 'Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 20, 'Business Line': 19, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 7500, 'Description': 'IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 21, 'Business Line': 20, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 3000, 'sales': 5000, 'Description': 'Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: 更新Google Sheets读取参数，sheetName改为'commercial-long'以匹配新需求。
  TODOs: 
    - 测试Google Sheets读取数据是否正确
    - 确认sheetName参数生效
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'commercial-long'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Online Fitness Coaching & Wellness Apps: Providing tailored workout programs, virtual fitness classes, nutrition planning, and progress tracking through mobile apps., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'Based on the description: {{$json.Description}}, classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}, {'role': 'user', 'content': 'Based on the description: Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation., classify this business as either to B (business-to-business) or to C (business-to-consumer). Respond with only: to B or to C'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to C'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to B'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 调用AI完成节点，基于输入的messages进行业务流类型分类。
  TODOs: 
    - 完善AI调用参数
    - 测试AI分类功能
    - 确保参数格式正确
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
[{'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 13, 'Business Line': 12, 'Manager': 'cc9008@nyu.edu', 'cost': 30000, 'sales': 5000, 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 14, 'Business Line': 13, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 20000, 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 15, 'Business Line': 14, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7600, 'sales': 8000, 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 16, 'Business Line': 15, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 6000, 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 19, 'Business Line': 18, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 25000, 'sales': 4000, 'Description': 'Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 21, 'Business Line': 20, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 3000, 'sales': 5000, 'Description': 'Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.'}, 'pairedItem': {'item': 0}}]
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
    """

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




You can also see the runnning result for all functions in there comments.
"""