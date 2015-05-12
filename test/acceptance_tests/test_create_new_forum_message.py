__author__ = 'arobres'

from commons.rest_utils import RestUtils
from commons.utils import assert_json_format, delete_keys_from_dict
from commons.constants import THEME, MESSAGES, FORUM_KEYS
from commons.body_builders import create_default_forum_message_body

from nose.tools import assert_equals, assert_true



class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.api_utils = RestUtils()

    def test_create_message_with_all_parameters(self):

        body = create_default_forum_message_body()
        response = self.api_utils.create_message_forum(body=body)
        assert_true(response.ok)
        assert_equals(response.content, 'message created')

        

    def test_create_message_with_none_parameters(self):

        body = create_default_forum_message_body()
        body[THEME] = None

        response = self.api_utils.create_message_forum(body=body)

        assert_equals(response.status_code, 400)
        response_body = assert_json_format(response)
        assert_equals(response_body[MESSAGES], 'Theme not valid')

    def test_create_message_without_some_parameter(self):

        for key in FORUM_KEYS:

            body = create_default_forum_message_body()
            body = delete_keys_from_dict(dict_del=body, key=key)
            response = self.api_utils.create_message_forum(body=body)
            assert_equals(response.status_code, 400)
            response_body = assert_json_format(response)
            assert_equals(response_body[MESSAGES], 'some parameter is not correct')

    def test_create_message_with_incorrect_json_format(self):

        body = 'Not JSON format'
        response = self.api_utils.create_message_forum(body=body)
        assert_equals(response.status_code, 400)
        response_body = assert_json_format(response)
        assert_equals(response_body[MESSAGES], 'some parameter is not correct')

    def test_create_message_with_incorrect_theme(self):

        theme_list = ['QA', 'security', '', 'AUTOMATION', '"testing"']
        for theme in theme_list:

            body = create_default_forum_message_body()
            body[THEME] = theme
            response = self.api_utils.create_message_forum(body=body)
            assert_equals(response.status_code, 400)
            response_body = assert_json_format(response)
            assert_equals(response_body[MESSAGES], 'Theme not valid')
