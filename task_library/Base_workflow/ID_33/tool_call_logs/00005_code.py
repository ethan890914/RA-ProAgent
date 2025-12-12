"""Function param descriptions: 
This function doesn't need params

This function has been executed for 2 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
None

3.Output:
[{'json': {}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data):
  """
  comments: Manual trigger to start the workflow on demand
  TODOs: 
    - Test the trigger to ensure it fires correctly
  """
  params = {}
  function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
  output_data = function.run(input_data=None, params=params)
  return output_data



"""Function param descriptions: 
0 params["format"]: enum[string] = "metric": Format. The format in which format the data should be returned . Available values:
  0.0 value=="imperial": Imperial. Fahrenheit | miles/hour
  0.1 value=="metric": Metric. Celsius | meter/sec
  0.2 value=="standard": Scientific. Kelvin | meter/sec
1 params["locationSelection"]: enum[string] = "cityName": Location Selection. How to define the location for which to return the weather . Available values:
  1.0 value=="cityName": City Name
  1.1 value=="cityId": City ID
  1.2 value=="coordinates": Coordinates
  1.3 value=="zipCode": Zip Code
2 params["cityName"]: string = "", Required when (locationSelection in ['cityName']), otherwise do not provide: City. The name of the city to return the weather of(berlin,de)
3 params["cityId"]: number = 160001123, Required when (locationSelection in ['cityId']), otherwise do not provide: City ID. The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.
4 params["latitude"]: string = "", Required when (locationSelection in ['coordinates']), otherwise do not provide: Latitude. The latitude of the location to return the weather of(13.39)
5 params["longitude"]: string = "", Required when (locationSelection in ['coordinates']), otherwise do not provide: Longitude. The longitude of the location to return the weather of(52.52)
6 params["zipCode"]: string = "", Required when (locationSelection in ['zipCode']), otherwise do not provide: Zip Code. The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/.(10115,de)
7 params["language"]: string = "": Language. The two letter language code to get your output in (eg. en, de, ...).(en)

This function has been executed for 1 times. Last execution:
1.Status: FunctionExecuteSuccess
2.Input: 
[{'json': {}, 'pairedItem': {'item': 0}}]

3.Output:
[{'json': {'coord': {'lon': 55.3047, 'lat': 25.2582}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 27.96, 'feels_like': 27.77, 'temp_min': 27.14, 'temp_max': 27.96, 'pressure': 1017, 'humidity': 42, 'sea_level': 1017, 'grnd_level': 1017}, 'visibility': 10000, 'wind': {'speed': 5.66, 'deg': 320}, 'clouds': {'all': 0}, 'dt': 1764940466, 'sys': {'type': 1, 'id': 7537, 'country': 'AE', 'sunrise': 1764903017, 'sunset': 1764941328}, 'timezone': 14400, 'id': 292223, 'name': 'Dubai', 'cod': 200}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data):
  """
  comments: Get current weather data for Dubai with metric units
  TODOs: 
    - Test the action to ensure correct weather data is fetched
  """
  params = {'cityName': 'Dubai', 'format': 'metric', 'language': 'en', 'locationSelection': 'cityName'}
  function = transparent_action(integration="openWeatherMap", resource="default", operation="currentWeather")
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
[{'json': {'text': 'Dubai temperature: 27.96 \n wind: 5.66'}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A1PGSJLBB', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764940598.642009', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Dubai temperature: 27.96 \n wind: 5.66', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'eLF4R', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Dubai temperature: 27.96 \n wind: 5.66'}]}]}]}, 'message_timestamp': '1764940598.642009'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data):
  """
  comments: Send a formatted weather message to Slack channel 'weathers' with proper params
  TODOs: 
    - Test sending message to Slack
    - Verify correct message format and delivery
  """
  params = { 'channelId': {'mode': 'name', 'value': 'weathers'},
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
[{'json': {'ok': True, 'channel': 'C0A1PGSJLBB', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764940598.642009', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': 'Dubai temperature: 27.96 \n wind: 5.66', 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'eLF4R', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Dubai temperature: 27.96 \n wind: 5.66'}]}]}]}, 'message_timestamp': '1764940598.642009'}, 'pairedItem': {'item': 0}}]
"""
def mainWorkflow(trigger_input: [{...}]):
    """
    comments: Workflow triggered manually, gets Dubai weather and sends formatted message to Slack channel 'weathers'
    TODOs: 
      - Test complete workflow
      - Handle missing weather data gracefully
    """
    # Step 1: Get manual trigger output
    manual_trigger_output = trigger_0(None)

    # Step 2: Get current weather for Dubai
    weather_output = action_0(manual_trigger_output)

    # Step 3: Extract temperature and wind speed
    weather_json = weather_output[0]['json'] if weather_output else {}
    temp = weather_json.get('main', {}).get('temp', 'unknown')
    wind_speed = weather_json.get('wind', {}).get('speed', 'unknown')

    # Step 4: Format message
    message_text = f"Dubai temperature: {temp} \n wind: {wind_speed}"

    # Step 5: Prepare Slack input data
    slack_input = [{"json": {"text": message_text}}]

    # Step 6: Send message to Slack
    slack_output = action_1(slack_input)

    return slack_output



"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""