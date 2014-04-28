__author__ = 'arobres'


from json import JSONEncoder
import requests

from configuration import FORUM_HOSTNAME, FORUM_PORT, HEADERS

SERVER_ROOT = 'http://{}:{}/v1.0'.format(FORUM_HOSTNAME, FORUM_PORT)
CREATE_USER_PATTERN = '{url_root}/users/'
CREATE_MESSAGE_FORUM = '{url_root}/forum/'

class RestUtils(object):

    def __init__(self):
        """Initialization method
        """

        self.api_url = SERVER_ROOT
        print "Initialized API REST Utils"

        self.encoder = JSONEncoder()

    def _call_api(self, pattern, method, body=None, headers=HEADERS, payload=None, **kwargs):

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

        print 'METHOD: {}\nURL: {} \nHEADERS: {} \nBODY: {}'.format(method, url, headers, self.encoder.encode(body))

        try:
            r = requests.request(method=method, url=url, data=self.encoder.encode(body), headers=headers,
                                 params=payload)

        except Exception, e:
            print "Request {} to {} crashed: {}".format(method, url, str(e))
            return None

        return r

    def create_user(self, name=None, username=None, pwd=None, role=None, email=None, body=None, headers=None):

        if not body:

            body = {'name': name,
                    'username': username,
                    'password': pwd,
                    'role': role,
                    'email': email
                    }

        return self._call_api(pattern=CREATE_USER_PATTERN, method='post', headers=headers, body=body)

    def create_message(self, theme=None, subject=None, message=None, body=None, headers=None):

        if not body:

            body = {'theme': theme,
                    'subject': subject,
                    'message': message}

        return self._call_api(pattern=CREATE_MESSAGE_FORUM, method='post', headers=headers, body=body)
