__author__ = 'arobres'

#### AUTHENTICATION ####
#### REQUESTS PROVIDE METHODS TO WORK WITH BASIC AUTHENTICATION, DIGEST AUTHENTICATION AND OAUTH
#### http://docs.python-requests.org/en/latest/user/authentication/

import requests
from nose.tools import assert_equals, assert_true
import ujson

new_json_body = {}
new_json_body['name'] = 'community'
new_json_body['username'] = 'emc2'
new_json_body['password'] = 'easy_pwd'
new_json_body['role'] = 'QA'
new_json_body['email'] = 'emc2@tid.es'
new_json_body = ujson.dumps(new_json_body)

#Send the HTTP Request
response = requests.post(url='http://localhost:8081/v1.0/users', data=new_json_body)

#Assert response
assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
response_body = response.content
assert_equals(response_body, 'user created', 'INCORRECT RESPONSE BODY. RESPONSE OBTAINED IS: {}'.format(response_body))

#WE CAN TRY TO ACCESS TO MY PRIVATE MAILBOX

response = requests.get(url='http://localhost:8081/v1.0/users/inbox/emc2')

#Assert response
assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))

#We obtain a 401 Error Unauthorized and a HTML response. If I try convert the response to JSON...

try:
    json_response = response.json()
    print json_response
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'


#We should use basic authentication.

response = requests.get(url='http://localhost:8081/v1.0/users/inbox/emc2', auth=('emc2', 'easy_pwd'))

#Assert response
assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))

#Now we can try to obtain the JSON response data
try:
    json_response = response.json()
    print json_response
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'

assert_equals(json_response['username'], 'emc2')
assert_equals(json_response['messages'], [])



