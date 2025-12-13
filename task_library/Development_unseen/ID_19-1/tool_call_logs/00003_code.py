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
  comments: Trigger the workflow manually.
  TODOs: 
    - Test the manual trigger.
    - Ensure it activates the main workflow.
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
def action_0(input_data):
  """
  comments: Read all rows from the specified Google Sheet and sheetName 'commercial' with given documentId.
  TODOs: 
    - Test reading data from the Google Sheet.
    - Verify output contains commercial entries.
  """
  params = { 'documentId': {'mode': 'id', 'value': '1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c'},
             'sheetName': {'mode': 'id', 'value': 'commercial'}}
  function = transparent_action(integration="googleSheets", resource="sheet", operation="read")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Enterprise SaaS Solutions: Providing tailored software solutions for businesses to streamline operations and enhance productivity.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Cloud Infrastructure Services: Offering scalable and secure cloud computing solutions for enterprises to manage their data and applications efficiently.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Data Analytics and Business Intelligence Solutions: Offering advanced data analytics tools and services to help businesses make informed decisions and improve their overall performance.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Business Process Automation Services: Helping businesses automate repetitive tasks and streamline their workflow to improve overall efficiency and reduce operational costs.'}]}}, {'json': {'messages': [{'role': 'system', 'content': "You are a news classifier. Classify as 'to Business' or to 'Customer'."}, {'role': 'user', 'content': 'Customized Enterprise Integration Solutions: Offering tailored integration solutions to help businesses connect various systems and applications seamlessly for improved data flow and communication.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Customer'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}, {'json': {'choices': [{'text': 'to Business'}]}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Use AI to classify each commercial entry Description as 'to Business' or 'to Customer'.
  TODOs: 
    - Build messages array input in the workflow.
    - Test AI classification.
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
[{'json': {'Description': 'E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.', 'category': 'to Customer', 'index': 1, 'text': '1. Commercial Entry: E-commerce Marketplace: Operating an online platform for consumers to purchase a wide range of products from various brands and sellers.\nCategory: to Customer', 'subject': 'Commercial Entry Classification 1'}}, {'json': {'Description': 'Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.', 'category': 'to Customer', 'index': 2, 'text': '2. Commercial Entry: Online Food Delivery Service: Offering a convenient platform for consumers to order food from local restaurants and get it delivered to their doorstep.\nCategory: to Customer', 'subject': 'Commercial Entry Classification 2'}}, {'json': {'Description': 'Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.', 'category': 'to Customer', 'index': 3, 'text': '3. Commercial Entry: Online Travel Booking Portal: Offering a comprehensive platform for consumers to book flights, hotels, and other travel-related services conveniently.\nCategory: to Customer', 'subject': 'Commercial Entry Classification 3'}}, {'json': {'Description': 'Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.', 'category': 'to Customer', 'index': 4, 'text': '4. Commercial Entry: Online Personal Finance Management Tools: Providing users with intuitive tools and resources to manage their personal finances, track expenses, and create budgets.\nCategory: to Customer', 'subject': 'Commercial Entry Classification 4'}}, {'json': {'Description': 'Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.', 'category': 'to Customer', 'index': 5, 'text': '5. Commercial Entry: Online Education and E-learning Platform: Offering a variety of online courses and educational resources for users to enhance their skills and knowledge in various subjects.\nCategory: to Customer', 'subject': 'Commercial Entry Classification 5'}}]

3.Output:
[{'json': {'id': '19af63768c5f4a36', 'threadId': '19af63768c5f4a36', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19af6376c4a50d9d', 'threadId': '19af6376c4a50d9d', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19af637732982b1f', 'threadId': '19af637732982b1f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19af63776f63a8d0', 'threadId': '19af63776f63a8d0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19af6377c62da3df', 'threadId': '19af6377c62da3df', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def action_2(input_data):
  """
  comments: Send email with Gmail containing the classification results, set recipient, subject, and message from input data.
  TODOs: 
    - Test sending email after setting parameters.
    - Verify emails are sent only for 'to Customer' entries.
  """
  params = { 'emailType': 'text',
             'message': '={{$json["text"]}}',
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
[{'json': {'id': '19af63768c5f4a36', 'threadId': '19af63768c5f4a36', 'labelIds': ['SENT']}, 'pairedItem': {'item': 0}}, {'json': {'id': '19af6376c4a50d9d', 'threadId': '19af6376c4a50d9d', 'labelIds': ['SENT']}, 'pairedItem': {'item': 1}}, {'json': {'id': '19af637732982b1f', 'threadId': '19af637732982b1f', 'labelIds': ['SENT']}, 'pairedItem': {'item': 2}}, {'json': {'id': '19af63776f63a8d0', 'threadId': '19af63776f63a8d0', 'labelIds': ['SENT']}, 'pairedItem': {'item': 3}}, {'json': {'id': '19af6377c62da3df', 'threadId': '19af6377c62da3df', 'labelIds': ['SENT']}, 'pairedItem': {'item': 4}}]
"""
def mainWorkflow(trigger_input):
    """
    comments: Main workflow to classify commercial entries from Google Sheets and send emails for 'to Customer' entries.
    TODOs:
      - Test end to end workflow
      - Validate AI classification parsing
      - Validate email sending
    """
    # Step 1: Trigger input ignored, start with reading Google Sheets
    sheet_data = action_0(trigger_input)
    if not sheet_data:
        return []

    # Step 2: Build AI input for each Description
    ai_input = []
    descriptions = []
    for item in sheet_data:
        desc = item['json'].get('Description', '')
        if desc.strip() == '':
            continue
        descriptions.append(desc)
        messages = [
            {"role": "system", "content": "You are a news classifier. Classify as 'to Business' or to 'Customer'."},
            {"role": "user", "content": desc}
        ]
        ai_input.append({"json": {"messages": messages}})

    if not ai_input:
        return []

    # Step 3: Call AI completion
    ai_output = action_1(ai_input)

    # Step 4: Parse AI output and filter only 'to Customer'
    emails_to_send = []
    for idx, (item, ai_item) in enumerate(zip(sheet_data, ai_output), start=1):
        ai_text = ai_item['json']['choices'][0]['text'].strip().lower()
        # Simple classification
        if 'to customer' in ai_text:
            desc = item['json'].get('Description', '')
            category = 'to Customer'
            email_text = f"{idx}. Commercial Entry: {desc}\nCategory: {category}"
            emails_to_send.append({
                "json": {
                    "Description": desc,
                    "category": category,
                    "index": idx,
                    "text": email_text,
                    "subject": f"Commercial Entry Classification {idx}"
                }
            })

    # Step 5: Send emails
    if emails_to_send:
        email_outputs = action_2(emails_to_send)
        return email_outputs
    else:
        return []



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""