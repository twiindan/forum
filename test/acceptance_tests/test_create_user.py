__author__ = 'arobres'

from commons.rest_utils import RestUtils
from nose.tools import assert_equals, assert_true


class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.api_utils = RestUtils()

    def create_body(self, name=None, username=None, pwd=None, role=None, email=None):

        body = {}
        if name is not None:
            body['name'] =  name
        if username is not None:
            body['username'] = username
        if pwd is not None:
            body['password'] = pwd
        if role is not None:
            body['role'] = role
        if email is not None:
            body['email'] = email

        return body

    def test_create_user_with_all_parameters(self):

        name = 'toni'
        username = 'qaforever'
        pwd = 'easypwd'
        role = 'QA'
        email = 'arobres@tid.es'

        response = self.api_utils.create_user(name=name, username=username, pwd=pwd, role=role, email=email)

        assert_true(response.ok)
        assert_equals(response.content, 'user created')

    def test_create_user_with_none_values(self):

        name = 'toni'
        username = 'hello'
        pwd = 'easypwd'
        role = 'QA'
        email = 'arobres@tid.es'

        response = self.api_utils.create_user(name=name, username=username, pwd=pwd, role=role)

        assert_true(response.ok)
        assert_equals(response.content, 'user created')

    def test_create_user_without_some_parameter(self):

        name = 'toni'
        username = 'qaforever'
        pwd = 'easypwd'
        role = 'QA'
        email = 'arobres@tid.es'

        body = self.create_body(name, username, pwd, role)

        response = self.api_utils.create_user(body=body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

        body = self.create_body(username, pwd, role, email)
        response = self.api_utils.create_user(body=body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_create_user_invalid_json_format(self):

        body = 'hello, is not a JSON'

        response = self.api_utils.create_user(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_not_existant_role(self):

        name = 'toni'
        username = 'qaforever'
        pwd = 'easypwd'
        role = 'tester'
        email = 'arobres@tid.es'

        response = self.api_utils.create_user(name=name, username=username, pwd=pwd, role=role, email=email)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'Role not valid')