__author__ = 'arobres'

import requests
from nose.tools import assert_equals, assert_true
import ujson

#OK WE NOW CAN SEND MESSAGES TO THE FORUM

THEME_LIST = ['Security', 'Development', 'Automation', 'Testing']
message_body = {}
message_body['theme'] = ''
message_body['subject'] = ''
message_body['message'] = ''
print message_body

#CREATE 4 NEW MESSAGES IN FORUM

for message_id in range(0, 4):

    message_body['theme'] = THEME_LIST[message_id]
    message_body['subject'] = 'MESSAGE SUBJECT ID = {}'.format(message_id+1)
    message_body['message'] = 'MESSAGE BODY ID = {}'.format(message_id+1)

    response = requests.post(url='http://localhost:8081/v1.0/forum', data=ujson.dumps(message_body))
    assert_true(response.ok)
    assert_equals(response.content, 'message created')


#WE CAN MAKE A REQUEST TO OBTAIN ALL THE FORUM MESSAGES
response = requests.get(url='http://localhost:8081/v1.0/forum')

assert_true(response.ok)

try:
    json_response = response.json()
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'

print json_response

print json_response['Development']

print json_response['Development'][0]


#THIS API ALLOW HTTP QUERY PARAMETERS TO FILTER BY THEME
#FIRST CREATE A DICT WITH THE FILTER USING THE PATTERN {'key': 'value'}

payload = {'theme': 'Security'}

#AFTER INCLUDE IT IN THE REQUEST
response = requests.get(url='http://localhost:8081/v1.0/forum', params=payload)
print (response.url)

#Verify the response
assert_true(response.ok, response.content)

#Convert to JSON
try:
    json_response = response.json()
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'

print json_response['Security']

print json_response


###### REMEMBER ########
# TO USE QUERY PARAMETERS IN URL DEFINE FIRST ALL THE PARAMETERS IN A DICT AND INTRODUCE IT IN THE REQUEST








