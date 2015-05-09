__author__ = 'arobres'
import string
import random
from commons.constants import THEME, SUBJECT, MESSAGES, FORUM_THEMES
from commons.rest_utils import RestUtils
from nose.tools import assert_equals, assert_true



api_utils = RestUtils()


def id_generator(size=10, chars=string.ascii_letters + string.digits):

    """Method to create random ids
    :param size: define the string size
    :param chars: the characters to be use to create the string
    return ''.join(random.choice(chars) for x in range(size))
    """

    return ''.join(random.choice(chars) for x in range(size))


def assert_json_format(request):

    """"Method to assert the JSON format
    :param request: Object with the response
    :return response if is JSON compliance
    """

    try:
        response = request.json()
    except ValueError:
        assert False, "JSON Cannot be decode. Response format not correspond with JSON format"

    return response


def delete_keys_from_dict(dict_del, key):

    """
    Method to delete keys from python dict
    :param dict_del: Python dictionary with all keys
    :param key: key to be deleted in the Python dictionary
    :returns a new Python dictionary without the rules deleted
    """

    if key in dict_del.keys():

        del dict_del[key]
    for v in dict_del.values():
        if isinstance(v, dict):
            delete_keys_from_dict(v, key)

    return dict_del


def replace_values_from_dict(dict_replace, key, replace_to=None):

    """
    Method to replace values from python dict
    :param dict_replace: Python dictionary
    :param key: key to be replaced in the Python dictionary
    :param replace_to: The new value of the keys replaced
    :returns a new Python dictionary without the rules replaced
    """

    if key in dict_replace.keys():

        dict_replace[key] = replace_to
    for v in dict_replace.values():
        if isinstance(v, dict):
            replace_values_from_dict(v, key)

    return dict_replace


def create_body(theme=None, subject=None, message=None):

        body = {THEME: theme, SUBJECT: subject, MESSAGES: message}
        return body


def create_default_body():

    theme = 'testing'
    subject = 'QA movie'
    message = 'New movie about QA people!'

    return create_body(theme=theme, subject=subject, message=message)


def create_random_message():

    theme = random.choice(FORUM_THEMES)
    subject = id_generator(random.randint(1, 20))
    message = id_generator(random.randint(20, 200))

    return create_body(theme=theme, subject=subject, message=message)


def create_several_forum_messages(num_messages):
    for x in range(num_messages):
        body = create_random_message()
        print body
        response = api_utils.create_message_forum(body=body)
        assert_true(response.ok)
        assert_equals(response.content, 'message created')