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
  comments: Trigger the workflow manually on user click.
  TODOs: 
    - Test trigger functionality
    - Ensure output data format matches expected input for workflow
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
  comments: Read commercial entries from the specified Google Sheet using documentId and sheetName.
  TODOs: 
    - Test reading data from Google Sheets
    - Add error handling if needed
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
[{'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': 'You are a news classifier. Classify as to Business or to Customer.'}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Classify each Description as 'to Business' or 'to Customer' using AI.
  TODOs: 
    - Build messages array for each Description
    - Test AI classification output
  """
  params = {}  # to be Implemented
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
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'emailType': 'text', 'message': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nCategory: Customer', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'emailType': 'text', 'message': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nCategory: Customer', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'emailType': 'text', 'message': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nCategory: Customer', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'emailType': 'text', 'message': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nCategory: Customer', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'emailType': 'text', 'message': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nCategory: Customer', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '6. Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.', 'emailType': 'text', 'message': '6. Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.\nCategory: Business', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '7. Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.', 'emailType': 'text', 'message': '7. Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.\nCategory: Business', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '8. Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.', 'emailType': 'text', 'message': '8. Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.\nCategory: Business', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '9. Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.', 'emailType': 'text', 'message': '9. Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.\nCategory: Business', 'options': {}}}, {'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'emailType': 'text', 'message': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nCategory: Business', 'options': {}}}]

3.Output:
[]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Use dynamic parameters from input_data for sending emails via Gmail, no static params.
  TODOs: 
    - Test sending multiple emails with dynamic content
    - Verify email delivery and correctness
  """
  params = {}
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'error': 'Execution Failed: \nOutput: Problem with execution 745: The workflow has issues and cannot be executed for that reason. Please fix them first.. Aborting.\nThe workflow has issues and cannot be executed for that reason. Please fix them first. (execution 745)\nError executing workflow. See log messages for details.\n\nExecution error:\n====================================\nThe workflow has issues and cannot be executed for that reason. Please fix them first.\nundefined\nWorkflowHasIssuesError: The workflow has issues and cannot be executed for that reason. Please fix them first.\n    at WorkflowExecute.checkForWorkflowIssues (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1382:10)\n    at WorkflowExecute.processRunExecutionData (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1461:8)\n    at WorkflowExecute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:176:15)\n    at ManualExecutionService.runManually (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/manual-execution.service.ts:157:27)\n    at WorkflowRunner.runMainProcess (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:298:53)\n    at WorkflowRunner.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/workflow-runner.ts:175:4)\n    at Execute.run (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/commands/execute.ts:95:23)\n    at CommandRegistry.execute (/Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/src/command-registry.ts:67:4)\n    at /Users/qwuqwuqwu/.nvm/versions/node/v22.21.0/lib/node_modules/n8n/bin/n8n:63:2\nThe workflow has issues and cannot be executed for that reason. Please fix them first.\n'}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to classify commercial entries from Google Sheets and email results using Gmail, with error handling and debug logs.
    TODOs:
      - Test end-to-end workflow
      - Add more detailed error handling if needed
      - Optimize concurrency if needed
    """
    # Step 1: Read commercial entries from Google Sheets
    sheet_data = action_0(trigger_input)
    
    # Step 2: Build aiCompletion input for each Description
    ai_input = []
    for item in sheet_data:
        description = item['json'].get('Description', '')
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as to Business or to Customer."},
            {"role": "user", "content": description}
        ]
        ai_input.append({"json": {"messages": messages}})
    
    # Step 3: Call aiCompletion
    ai_output = action_1(ai_input)
    
    # Step 4: Parse AI output and prepare Gmail input
    gmail_input = []
    for i, item in enumerate(ai_output):
        ai_text = item['json']['choices'][0]['text'].strip() if 'choices' in item['json'] and item['json']['choices'] else ''
        description = sheet_data[i]['json'].get('Description', '')
        subject = f"{i+1}. Commercial Entry: {description}"
        message = f"{i+1}. Commercial Entry: {description}\nCategory: {ai_text}"
        gmail_input.append({
            "json": {
                "sendTo": "qwuqwuqwu@gmail.com",
                "subject": subject,
                "emailType": "text",
                "message": message,
                "options": {}
            }
        })
    
    # Step 5: Send emails with error handling
    try:
        print(f"Sending emails with Gmail input: {gmail_input}")
        gmail_output = action_2(gmail_input)
        print(f"Gmail output: {gmail_output}")
    except Exception as e:
        print(f"Error sending emails: {e}")
        return [{"json": {"error": str(e)}}]
    
    return gmail_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""