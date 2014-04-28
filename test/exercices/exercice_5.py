__author__ = 'arobres'


import requests
from nose.tools import assert_equals, assert_true
import ujson

# SEND MESSAGES TO USER

message_body = {'message': ''}

for index in range(1, 11):

    message_body['message'] = "HELLO I'M THE MESSAGE {}".format(index)
    response = requests.post(url='http://localhost:8081/v1.0/users/inbox/emc2', data=ujson.dumps(message_body))
    assert_true(response.ok, 'BAD REQUEST!, Response obtained is: {} {}'.format(response.status_code, response.content))
    response_body = response.content
    assert_equals(response_body, 'message saved', 'INCORRECT RESPONSE BODY. '
                                                  'RESPONSE OBTAINED IS: {}'.format(response_body))

# GET ALL THE MESSAGES
response = requests.get(url='http://localhost:8081/v1.0/users/inbox/emc2', auth=('emc2', 'easy_pwd'))
assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
try:
    json_response = response.json()
    print json_response
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'

print json_response['username']

print json_response['messages']

#NOW WE CAN DELETE ALL THE MESSAGES

response = requests.delete(url='http://localhost:8081/v1.0/users/inbox/emc2')

assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))

response = requests.delete(url='http://localhost:8081/v1.0/users/inbox/emc2', auth=('emc2', 'easy_pwd'))

assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
assert_equals(response.content, 'messages deleted', response.content)

#WE NEED VERIFY IF ALL THE MESSAGES ARE DELETED
response = requests.get(url='http://localhost:8081/v1.0/users/inbox/emc2', auth=('emc2', 'easy_pwd'))
assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
try:
    json_response = response.json()
    print json_response
except:
    print 'Error: THE RESPONSE NOT HAS JSON FORMAT'

assert_equals(json_response['username'], 'emc2')
assert_equals(json_response['messages'], [])




