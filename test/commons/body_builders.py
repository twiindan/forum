__author__ = 'arobres'

from commons.constants import THEME, SUBJECT, MESSAGES, FORUM_THEMES, NAME, USERNAME, PWD, EMAIL, ROLE, USER_ROLES
from nose.tools import assert_equals, assert_true
from commons.rest_utils import RestUtils
from commons.utils import id_generator

import random

api_utils = RestUtils()


def create_forum_body(theme=None, subject=None, message=None):

        body = {THEME: theme, SUBJECT: subject, MESSAGES: message}
        return body


def create_default_forum_message_body():

    theme = 'Testing'
    subject = 'QA movie'
    message = 'New movie about QA people!'

    return create_forum_body(theme=theme, subject=subject, message=message)


def create_random_forum_message():

    theme = random.choice(FORUM_THEMES)
    subject = id_generator(random.randint(1, 20))
    message = id_generator(random.randint(20, 200))

    return create_forum_body(theme=theme, subject=subject, message=message)


def create_several_forum_messages(num_messages):
    for x in range(num_messages):
        body = create_random_forum_message()
        print body
        response = api_utils.create_message_forum(body=body)
        assert_true(response.ok)
        assert_equals(response.content, 'message created')


def create_user_body(name=None, username=None, pwd=None, role=None, email=None):

    body = {}
    body[NAME] = name
    body[USERNAME] = username
    body[PWD] = pwd
    body[ROLE] = role
    body[EMAIL] = email

    return body


def create_default_user():

    name = 'toni'
    username = 'qaforever'
    pwd = 'easypwd'
    role = 'QA'
    email = 'arobres@tid.es'

    return create_user_body(name, username, pwd, role, email)


def create_random_user():
    name = id_generator(6)
    username = id_generator(6)
    pwd = id_generator(6)
    role = random.choice(USER_ROLES)
    email = '{}@{}'.format(id_generator(6), id_generator(6))

    return create_user_body(name, username, pwd, role, email)
