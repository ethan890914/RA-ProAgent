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
  comments: Trigger when the user manually triggers the workflow.
  TODOs: 
    - Test the manual trigger.
    - Ensure it activates the mainWorkflow correctly.
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_0(input_data: List[Dict] =  [{...}]):
  """
  comments: Get current weather data from OpenWeatherMap for New York using cityName and metric units.
  TODOs: 
    - Test the weather data retrieval for New York.
    - Ensure the output contains temperature and wind data for further processing.
  """
  params = {'cityName': 'New York', 'format': 'metric', 'language': 'en', 'locationSelection': 'cityName'}
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

This function has been executed for 0 times. Last execution:
1.Status: DidNotBeenCalled
2.Input: 
[]

3.Output:
[]
"""
def action_1(input_data: List[Dict] =  [{...}]):
  """
  comments: Send formatted weather message to Slack channel #weathers.
  TODOs: 
    - Set channel to #weathers.
    - Format message with temperature and wind.
    - Test message sending.
  """
  params = {}  # to be Implemented
  function = transparent_action(integration="slack", resource="message", operation="post")
  output_data = function.run(input_data=input_data, params=params)
  return output_data



"""

This function has been executed for 1 times. Last execution:
1.Status: ErrorRaisedHere
2.Input: 
[{'json': {}}]

3.Output:
[]
"""

def mainWorkflow(trigger_input: [{...}]):
  """
  comments: You need to give comments when implementing mainWorkflow
  TODOs: 
    - first define some actions
    - define a trigger
    - then implement this
  """
  print("Please call Workflow-implement first")
  raise NotImplementedError




"""

The directly running result for now codes with print results are as following:


Note: if there is 'KeyError' in the error message, it may be due to the wrong usage of output data. The output data info may help you: 
[Output Data Info]
the output data of function `trigger_0` is: `[{'json': {}}]`
the output data of function `action_0` is: `[]`
the output data of function `action_1` is: `[]`

------------------------
In Function: mainWorkflow
      print("Please call Workflow-implement first")
-->   raise NotImplementedError
------------------------
NotImplementedError: 

You can also see the runnning result for all functions in there comments.
"""