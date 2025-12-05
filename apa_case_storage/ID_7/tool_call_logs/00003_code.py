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
  comments: Manual trigger to start the workflow when user clicks the button.
  TODOs: 
    - Test manual trigger activation.
    - Verify output format.
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'messages': [{'role': 'system', 'content': 'You are a helpful assistant that generates jokes.'}, {'role': 'user', 'content': 'Please generate a joke with more than 100 words but less than 200 words.'}]}}]

3.Output:
[{'json': {'choices': [{'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!'}]}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Generate a joke with more than 100 words but less than 200 words using AI completion.
  TODOs: 
    - Implement specific prompt and parameters.
    - Test joke generation length and quality.
  """
  params = {}
  function = transparent_action(integration="aiCompletion", resource="default", operation="default")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""Function param descriptions: 
0 params["select"]: enum[string] = "", Required: Send Message To(Select...) . Available values:
  0.0 value=="channel": Channel
  0.1 value=="user": User
1 params["channelId"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Required when (select in ['channel']), otherwise do not provide: Channel. The Slack channel to send to(Select a channel...) . "mode" should be one of ['id', 'name', 'url']: 
  1.0 params["channelId"]["value"](when "mode"="id"): string: By ID(C0122KQ70S7E)
  1.1 params["channelId"]["value"](when "mode"="name"): string: By Name(#general)
  1.2 params["channelId"]["value"](when "mode"="url"): string: By URL(https://app.slack.com/client/TS9594PZK/B0556F47Z3A)
2 params["user"]: dict{"mode":enum(str),"values":any} = {'mode': 'list', 'value': ''}, Activate(Not Required) when (select in ['user']), otherwise do not provide: User(Select a user...) . "mode" should be one of ['id', 'username']: 
  ...hidden...
3 params["messageType"]: enum[string] = "text": Message Type. Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more . Available values:
  3.0 value=="text": Simple Text Message. Supports basic Markdown
  3.1 value=="block": Blocks. Combine text, buttons, form elements, dividers and more in Slack 's visual builder
  3.2 value=="attachment": Attachments
4 params["text"]: string = "", Activate(Not Required) when (messageType in ['block']), otherwise do not provide: Notification Text. Fallback text to display in slack notifications. Supports <a href="https://api.slack.com/reference/surfaces/formatting">markdown</a> by default - this can be disabled in "Options".
5 params["blocksUi"]: string = "", Required when (messageType in ['block']), otherwise do not provide: Blocks. Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>
6 params["attachments"]: list[dict] = [{}], Activate(Not Required) when (messageType in ['attachment']), otherwise do not provide: Attachments(Add attachment item) . properties description:
  ...hidden...
7 params["otherOptions"]: dict = {}: Options. Other options to set(Add options) . properties description:
  ...hidden...

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A0X7VLQ9J', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764906903.867109', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'mBB+g', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!'}]}]}]}, 'message_timestamp': '1764906903.867109'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send the generated joke to Slack channel #jokes with proper parameters set.
  TODOs: 
    - Test Slack message delivery.
    - Verify correct channel selection.
  """
  params = { 'channelId': {'mode': 'name', 'value': 'jokes'},
             'messageType': 'text',
             'select': 'channel',
             'text': '={{$json["text"]}}'}
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A0X7VLQ9J', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764906903.867109', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'mBB+g', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Sure! Here’s a joke that’s a bit longer and fits within your word count request:\n\nThere once was a man named Bob who decided to take up gardening. He was so excited to grow his own vegetables that he went to the store, bought all the seeds, tools, and fertilizers he could find, and planted a huge garden in his backyard. Every day, Bob would water his plants, talk to them, and even sing songs to encourage them to grow. One morning, he noticed a little sprout poking through the soil and felt incredibly proud.\n\nWeeks went by, and Bob’s garden flourished—except for one stubborn tomato plant that refused to grow any tomatoes. Frustrated, Bob asked his neighbor, an experienced gardener, for advice. The neighbor looked at the plant and said, “Bob, you’ve been talking to the plants and singing to them, but have you tried telling the tomato plant a joke? Sometimes laughter helps plants grow!”\n\nBob laughed and replied, “Well, I don’t know any tomato jokes.” The neighbor smiled and said, “Alright, here’s one: Why did the tomato turn red? Because it saw the salad dressing!” Bob chuckled, told the joke to the tomato plant, and the next day, to his surprise, the tomato plant had grown a bright, juicy tomato. From then on, Bob made sure to keep the jokes coming—because even plants need a little humor to thrive!'}]}]}]}, 'message_timestamp': '1764906903.867109'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow to generate a joke with AI on manual trigger and send it to Slack #jokes channel.
    TODOs: 
      - Test end-to-end joke generation and sending.
    """
    # Step 1: Build AI input with prompt for joke generation
    ai_input = [{
        "json": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that generates jokes."},
                {"role": "user", "content": "Please generate a joke with more than 100 words but less than 200 words."}
            ]
        }
    }]

    # Step 2: Call aiCompletion action
    ai_output = action_0(ai_input)

    # Step 3: Extract joke text from AI output
    joke_text = ai_output[0]["json"]["choices"][0]["text"]

    # Step 4: Wrap joke text for Slack message
    slack_input = [{"json": {"text": joke_text}}]

    # Step 5: Send joke to Slack #jokes channel
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""