__author__ = 'arobres'

import requests
from nose.tools import assert_equals, assert_true


#Make a GET request to the forum server

response = requests.get('http://localhost:8081/v1.0')


#get the response status code

status_code = response.status_code
print "RESPONSE STATUS CODE: {}".format(status_code)


#verify the response status code

assert_true(response.ok, 'BAD REQUEST!!!!!!')
assert_equals(status_code, 200, 'INCORRECT STATUS CODE. STATUS CODE OBTAINED IS: {}'.format(status_code))


#Save the body obtained in the response in a <string>

text_body = response.text
print "RESPONSE BODY: {}".format(text_body)
print "RESPONSE BODY IS A: {}".format(type(text_body))


#Save the body obtained in the response in a <dict>

json_body = response.json()
print "JSON RESPONSE BODY: {}".format(json_body)
print "JSON RESPONSE IS A: {}".format(type(json_body))


#Get the response body values and verify it

assert_equals(json_body['product'], 'forum', 'PRODUCT IS NOT CORRECT')
assert_equals(json_body['version'], '2.0', 'VERSION IS NOT CORRECT')


#Get the response headers

response_header = response.headers
print "RESPONSE HEADER: {}".format(response_header)


#Get the content-type response header

print "CONTENT-TYPE HEADER: {}".format(response_header['content-type'])
assert response_header['content-type'] == 'application/json'


#Make a POST request to the forum server without content

response = requests.post('http://localhost:8081/v1.0')
status_code = response.status_code
print "RESPONSE STATUS CODE: {}".format(status_code)


#Verify the status code

assert_equals(status_code, 405, 'INCORRECT STATUS CODE. STATUS CODE OBTAINED IS: {}'.format(status_code))


#Verify an incorrect status code

assert_equals(status_code, 200, 'INCORRECT STATUS CODE. STATUS CODE OBTAINED IS: {}'.format(status_code))
