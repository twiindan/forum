__author__ = 'arobres'

from commons.rest_utils import RestUtils
from commons.body_builders import create_user_body, create_default_user
from commons.utils import delete_keys_from_dict
from commons.constants import NAME, USERNAME
from nose.tools import assert_equals, assert_true


class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.api_utils = RestUtils()

    def test_create_user_with_all_parameters(self):

        response = self.api_utils.create_user(body=create_default_user())

        assert_true(response.ok)
        assert_equals(response.content, 'user created')

    def test_create_user_with_none_values(self):

        name = None
        username = 'hello'
        pwd = 'easypwd'
        role = 'QA'
        email = 'arobres@tid.es'

        request_body = create_user_body(name=name, username=username, pwd=pwd, role=role, email=email)

        response = self.api_utils.create_user(body=request_body)

        assert_true(response.ok)
        assert_equals(response.content, 'user created')

    def test_create_user_without_some_parameter(self):


        request_body = create_default_user()
        request_body = delete_keys_from_dict(request_body, NAME)

        response = self.api_utils.create_user(body=request_body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

        request_body = create_default_user()
        request_body = delete_keys_from_dict(request_body, USERNAME)

        response = self.api_utils.create_user(body=request_body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_create_user_invalid_json_format(self):

        body = 'hello, is not a JSON'

        response = self.api_utils.create_user(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_not_existent_role(self):

        name = 'toni'
        username = 'qaforever'
        pwd = 'easypwd'
        role = 'tester'
        email = 'arobres@tid.es'

        request_body = create_user_body(name=name, username=username, pwd=pwd, role=role, email=email)

        response = self.api_utils.create_user(body=request_body)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'Role not valid')

    def test_existent_user(self):

        response = self.api_utils.create_user(body=create_default_user())

        assert_equals(response.status_code, 409)

        response_body = response.json()
        assert_equals(response_body['message'], 'User exist!')

