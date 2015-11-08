__author__ = 'arobres'


from json import JSONEncoder
import requests

from configuration import FORUM_HOSTNAME, FORUM_PORT, HEADERS


POST = 'post'
GET = 'get'
DELETE = 'delete'

SERVER_ROOT = 'http://{}:{}/v1.0'.format(FORUM_HOSTNAME, FORUM_PORT)
CREATE_USER_PATTERN = '{url_root}/users/'
CREATE_MESSAGE_FORUM = '{url_root}/forum/'
USER_INBOX = '{url_root}/users/inbox/{username}'
RESET_PATTERN = '{url_root}/reset'


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

    def create_message_forum(self, body=None, headers=None):

        return self._call_api(pattern=CREATE_MESSAGE_FORUM, method=POST, headers=headers, body=body)

    def create_user(self, body=None, headers=HEADERS):

        #DEFINE THE CALL API WITH THE REQUIRED PARAMETERS (PATTERN, METHOD, HEADERS, BODY)
        pass

    def reset_mock(self):

        return self._call_api(pattern=RESET_PATTERN, method=GET, headers=HEADERS)
