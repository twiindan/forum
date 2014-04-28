__author__ = 'arobres'

import requests
from nose.tools import assert_equals, assert_true
import ujson

#make a POST request

response = requests.post('http://localhost:8081/v1.0/users')


#Assert response

assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
#We obtain a Assertion Error because server responses with 400 Bad Request


#Inserting data in the POST request
#We need include a JSON with all the data required
"""{'name': <string>,
     'username': <string>,
     'password': <string>,
     'role': <string>,
     'email': <string>
    }
"""

#How we can build JSON?

#First option
body = u"{'name': 'toni', 'username': 'arobres', 'password': 'tid', 'role': 'QA', 'email': 'arobres@tid.es'}'"

print body
print type(body)

string_body = ujson.dumps(body)
print string_body


#It's ok but... one remind...

#JSON can be mapped directly with Dicts in Python
body = {'name': 'toni', 'username': 'antonio_robres', 'password': 'tid', 'role': 'QA', 'email': 'arobres@tid.es'}

print body
print type(body)

dict_body = ujson.dumps(body)
print dict_body


#Another option

new_json_body = {}
new_json_body['name'] = 'toni'
new_json_body['username'] = 'toni'
new_json_body['password'] = 'tid'
new_json_body['role'] = 'QA'
new_json_body['email'] = 'arobres@tid.es'

print new_json_body
new_json_body = ujson.dumps(new_json_body)
print new_json_body

#OK... Now we can do the POST request

response = requests.post(url='http://localhost:8081/v1.0/users', data=new_json_body)

#Assert response

assert_true(response.ok, 'BAD REQUEST!!!!!, Response obtained is: {} {}'.format(response.status_code, response.content))
response_body = response.content

assert_equals(response_body, 'user created', 'INCORRECT RESPONSE BODY. RESPONSE OBTAINED IS: {}'.format(response_body))


#BE CAREFUL WITH THE RESPONSE WHEN TRY TO CONVERT TO JSON:

response_body = response.json()


#### LEARNING BY DOING  ####

#MAKE A REQUEST TO PUBLISH A MESSAGE TO THE FORUM