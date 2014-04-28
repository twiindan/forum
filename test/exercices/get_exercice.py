__author__ = 'arobres'

import requests
from nose.tools import assert_equals, assert_true

def example_get():

    response = requests.get('http://localhost:8081/v1.0')
    status_code = response.status_code
    print "RESPONSE STATUS CODE: {}".format(status_code)

    assert_true(response.ok, 'BAD REQUEST!!!!!!')
    assert_equals(status_code, 200, 'INCORRECT STATUS CODE. STATUS CODE OBTAINED IS: {}'.format(status_code))

    text_body = response.text
    print "RESPONSE BODY: {}".format(text_body)

    json_body = response.json()
    print "JSON RESPONSE BODY: {}".format(json_body)
    print "JSON RESPONSE IS A: {}".format(type(json_body))

    assert_equals(json_body['product'], 'forum', 'PRODUCT IS NOT CORRECT')
    assert_equals(json_body['version'], '2.0', 'VERSION IS NOT CORRECT')

    response_header = response.headers
    print "RESPONSE HEADER: {}".format(response_header)

    print "CONTENT-TYPE HEADER: {}".format(response_header['content-type'])
    assert response_header['content-type'] == 'application/json'

    response = requests.post('http://localhost:8081/v1.0')
    status_code = response.status_code
    print "RESPONSE STATUS CODE: {}".format(status_code)

    assert_equals(status_code, 405, 'INCORRECT STATUS CODE. STATUS CODE OBTAINED IS: {}'.format(status_code))

if __name__ == "__main__":
    example_get()

