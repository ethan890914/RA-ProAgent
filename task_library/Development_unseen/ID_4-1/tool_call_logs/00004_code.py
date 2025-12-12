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
  comments: 定义手动触发器，用户点击后触发整个工作流
  TODOs: 
    - 实现触发器逻辑
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
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 12, 'Business Line': 11, 'Manager': 'cc9008@nyu.edu', 'cost': 50000, 'sales': 10000, 'Description': 'Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 13, 'Business Line': 12, 'Manager': 'cc9008@nyu.edu', 'cost': 30000, 'sales': 5000, 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 14, 'Business Line': 13, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 20000, 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 15, 'Business Line': 14, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7600, 'sales': 8000, 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 16, 'Business Line': 15, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 6000, 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 17, 'Business Line': 16, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 60000, 'sales': 20000, 'Description': 'Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 18, 'Business Line': 17, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 100000, 'sales': 80000, 'Description': 'Online Fitness Coaching & Wellness Apps: Providing tailored workout programs, virtual fitness classes, nutrition planning, and progress tracking through mobile apps.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 19, 'Business Line': 18, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 25000, 'sales': 4000, 'Description': 'Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 20, 'Business Line': 19, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 7500, 'Description': 'IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 21, 'Business Line': 20, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 3000, 'sales': 5000, 'Description': 'Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: 配置Google Sheets读取动作，指定文档ID和表单名称，读取业务流数据
  TODOs: 
    - 测试读取数据是否正确
    - 根据读取结果调整后续处理逻辑
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'sheetName': {'mode': 'id', 'value': 'commercial-long'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Online Fitness Coaching & Wellness Apps: Providing tailored workout programs, virtual fitness classes, nutrition planning, and progress tracking through mobile apps.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices.. '}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Classify this business description as B2B or B2C: Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.. '}]}}]

3.Output:
[{'json': {'choices': [{'text': 'This business description is B2C (Business-to-Consumer), as it involves selling products directly to individual consumers.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2C (Business-to-Consumer) because it provides a service directly to individual consumers who order food for personal consumption.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2C (Business-to-Consumer) because it offers a platform directly to consumers for booking flights, hotels, and other travel-related services.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2C (Business to Consumer) because it focuses on providing personal finance management tools directly to individual users for managing their own finances.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'The business description "Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects" is primarily **B2C (Business to Consumer)**, as it targets individual users seeking to improve their skills and knowledge.\n\nHowever, if the platform also offers corporate training solutions or partners with businesses to provide employee education, it could have a B2B component as well. But based on the given description alone, it is mainly B2C.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it involves providing software solutions specifically designed for other businesses.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it targets enterprises as its customers.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it offers data analytics tools and services specifically aimed at helping other businesses improve their performance.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it involves providing services to other businesses to help them automate tasks and improve efficiency.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it involves providing customized integration solutions to other businesses to improve their systems and communication.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'The business described is primarily B2C (Business-to-Consumer) because it provides services directly to patients, who are individual consumers.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it offers a Learning Management System specifically designed for enterprises to train their employees.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because the software solutions are designed to help companies manage their HR and talent management processes.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is classified as B2B (Business-to-Business). It describes providing tools to businesses rather than directly to individual consumers.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is primarily B2B (Business-to-Business), as it offers digital marketing and social media management tools that are typically used by other businesses to manage their marketing efforts.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'The business description "Subscription-based Digital Content Platforms: Streaming or premium content platforms offering entertainment, news, podcasts, videos, e-books, or exclusive creator content" is primarily **B2C (Business-to-Consumer)**. \n\nThese platforms typically provide content directly to individual consumers who subscribe for personal use.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is primarily B2C (Business-to-Consumer), as it involves providing fitness coaching, wellness apps, and related services directly to individual consumers.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it offers cybersecurity solutions and managed security services specifically for enterprises, which are other businesses.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'The business description "IoT-based Smart Home Solutions: Providing consumers with systems that automate lighting, temperature, home security, and energy usage via connected devices" is classified as **B2C (Business-to-Consumer)**. \n\nThis is because the products and services are directly offered to individual consumers for personal use in their homes.'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'This business description is B2B (Business-to-Business) because it involves providing supply chain and inventory management solutions, which are typically used by other businesses rather than individual consumers.'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: 调用AI完成接口，根据业务描述判断业务流类型
  TODOs: 
    - 构建AI消息格式
    - 测试AI完成结果
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
[{'json': {'businessFlowType': 'to Business', 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Cybersecurity Solutions & Managed Security Services: Offering threat detection, vulnerability scanning, endpoint protection, and incident response services for enterprises.'}}, {'json': {'businessFlowType': 'to Business', 'Description': 'Digital Supply Chain & Inventory Management Platforms: Providing real-time tracking, demand forecasting, supplier coordination, warehouse management, and procurement automation.'}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: 主工作流，触发后读取Google Sheets数据，调用AI判断业务流类型
    TODOs:
      - 测试整体流程
      - 处理异常情况
    """
    # 1. 触发读取Google Sheets数据
    sheet_data = action_0(trigger_input)

    # 2. 构建AI输入，针对每条数据的Description字段构建消息
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        message = f'Classify this business description as B2B or B2C: {description}. '
        ai_input.append({'json': {'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': message}
        ]}})

    # 3. 调用AI完成接口
    ai_output = action_1(ai_input)

    # 4. 解析AI结果，判断业务流类型，只返回'to Business'类型
    results = []
    for i, item in enumerate(ai_output):
        ai_text = item['json']['choices'][0]['text'].strip().lower()
        # 简单判断是否包含'b2b'或'to business'
        if 'b2b' in ai_text or 'to business' in ai_text:
            results.append({'json': {'businessFlowType': 'to Business', 'Description': sheet_data[i]['json'].get('Description', '')}})

    # 5. 返回结果
    return results



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""