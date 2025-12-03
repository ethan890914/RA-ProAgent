"""Function param descriptions: 
This function doesn't need params

This function has been executed for 1 times. Last execution:
1.Status: TriggerAcivatedSuccess
2.Input: 
[]

3.Output:
[{'json': {}}]
"""
def trigger_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Trigger the workflow manually when user clicks the button.
  TODOs: 
    - Test the manual trigger works.
    - Check the output data format.
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
[{'json': {}}]

3.Output:
[{'json': {'coord': {'lon': -97.7431, 'lat': 30.2672}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 11.49, 'feels_like': 10.81, 'temp_min': 10.65, 'temp_max': 12.77, 'pressure': 1017, 'humidity': 81, 'sea_level': 1017, 'grnd_level': 993}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 170}, 'clouds': {'all': 100}, 'dt': 1764778570, 'sys': {'type': 2, 'id': 2105175, 'country': 'US', 'sunrise': 1764767510, 'sunset': 1764804622}, 'timezone': -21600, 'id': 4671654, 'name': 'Austin', 'cod': 200}, 'pairedItem': {'item': 0}}]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Fetch current weather for Austin using cityName and metric units.
  TODOs: 
    - Test the action to verify it returns weather data for Austin.
    - Handle possible errors in fetching data.
  """
  params = {'cityName': 'Austin', 'format': 'metric', 'locationSelection': 'cityName'}
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
[{'json': {'text': "Austin coord: {'lon': -97.7431, 'lat': 30.2672} \n temperature: 11.49 \n visibility: 10000"}}]

3.Output:
[{'json': {'ok': True, 'channel': 'C0A1PGSJLBB', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764778684.181289', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "Austin coord: {'lon': -97.7431, 'lat': 30.2672} \n temperature: 11.49 \n visibility: 10000", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'qmj9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "Austin coord: {'lon': -97.7431, 'lat': 30.2672} \n temperature: 11.49 \n visibility: 10000"}]}]}]}, 'message_timestamp': '1764778684.181289'}, 'pairedItem': {'item': 0}}]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Send a message to Slack channel 'weathers' with the weather information text.
  TODOs: 
    - Test Slack message sending.
    - Verify the message appears in the correct Slack channel.
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
[{'json': {'ok': True, 'channel': 'C0A1PGSJLBB', 'message': {'user': 'U09UT5PE4HZ', 'type': 'message', 'ts': '1764778684.181289', 'bot_id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'text': "Austin coord: {'lon': -97.7431, 'lat': 30.2672} \n temperature: 11.49 \n visibility: 10000", 'team': 'T09VCDJNALR', 'bot_profile': {'id': 'B09V34LF560', 'app_id': 'A09UW3HDF37', 'user_id': 'U09UT5PE4HZ', 'name': 'ProAgentBot', 'icons': {'image_36': 'https://a.slack-edge.com/80588/img/plugins/app/bot_36.png', 'image_48': 'https://a.slack-edge.com/80588/img/plugins/app/bot_48.png', 'image_72': 'https://a.slack-edge.com/80588/img/plugins/app/service_72.png'}, 'deleted': False, 'updated': 1764012858, 'team_id': 'T09VCDJNALR'}, 'blocks': [{'type': 'rich_text', 'block_id': 'qmj9', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': "Austin coord: {'lon': -97.7431, 'lat': 30.2672} \n temperature: 11.49 \n visibility: 10000"}]}]}]}, 'message_timestamp': '1764778684.181289'}, 'pairedItem': {'item': 0}}]
"""
def trigger_0(input_data: list = [{"json": {}}]):
    """
    comments: Trigger the workflow manually when user clicks the button.
    TODOs: 
      - Test the manual trigger works.
      - Check the output data format.
    """
    params = {}
    function = transparent_trigger(integration="manualTrigger", resource="default", operation="default")
    output_data = function.run(input_data=None, params=params)
    return output_data


def action_0(input_data: list):
    """
    comments: Fetch current weather for Austin using cityName and metric units.
    TODOs: 
      - Test the action to verify it returns weather data for Austin.
      - Handle possible errors in fetching data.
    """
    params = {"cityName": "Austin", "format": "metric", "locationSelection": "cityName"}
    function = transparent_action(integration="openWeatherMap", resource="default", operation="currentWeather")
    output_data = function.run(input_data=input_data, params=params)
    return output_data


def action_1(input_data: list):
    """
    comments: Send a message to a Slack channel with the weather information.
    TODOs: 
      - Configure channel parameter to the weather channel.
      - Format the message text with coord, temperature and visibility.
      - Test the Slack message sending.
    """
    params = {"select": "channel", "channelId": {"mode": "name", "value": "weathers"}, "messageType": "text", "text": "={{$json[\"text\"]}}"}
    function = transparent_action(integration="slack", resource="message", operation="post")
    output_data = function.run(input_data=input_data, params=params)
    return output_data


def mainWorkflow(trigger_input: list):
    """
    comments: Workflow to fetch current weather for Austin and send to Slack channel 'weathers'.
    TODOs: 
      - Test the entire workflow end to end.
      - Handle possible errors in API calls.
    """
    # Step 1: Trigger input is not used directly, but passed to action_0
    weather_output = action_0(trigger_input)

    # Step 2: Extract coord, temperature, visibility
    if not weather_output or not weather_output[0].get("json"):
        raise ValueError("No weather data received.")
    weather_json = weather_output[0]["json"]
    coord = weather_json.get("coord")
    main = weather_json.get("main")
    visibility = weather_json.get("visibility")

    if not coord or not main or visibility is None:
        raise ValueError("Missing required weather data fields.")

    temperature = main.get("temp")
    if temperature is None:
        raise ValueError("Temperature data missing.")

    # Step 3: Format message
    message_text = f"Austin coord: {coord} \n temperature: {temperature} \n visibility: {visibility}"

    # Step 4: Prepare Slack input
    slack_input = [{"json": {"text": message_text}}]

    # Step 5: Send to Slack
    slack_output = action_1(slack_input)

    return slack_output




"""

The directly running result for now codes with print results are as following:




You can also see the runnning result for all functions in there comments.
"""