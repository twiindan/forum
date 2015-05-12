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
        pass

    def test_not_existent_role(self):
        pass

    def test_existent_user(self):
        pass