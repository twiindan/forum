__author__ = 'arobres'

from rest_utils import RestUtils
from nose.tools import assert_equals, assert_true


def create_forum_body(theme=None, subject=None, message=None):

        body = {'theme': theme, 'subject': subject, 'message': message}
        return body


class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.api_utils = RestUtils()
        self.api_utils.reset_mock()

    def test_create_message_with_all_parameters(self):

        body = create_forum_body(theme='Automation', subject='First test', message='Automating my first test')
        print body
        response = self.api_utils.create_message_forum(body=body)
        assert_true(response.ok)
        assert_equals(response.content, 'message created')

    def test_create_message_with_incorrect_theme(self):

        theme_list = ['QA', 'security', '', 'AUTOMATION', '"testing"']

        for theme in theme_list:

            body = create_forum_body(theme=theme, subject='First test', message='Automating my first test')
            response = self.api_utils.create_message_forum(body=body)
            assert_equals(response.status_code, 400)

            try:
                response_body = response.json()
            except ValueError:
                assert False, "JSON Cannot be decode. Response format not correspond with JSON format"

            assert_equals(response_body['message'], 'Theme not valid')
