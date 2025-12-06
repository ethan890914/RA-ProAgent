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
  comments: 手动触发器，作为工作流的入口，触发后执行后续动作。
  TODOs: 
    - 测试触发器是否能正常触发
    - 确保触发器输出格式符合预期
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
  comments: 配置Google Sheets读取参数，指定文档ID和表名，读取商业流程数据。
  TODOs: 
    - 测试读取数据是否正确
    - 确认数据格式符合预期
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Online Fitness Coaching & Wellness Apps: Providing tailored workout programs, virtual fitness classes, nutrition planning, and progress tracking through mobile apps., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices., classify this business as either 'to Business' or 'to Customer'."}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': "Based on the description: Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation., classify this business as either 'to Business' or 'to Customer'."}]}}]

3.Output:
[{'json': {'choices': [{'text': "The described business, an E-commerce Marketplace where consumers purchase products from various brands and sellers, is classified as 'to Customer' (B2C)."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business is classified as 'to Customer' (B2C), as it provides a service directly to individual consumers."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "The business described is a 'to Customer' (B2C) business, as it offers travel booking services directly to individual consumers."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business would be classified as 'to Customer' (B2C), as it provides personal finance management tools directly to individual users."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business would be classified as 'to Customer' (B2C), as it offers online courses and educational resources directly to individual users seeking to enhance their skills and knowledge."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business should be classified as 'to Business' (B2B) since it provides software solutions tailored for businesses."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'The business described as offering "Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently" is classified as **to Business** (B2B).'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "The business described is classified as 'to Business' (B2B) because it offers data analytics and business intelligence solutions aimed at helping other businesses improve their performance."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business falls under the category "to Business" (B2B) because it provides automation services aimed at helping other businesses improve their operations.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business should be classified as 'to Business' (B2B) because it offers customized integration solutions aimed at helping other businesses connect their systems and applications."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business is classified as 'to Customer' (B2C) because it provides medical consultations and health services directly to individual patients."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business should be classified as 'to Business' (B2B), as it offers an LMS specifically designed for corporations to train employees and manage compliance."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business would be classified as 'to Business' (B2B) because HR & Talent Management Software is typically sold to companies and organizations rather than individual consumers."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "The business described is classified as 'to Business' (B2B), since CRM platforms are typically provided to other businesses to help them manage their sales, marketing, and customer support."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business is classified as 'to Business' (B2B) because it offers digital marketing and social media management tools typically used by other businesses to manage their marketing efforts."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business would be classified as 'to Customer' (B2C), as subscription-based digital content platforms primarily target individual consumers."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business would be classified as 'to Customer' (B2C), as it provides fitness coaching and wellness services directly to individual users through mobile apps."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business should be classified as 'to Business' (B2B) because it offers cybersecurity solutions and managed security services typically targeted at enterprises rather than individual consumers."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business is classified as 'to Customer' (B2C) because it provides smart home solutions directly to individual consumers for personal use."}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': "This business is classified as 'to Business' (B2B) because it provides platforms and services aimed at other businesses for managing supply chains and inventory."}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 调用AI完成节点，根据Description字段判断业务类型。
  TODOs: 
    - 构造正确的messages参数
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
[{'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 13, 'Business Line': 12, 'Manager': 'cc9008@nyu.edu', 'cost': 30000, 'sales': 5000, 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 14, 'Business Line': 13, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 20000, 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 15, 'Business Line': 14, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7600, 'sales': 8000, 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 16, 'Business Line': 15, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 6000, 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 19, 'Business Line': 18, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 25000, 'sales': 4000, 'Description': 'Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 21, 'Business Line': 20, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 3000, 'sales': 5000, 'Description': 'Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 根据触发器启动，读取谷歌表格数据，调用AI判断业务类型，并筛选'to Business'类型。
    TODOs: 
      - 验证Google Sheets读取是否成功
      - 构造AI输入的messages字段
      - 解析AI返回结果
      - 返回筛选后的业务类型为'to Business'的数据
    """
    # Step 1: 读取Google Sheets数据
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        return []

    # Step 2: 构造AI输入
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the description: {description}, classify this business as either 'to Business' or 'to Customer'."}
        ]
        ai_input.append({"json": {"messages": messages}})

    # Step 3: 调用AI完成节点
    ai_output = action_1(ai_input)

    # Step 4: 解析AI结果，并筛选'to Business'的条目
    filtered_results = []
    for i, ai_item in enumerate(ai_output):
        ai_text = ai_item['json']['choices'][0]['text'].strip().lower()
        if 'to business' in ai_text:
            filtered_results.append(sheet_data[i])

    return filtered_results



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""