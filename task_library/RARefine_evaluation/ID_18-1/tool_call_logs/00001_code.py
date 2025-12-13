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
  comments: Trigger the workflow manually by user clicking the button.
  TODOs: 
    - Test manual trigger activation.
    - Verify trigger output format.
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
[{'json': {'row_number': 2, 'Business Line': 1, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 50000, 'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 3, 'Business Line': 2, 'Manager': 'cc9008@nyu.edu', 'cost': 5000, 'sales': 30000, 'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 4, 'Business Line': 3, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 10000, 'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 5, 'Business Line': 4, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 7600, 'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 6, 'Business Line': 5, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 6000, 'sales': 8000, 'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 7, 'Business Line': 6, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 20000, 'sales': 60000, 'Description': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 8, 'Business Line': 7, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 80000, 'sales': 100000, 'Description': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 9, 'Business Line': 8, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 4000, 'sales': 25000, 'Description': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 10, 'Business Line': 9, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7500, 'sales': 4000, 'Description': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 11, 'Business Line': 10, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 5000, 'sales': 3000, 'Description': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 12, 'Business Line': 11, 'Manager': 'cc9008@nyu.edu', 'cost': 50000, 'sales': 10000, 'Description': 'Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 13, 'Business Line': 12, 'Manager': 'cc9008@nyu.edu', 'cost': 30000, 'sales': 5000, 'Description': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 14, 'Business Line': 13, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 10000, 'sales': 20000, 'Description': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 15, 'Business Line': 14, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 7600, 'sales': 8000, 'Description': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}, 'pairedItem': {'item': 0}}, {'json': {'row_number': 16, 'Business Line': 15, 'Manager': 'qwuqwuqwu@gmail.com', 'cost': 8000, 'sales': 6000, 'Description': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Update Google Sheets read action to use sheetName 'commercial-mid' instead of 'commercial'.
  TODOs: 
    - Test reading sheet data with new sheetName.
    - Verify output schema for further processing.
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'filtersUI': {},
             'options': {},
             'sheetName': {'mode': 'id', 'value': 'commercial-mid'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or 'to Customer'."}, {'role': 'user', 'content': 'Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Use AI to classify each Description as 'to Business' or 'to Customer'.
  TODOs: 
    - Build messages array in workflow.
    - Test AI completion with sample inputs.
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
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
[{'json': {'subject': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'message': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nCategory: to Customer'}}, {'json': {'subject': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'message': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nCategory: to Customer'}}, {'json': {'subject': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'message': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nCategory: to Customer'}}, {'json': {'subject': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'message': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nCategory: to Customer'}}, {'json': {'subject': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'message': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nCategory: to Customer'}}, {'json': {'subject': '6. Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.', 'message': '6. Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nCategory: to Business'}}, {'json': {'subject': '7. Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.', 'message': '7. Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nCategory: to Business'}}, {'json': {'subject': '8. Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.', 'message': '8. Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nCategory: to Business'}}, {'json': {'subject': '9. Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.', 'message': '9. Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nCategory: to Business'}}, {'json': {'subject': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'message': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nCategory: to Business'}}, {'json': {'subject': '11. Commercial Entry: Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.', 'message': '11. Commercial Entry: Digital Health & Telemedicine Platform: Providing patients with online medical consultations, appointment scheduling, electronic prescriptions, and remote health monitoring.\nCategory: to Customer'}}, {'json': {'subject': '12. Commercial Entry: Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.', 'message': '12. Commercial Entry: Online Learning Management System for Enterprises: Offering corporations a customizable LMS to train employees, track progress, and manage compliance certifications.\nCategory: to Business'}}, {'json': {'subject': '13. Commercial Entry: HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.', 'message': '13. Commercial Entry: HR & Talent Management Software: Solutions that help companies with recruitment, onboarding, employee performance management, payroll, and benefits administration.\nCategory: to Business'}}, {'json': {'subject': '14. Commercial Entry: Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.', 'message': '14. Commercial Entry: Customer Relationship Management (CRM) Platforms: Providing businesses with tools to manage sales pipelines, automate marketing campaigns, and enhance customer support.\nCategory: to Business'}}, {'json': {'subject': '15. Commercial Entry: Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.', 'message': '15. Commercial Entry: Digital Marketing & Social Media Management Tools: Offering services for content scheduling, analytics dashboards, ad management, SEO optimization, and influencer tracking.\nCategory: to Business'}}]

3.Output:
[{'json': {'id': '19afb33a04a3b9a7', 'threadId': '19afb33a04a3b9a7', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19afb33a4c944de0', 'threadId': '19afb33a4c944de0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19afb33a8ccbdf7a', 'threadId': '19afb33a8ccbdf7a', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19afb33b090ab589', 'threadId': '19afb33b090ab589', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19afb33b540571d2', 'threadId': '19afb33b540571d2', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}, {'json': {'id': '19afb33b83bb9c78', 'threadId': '19afb33b83bb9c78', 'labelIds': ['SENT']}, 'pairedItem': {'item': 5}}, {'json': {'id': '19afb33bd9b461b5', 'threadId': '19afb33bd9b461b5', 'labelIds': ['SENT']}, 'pairedItem': {'item': 6}}, {'json': {'id': '19afb33c29f2c636', 'threadId': '19afb33c29f2c636', 'labelIds': ['SENT']}, 'pairedItem': {'item': 7}}, {'json': {'id': '19afb33c7b9ffc5f', 'threadId': '19afb33c7b9ffc5f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 8}}, {'json': {'id': '19afb33cd204eaf9', 'threadId': '19afb33cd204eaf9', 'labelIds': ['SENT']}, 'pairedItem': {'item': 9}}, {'json': {'id': '19afb33d055060d3', 'threadId': '19afb33d055060d3', 'labelIds': ['SENT']}, 'pairedItem': {'item': 10}}, {'json': {'id': '19afb33d41d11755', 'threadId': '19afb33d41d11755', 'labelIds': ['SENT']}, 'pairedItem': {'item': 11}}, {'json': {'id': '19afb33dbdcb4c2b', 'threadId': '19afb33dbdcb4c2b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 12}}, {'json': {'id': '19afb33e021f17ce', 'threadId': '19afb33e021f17ce', 'labelIds': ['SENT']}, 'pairedItem': {'item': 13}}, {'json': {'id': '19afb33e5f1c2d2f', 'threadId': '19afb33e5f1c2d2f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 14}}]
"""
def action_2(input_data):
  """
  comments: Send classification results via Gmail to the specified email address with subject and message extracted from input_data.
  TODOs: 
    - Test sending email.
    - Verify email content and recipient.
  """
  params = { 'emailType': 'text',
             'message': '={{$json["message"]}}',
             'options': {},
             'sendTo': 'qwuqwuqwu@gmail.com',
             'subject': '={{$json["subject"]}}'}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'id': '19afb33a04a3b9a7', 'threadId': '19afb33a04a3b9a7', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19afb33a4c944de0', 'threadId': '19afb33a4c944de0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19afb33a8ccbdf7a', 'threadId': '19afb33a8ccbdf7a', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19afb33b090ab589', 'threadId': '19afb33b090ab589', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19afb33b540571d2', 'threadId': '19afb33b540571d2', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}, {'json': {'id': '19afb33b83bb9c78', 'threadId': '19afb33b83bb9c78', 'labelIds': ['SENT']}, 'pairedItem': {'item': 5}}, {'json': {'id': '19afb33bd9b461b5', 'threadId': '19afb33bd9b461b5', 'labelIds': ['SENT']}, 'pairedItem': {'item': 6}}, {'json': {'id': '19afb33c29f2c636', 'threadId': '19afb33c29f2c636', 'labelIds': ['SENT']}, 'pairedItem': {'item': 7}}, {'json': {'id': '19afb33c7b9ffc5f', 'threadId': '19afb33c7b9ffc5f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 8}}, {'json': {'id': '19afb33cd204eaf9', 'threadId': '19afb33cd204eaf9', 'labelIds': ['SENT']}, 'pairedItem': {'item': 9}}, {'json': {'id': '19afb33d055060d3', 'threadId': '19afb33d055060d3', 'labelIds': ['SENT']}, 'pairedItem': {'item': 10}}, {'json': {'id': '19afb33d41d11755', 'threadId': '19afb33d41d11755', 'labelIds': ['SENT']}, 'pairedItem': {'item': 11}}, {'json': {'id': '19afb33dbdcb4c2b', 'threadId': '19afb33dbdcb4c2b', 'labelIds': ['SENT']}, 'pairedItem': {'item': 12}}, {'json': {'id': '19afb33e021f17ce', 'threadId': '19afb33e021f17ce', 'labelIds': ['SENT']}, 'pairedItem': {'item': 13}}, {'json': {'id': '19afb33e5f1c2d2f', 'threadId': '19afb33e5f1c2d2f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 14}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered manually, reads commercial entries from Google Sheets, classifies each Description with AI, and sends each result by Gmail.
    TODOs:
        - Build aiCompletion input messages with system and user prompts.
        - Parse AI output to extract classification.
        - Format and send emails with classification results.
    """
    # Step 1: Trigger input is not used for data, just start
    # Step 2: Read data from Google Sheets
    sheet_data = action_0(trigger_input)
    
    # Step 3: Prepare aiCompletion input
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or 'to Customer'."},
            {"role": "user", "content": description}
        ]
        ai_input.append({"json": {"messages": messages}})
    
    # Step 4: Call aiCompletion action
    ai_output = action_1(ai_input)
    
    # Step 5: Parse aiCompletion output and prepare emails
    email_inputs = []
    for i, (sheet_item, ai_item) in enumerate(zip(sheet_data, ai_output), start=1):
        description = sheet_item['json'].get('Description', '')
        ai_text = ai_item['json'].get('choices', [{}])[0].get('text', '').strip()
        # Extract category from AI text, simplified to look for keywords
        category = 'to Business' if 'business' in ai_text.lower() else 'to Customer'
        subject = f"{i}. Commercial Entry: {description}"
        message = f"{i}. Commercial Entry: {description}\nCategory: {category}"
        email_inputs.append({"json": {"subject": subject, "message": message}})
    
    # Step 6: Send emails via Gmail
    gmail_output = action_2(email_inputs)
    
    return gmail_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""