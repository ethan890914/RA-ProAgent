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

This function has been executed for 10 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'sendTo': 'qwuqwuqwu@gmail.com', 'subject': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'emailType': 'text', 'message': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.\nCategory: Business', 'options': {}}}]

3.Output:
[{'json': {'id': '19ad562ec425a426', 'threadId': '19ad562ec425a426', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]
"""
def action_2(input_data: List[Dict] =  [{...}]):
  """
  comments: Explicitly set Gmail send action parameters with string values from input_data to avoid type issues and fix workflow errors.
  TODOs: 
    - Test sending email with explicit string parameters
    - Verify workflow runs without errors
    - Check email delivery
  """
  params = {
             "sendTo": "=qwuqwuqwu@gmail.com",
             "subject": "={{$json[\"subject\"]}}",
             "emailType": "text",
             "message": "={{$json[\"message\"]}}",
             "options": {}
           }
  function = transparent_action(integration="gmail", resource="message", operation="send")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'index': 1, 'subject': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'status': 'success', 'output': [{'json': {'id': '19ad561842327470', 'threadId': '19ad561842327470', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 2, 'subject': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'status': 'success', 'output': [{'json': {'id': '19ad561ac778a6d8', 'threadId': '19ad561ac778a6d8', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 3, 'subject': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'status': 'success', 'output': [{'json': {'id': '19ad561d9fa7b4f1', 'threadId': '19ad561d9fa7b4f1', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 4, 'subject': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'status': 'success', 'output': [{'json': {'id': '19ad5620378bd2d8', 'threadId': '19ad5620378bd2d8', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 5, 'subject': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'status': 'success', 'output': [{'json': {'id': '19ad5622a50aea1e', 'threadId': '19ad5622a50aea1e', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 6, 'subject': '6. Commercial Entry: Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.', 'status': 'success', 'output': [{'json': {'id': '19ad56250aa65f36', 'threadId': '19ad56250aa65f36', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 7, 'subject': '7. Commercial Entry: Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.', 'status': 'success', 'output': [{'json': {'id': '19ad562794d931b0', 'threadId': '19ad562794d931b0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 8, 'subject': '8. Commercial Entry: Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.', 'status': 'success', 'output': [{'json': {'id': '19ad5629f09bf044', 'threadId': '19ad5629f09bf044', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 9, 'subject': '9. Commercial Entry: Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.', 'status': 'success', 'output': [{'json': {'id': '19ad562c7a5a3fee', 'threadId': '19ad562c7a5a3fee', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}, {'json': {'index': 10, 'subject': '10. Commercial Entry: Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.', 'status': 'success', 'output': [{'json': {'id': '19ad562ec425a426', 'threadId': '19ad562ec425a426', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}]}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to classify commercial entries from Google Sheets and send each classification result via individual Gmail emails with error handling.
    TODOs:
      - Test sending emails individually
      - Improve error handling and logging
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
    gmail_results = []
    for i, item in enumerate(ai_output):
        ai_text = item['json']['choices'][0]['text'].strip() if 'choices' in item['json'] and item['json']['choices'] else ''
        description = sheet_data[i]['json'].get('Description', '')
        subject = f"{i+1}. Commercial Entry: {description}"
        message = f"{i+1}. Commercial Entry: {description}\nCategory: {ai_text}"
        gmail_input = [{
            "json": {
                "sendTo": "qwuqwuqwu@gmail.com",
                "subject": subject,
                "emailType": "text",
                "message": message,
                "options": {}
            }
        }]
        try:
            print(f"Sending email {i+1} with subject: {subject}")
            gmail_output = action_2(gmail_input)
            gmail_results.append({"json": {"index": i+1, "subject": subject, "status": "success", "output": gmail_output}})
        except Exception as e:
            print(f"Error sending email {i+1}: {e}")
            gmail_results.append({"json": {"index": i+1, "subject": subject, "status": "failed", "error": str(e)}})
    
    return gmail_results




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""