__author__ = 'arobres'


from json import JSONEncoder
import requests
import logging

from configuration import FORUM_HOSTNAME, FORUM_PORT, HEADERS


POST = 'post'
GET = 'get'
DELETE = 'delete'

SERVER_ROOT = 'http://{}:{}/v1.0'.format(FORUM_HOSTNAME, FORUM_PORT)
CREATE_USER_PATTERN = '{url_root}/users/'
CREATE_MESSAGE_FORUM = '{url_root}/forum/'
USER_INBOX = '{url_root}/users/inbox/{username}'

class RestUtils(object):

    def __init__(self):
        """Initialization method
        """

        self.api_url = SERVER_ROOT
        print "Initialized API REST Utils"

        self.encoder = JSONEncoder()

    def _call_api(self, pattern, method, body=None, headers=HEADERS, payload=None, auth=None, **kwargs):

        """Launch HTTP request to Policy Manager API with given arguments
        :param pattern: string pattern of API url with keyword arguments (format string syntax)
        :param method: HTTP method to execute (string)
        :param body: JSON body content (dict)
        :param headers: HTTP header request (dict)
        :param payload: Query parameters for the URL
        :param **kwargs: URL parameters (without url_root) to fill the patters
        :returns: REST API response
        """

        kwargs['url_root'] = self.api_url

        url = pattern.format(**kwargs)

        try:
            r = requests.request(method=method, url=url, data=self.encoder.encode(body), headers=headers,
                                 params=payload, auth=auth)

        except Exception, e:
            print "Request {} to {} crashed: {}".format(method, url, str(e))
            return None

        return r

    def create_user(self, body=None, headers=HEADERS):

        return self._call_api(pattern=CREATE_USER_PATTERN, method=POST, headers=headers, body=body)

    def send_private_messages(self, message_body=None, username=None, headers=HEADERS):

        body = {'message': message_body}

        return self._call_api(pattern=USER_INBOX, method=POST, headers=headers, body=body, username=username)

    def get_private_messages(self, username=None, pwd=None, headers=HEADERS):

        authentication = (username, pwd)
        return self._call_api(pattern=USER_INBOX, method=GET, headers=headers, username=username,
                              auth=authentication)

    def delete_private_messages(self, username=None, pwd=None, headers=HEADERS):

        authentication = (username, pwd)
        return self._call_api(pattern=USER_INBOX, method=DELETE, headers=headers, username=username,
                              auth=authentication)

    def create_message_forum(self, body=None, headers=None):

        return self._call_api(pattern=CREATE_MESSAGE_FORUM, method=POST, headers=headers, body=body)

    def retrieve_forum_messages(self, theme=None, headers=HEADERS):

        if theme is not None:
            payload = {'theme': theme}

        return self._call_api(pattern=CREATE_MESSAGE_FORUM, method=GET, headers=headers, payload=payload)
