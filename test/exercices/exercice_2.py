import requests
from nose.tools import assert_equals
import ujson

requests.get('http://localhost:8081/v1.0/reset')


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

#DEFINE THE VARIABLES TO BE USED
username = 'vlctesting'
password = 'vlctesting'
message_to_send = 'Hello user! Is your first message!'
create_user_url = 'http://localhost:8081/v1.0/users'
send_message_url = 'http://localhost:8081/v1.0/users/inbox/expoqa'

#DEFINE THE BODY TO CREATE A NEW USER


#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps


#SEND THE POST REQUEST WITH THE BODY CREATED


#ASSERT THE STATUS CODE AND RESPONSE CONTENT
#ASSERT THE RESPONSE CONTENT



'''
THE SECOND PART IS SEND A MESSAGE TO THE USER CREATED
URL: http://localhost:8081/v1.0/users/inbox/{username}
ACTION: POST
THE BODY SHOULD HAVE THE FOLLOWING MANDATORY PARAMETERS: message
ASSERT THE STATUS CODE (200) AND THE CONTENT OF THE MESSAGE (message saved)

'''

#DEFINE THE BODY TO SEND A MESSAGE


#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps


#SEND THE POST REQUEST WITH THE BODY CREATED


#ASSERT THE STATUS CODE AND RESPONSE CONTENT
#ASSERT THE RESPONSE CONTENT



'''
THE LAST PART IS OBTAIN ALL THE MESSAGES FROM THE USER INBOX
URL: http://localhost:8081/v1.0/users/inbox/{username}
ACTION: GET
ASSERT THE STATUS CODE (200), THE NUMBER OF MESSAGES (1) AND THE CONTENT OF THE MESSAGE
REMEBER THAT THIS REQUEST NEEDS AUTHENTICATION
'''


#DEFINE THE AUTHENTICATION TUPLE


#SEND THE GET REQUEST WITH THE AUTHENTICATION


#ASSERT THE STATUS CODE


#CONVERT THE RESPONSE CONTENT TO DICT USING THE FUNCTION .json()


#ASSERT THE USERNAME


#ASSERT THE NUMBER OF MESSAGES


#ASSERT THE MESSAGE RECEIVED

