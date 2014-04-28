__author__ = 'arobres'

from commons.rest_utils import RestUtils
from nose.tools import assert_equals, assert_true


class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.api_utils = RestUtils()

    def create_body(self, theme=None, subject=None, message=None):

        body = {}
        if theme is not None:
            body['theme'] = theme
        if subject is not None:
            body['subject'] = subject
        if message is not None:
            body['message'] = message
        return body

    def test_create_message_with_all_parameters(self):

        theme = 'testing'
        subject = 'QA movie'
        message = 'New movie about QA people!'

        response = self.api_utils.create_message(theme=theme, subject=subject, message=message)

        assert_true(response.ok)
        assert_equals(response.content, 'message created')

    def test_create_message_with_none_parameters(self):

        subject = 'QA movie'
        message = 'New movie about QA people!'

        response = self.api_utils.create_message(subject=subject, message=message)

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'Theme not valid')

    def test_create_message_without_some_parameter(self):

        theme = 'testing'
        subject = 'QA movie'
        message = 'New movie about QA people!'

        body = self.create_body(theme=theme, subject=subject)
        response = self.api_utils.create_message(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

        body = self.create_body(theme=theme, message=message)
        response = self.api_utils.create_message(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

        body = self.create_body(message=message, subject=subject)
        response = self.api_utils.create_message(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_create_message_with_incorrect_json_format(self):

        body = 'Not JSON format'
        response = self.api_utils.create_message(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'some parameter is not correct')

    def test_create_message_with_incorrect_theme(self):

        theme_list = ['QA', 'Security', '', 'AUTOMATION', '"testing"']
        subject = 'QA movie'
        message = 'New movie about QA people!'

        for theme in theme_list:

            body = self.create_body(theme=theme, subject=subject, message=message)
            response = self.api_utils.create_message(body=body)
            assert_equals(response.status_code, 400)
            response_body = response.json()
            assert_equals(response_body['message'], 'Theme not valid')
