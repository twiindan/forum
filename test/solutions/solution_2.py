import requests
from nose.tools import assert_equals
import ujson


'''
E2E SCENARIO
CREATE A USER
SEND A MESSAGE TO THE USER
OBTAIN ALL USER MESSAGES (YOU NEED AUTHENTICATION)
'''

'''
FIRST WE NEED CREATE THE USER
URL: http://localhost:8081/v1.0/users
ACTION: POST
THE BODY SHOULD HAVE THE FOLLOWING MANDATORY PARAMETERS: name, username, password, role, email
THE ROLE SHOULD BE ONE OF THE FOLLOWING OPTIONS: QA, DEVELOPER, MANAGER
ASSERT THE STATUS CODE (200) and the response content (user created)
'''

requests.get('http://localhost:8081/v1.0/reset')


#DEFINE THE VARIABLES TO BE USED
username = 'vlctesting'
password = 'vlctesting'
message_to_send = 'Hello user! Is your first message!'
create_user_url = 'http://localhost:8081/v1.0/users'
send_message_url = 'http://localhost:8081/v1.0/users/inbox/vlctesting'

#DEFINE THE BODY TO CREATE A NEW USER
user_body = {'name': 'vlc', 'username': username, 'password': password, 'role': 'QA', 'email': 'contact@vlctesting.com'}

#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps
user_body = ujson.dumps(user_body)

#SEND THE POST REQUEST WITH THE BODY CREATED
response = requests.post(url=create_user_url, data=user_body)

#ASSERT THE STATUS CODE AND RESPONSE CONTENT
#ASSERT THE RESPONSE CONTENT
assert_equals(response.status_code, 200)
assert_equals(response.content, 'user created')

'''
THE SECOND PART IS SEND A MESSAGE TO THE USER CREATED
URL: http://localhost:8081/v1.0/users/inbox/{username}
ACTION: POST
THE BODY SHOULD HAVE THE FOLLOWING MANDATORY PARAMETERS: message
ASSERT THE STATUS CODE (200) AND THE CONTENT OF THE MESSAGE (message saved)

'''

#DEFINE THE BODY TO SEND A MESSAGE
message_body = {'message': message_to_send}

#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps
message_body = ujson.dumps(message_body)

#SEND THE POST REQUEST WITH THE BODY CREATED
response = requests.post(url=send_message_url, data=message_body)

#ASSERT THE STATUS CODE AND RESPONSE CONTENT
#ASSERT THE RESPONSE CONTENT
assert_equals(response.status_code, 200)
assert_equals(response.content, 'message saved')


'''
THE LAST PART IS OBTAIN ALL THE MESSAGES FROM THE USER INBOX
URL: http://localhost:8081/v1.0/users/inbox/{username}
ACTION: GET
ASSERT THE STATUS CODE (200), THE NUMBER OF MESSAGES (1) AND THE CONTENT OF THE MESSAGE
REMEBER THAT THIS REQUEST NEEDS AUTHENTICATION
'''


#DEFINE THE AUTHENTICATION TUPLE
auth = (username, password)

#SEND THE GET REQUEST WITH THE AUTHENTICATION 
response = requests.get(url=send_message_url, auth=auth)

#ASSERT THE STATUS CODE
assert_equals(response.status_code, 200)

#CONVERT THE RESPONSE CONTENT TO DICT USING THE FUNCTION .json()
response_body = response.json()

#ASSERT THE USERNAME
assert_equals(response_body['username'], username)

#ASSERT THE NUMBER OF MESSAGES
assert_equals(len(response_body['messages']), 1)

#ASSERT THE MESSAGE RECEIVED
assert_equals(response_body['messages'][0]['message'], message_to_send)
