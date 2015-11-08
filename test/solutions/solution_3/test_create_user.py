__author__ = 'arobres'

from rest_utils import RestUtils
from nose.tools import assert_equals, assert_true


def create_user_body(name=None, username=None, pwd=None, role=None, email=None):

    body = {}
    body['name'] = name
    body['username'] = username
    body['password'] = pwd
    body['role'] = role
    body['email'] = email

    return body


class TestCreateUser():

    @classmethod
    def setup_class(self):

        self.api_utils = RestUtils()

    def test_create_user_with_all_parameters(self):

        name = 'vlc'
        username = 'hello'
        pwd = 'easypwd'
        role = 'QA'
        email = 'vlc@vlc.es'

        request_body = create_user_body(name=name, username=username, pwd=pwd, role=role, email=email)
        print request_body
        response = self.api_utils.create_user(body=request_body)

        assert_true(response.ok)
        assert_equals(response.content, 'user created')

    def test_not_existent_role(self):

        name = 'toni'
        username = 'qaforever'
        pwd = 'easypwd'
        role = 'tester'
        email = 'vlc@vlc.es'

        request_body = create_user_body(name=name, username=username, pwd=pwd, role=role, email=email)

        response = self.api_utils.create_user(body=request_body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'Role not valid')

    def test_existent_user(self):

        name = 'vlc'
        username = 'hello'
        pwd = 'easypwd'
        role = 'QA'
        email = 'vlc@vlc.es'

        request_body = create_user_body(name=name, username=username, pwd=pwd, role=role, email=email)

        response = self.api_utils.create_user(body=request_body)

        assert_equals(response.status_code, 409)

        response_body = response.json()
        assert_equals(response_body['message'], 'User exist!')
