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
  comments: Trigger the workflow manually by user clicking a button.
  TODOs: 
    - Test the trigger with a manual click.
    - Ensure output data format is correct.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["messages"]: string = "", Required: messages. Set system and user prompts here. An Example:{"messages": [{"role": "system","content": "Please say hello to user."}, {"role": "user","content": "Hello!"}]}

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Generate a joke that is more than 100 words but less than 200 words.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Generate a joke with length between 100 and 200 words using AI completion. The prompt is provided in the workflow input_data, so params is empty.
  TODOs: 
    - Set the prompt to generate a joke with specified length in workflow mainWorkflow.
    - Test the joke generation output.
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["select"]: enum[string] = "", Required: Send Message To(Select...) . Available values:
  0.0 value=="channel": Channel
  0.1 value=="user": User
1 params["channelId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required: Channel. The Slack channel to send to(Select a channel...) . "mode" should be one of ['id', 'name', 'url']: 
  1.0 params["channelId"]["value"](when "mode"="id"): string: By ID(C0122KQ70S7E)
  1.1 params["channelId"]["value"](when "mode"="name"): string: By Name(#general)
  1.2 params["channelId"]["value"](when "mode"="url"): string: By URL(https://app.slack.com/client/TS9594PZK/B0556F47Z3A)
2 params["user"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}: User(Select a user...) . "mode" should be one of ['id', 'username']: 
  ...hidden...
3 params["messageType"]: enum[string] = "text": Message Type. Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more . Available values:
  3.0 value=="text": Simple Text Message. Supports basic Markdown
  3.1 value=="block": Blocks. Combine text, buttons, form elements, dividers and more in Slack 's visual builder
  3.2 value=="attachment": Attachments
4 params["text"]: string = "": Notification Text. Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options".
5 params["blocksUi"]: string = "", Required: Blocks. Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>
6 params["attachments"]: list[dict] = [{}]: Attachments(Add attachment item) . properties description:
  ...hidden...
7 params["otherOptions"]: dict = {}: Options. Other options to set(Add options) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'select': 'channel', 'channelId': {'mode': 'name', 'value': 'jokes'}, 'messageType': 'text', 'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A0X7VLQ9J', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764604984.408729', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '//p', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!'}]}]}]}, 'message_timestamp': '1764604984.408729'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Send the generated joke to the Slack #jokes channel with correct parameters.
  TODOs: 
    - Test sending message to Slack.
    - Verify the Slack channel is correctly set to #jokes.
  """
  params = {
             "select": "channel",
             "channelId": {
               "mode": "name",
               "value": "jokes"
             },
             "messageType": "text",
             "text": "={{$json[\"text\"]}}"
           }
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A0X7VLQ9J', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764604984.408729', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': '//p', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a joke that’s between 100 and 200 words:\n\nA man walks into a library, approaches the librarian, and says, “I’d like a book on how to make friends.” The librarian smiles and hands him a thick volume. The man takes it home, reads it cover to cover, but still struggles to make friends. So, the next day, he returns to the library and says, “I need a book on how to be confident.” The librarian hands him another book. He reads it, but still feels shy at parties. On his third visit, he asks for a book on how to tell jokes. The librarian gives him a comedy book. He reads it, but when he tries to tell a joke, no one laughs. Frustrated, he asks the librarian, “Do you have a book on how to understand librarians?” The librarian replies, “Sure, but it’s in the fiction section—because anyone who understands librarians is living in a fantasy world!” The man laughs, finally making a friend — the librarian!'}]}]}]}, 'message_timestamp': '1764604984.408729'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered manually, generates a joke using AI completion, and sends it to Slack #jokes channel.
    TODOs:
      - Test the end-to-end workflow.
      - Handle empty AI output gracefully.
    """
    # Step 1: Build AI input for joke generation
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Generate a joke that is more than 100 words but less than 200 words."}
            ]
        }
    }]

    # Step 2: Call AI completion action
    ai_output = action_0(ai_input)

    # Step 3: Extract joke text from AI output
    if not ai_output or not ai_output[0]["json"].get("choices"):
        joke_text = "Sorry, I couldn't generate a joke at this time."
    else:
        joke_text = ai_output[0]["json"]["choices"][0]["text"].strip()

    # Step 4: Prepare Slack input
    slack_input = [{
        "json": {
            "select": "channel",
            "channelId": {"mode": "name", "value": "jokes"},
            "messageType": "text",
            "text": joke_text
        }
    }]

    # Step 5: Call Slack action to send the joke
    slack_output = action_1(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""