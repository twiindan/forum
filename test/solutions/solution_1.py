import requests
from nose.tools import assert_equals
import ujson


#MAKE A REQUEST TO PUBLISH A MESSAGE TO THE FORUM
'''
The URL is http://localhost:8081/v1.0/forum
THE BODY SHOULD HAVE THE FOLLOWING MANDATORY PARAMETERS: theme, subject and message
THE THEME SHOULD BE ONE OF THE FOLLOWING OPTIONS:
FORUM_THEMES = Security, Development, Automation, Testing
ASSERT THE STATUS CODE (200) and the response content (message created)
MAKE A GET REQUEST TO OBTAIN ALL THE MESSAGES PUBLISHED IN THE FORUM
'''

url = 'http://localhost:8081/v1.0/forum'

#DEFINE THE BODY IN A DICTIONARY WITH THE PARAMETERS REQUIRED
body = {'theme': 'Testing', 'subject': 'My first request', 'message': "It's my first message in the forum"}

#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps
body = ujson.dumps(body)

#SEND THE POST REQUEST
response = requests.post(url=url, data=body)

#ASSERT THE STATUS CODE
assert_equals(response.status_code, 200)

#ASSERT THE RESPONSE CONTENT
assert_equals(response.content, 'message created')

#SEND A REQUEST TO OBTAIN ALL THE MESSAGES FROM THE FORUM
response = requests.get(url=url)

#ASSERT THE STATUS CODE
assert_equals(response.status_code, 200)

#CONVERT THE RESPONSE CONTENT TO JSON
response_body = response.json()

#ASSERT THE MESSAGE
assert_equals(response_body['Testing'][0]['subject'], 'My first request')
assert_equals(response_body['Testing'][0]['message'], "It's my first message in the forum")

