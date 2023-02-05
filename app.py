__author__ = 'arobres'

from flask import Flask, request, make_response, Response, jsonify
from collections import defaultdict
from flask_httpauth import HTTPBasicAuth

import ujson


app = Flask(__name__)
auth = HTTPBasicAuth()
user_list = []
USER_ATTRIBUTES = {'name', 'username', 'password', 'role', 'email'}
FORUM_ATTRIBUTES = {'theme', 'subject', 'message'}
ROLES = ['QA', 'DEVELOPER', 'MANAGER', 'BA']

THEMES = ['Security', 'Development', 'Automation', 'Testing']
user_messages_dict = defaultdict(list)
forum_messages_dict = defaultdict(list)


@auth.verify_password
def check_username(username, password):
    for user in user_list:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False


@app.route('/v1.0/reset', methods=['GET'])
def reset_data():
    del user_list[:]
    user_messages_dict.clear()
    forum_messages_dict.clear()


@app.route("/v1.0/welcome", methods=['GET'])
def welcome():

    if request.cookies.get("visited"):
        return "Welcome back! Nice to see you again"
    else:
        resp = make_response("Hello there! Nice to meet you")
        resp.set_cookie("visited", "yes")
        return resp


@app.route("/v1.0", methods=['GET'])
def im_alive():
    return {"product": 'forum', "version": '0.3.0'}


@app.route("/v1.0/users", methods=['POST'])
def create_user():
    try:
        body = request.get_json()
    except:
        return Response(response='{"message": "The JSON format is not correct"}', status=400, mimetype='application/json')

    check = check_user_body(body)

    if not check:
        return Response(response='{"message": "some parameter is not correct"}', status=400, mimetype='application/json')

    if body['role'] not in ROLES:
        return Response(response='{"message": "Role not valid"}', status=400, mimetype='application/json')

    if find_user(body['username']):
        return Response(response='{"message": "User exist!"}', status=409, mimetype='application/json')

    else:
        user_list.append(body)

    return 'user created'


@app.route("/v1.0/users", methods=['GET'])
def list_users():
    if len(user_list) == 0:
        return "No users created"
    else:
        return {'users': user_list}


@app.route("/v1.0/users/inbox/<username>", methods=['POST'])
def create_user_message(username):

    try:
        body = request.get_json()
    except:
        return Response('{"message": "The JSON format is not correct"}', status=400)

    user_exist = find_user(username=username)

    if not user_exist:
        return Response('{"message": "The user not exists"}', status=404)

    receiver_list = user_messages_dict[username]
    receiver_list.append(body)
    return Response('message saved', status=200)


@auth.login_required
@app.route("/v1.0/users/inbox/<username>", methods=['GET'])
def get_user_messages(username):

    receiver_list = user_messages_dict[username]
    return {"username": username, "messages": receiver_list}

@app.route("/v1.0/users/inbox/<username>", methods=['DELETE'])
@auth.login_required
def delete_messages_from_user(username):

    del(user_messages_dict[username])
    return 'messages deleted'


@app.route("/v1.0/forum", methods=['POST'])
def publish_to_forum():
    try:
        body = request.get_json()
    except:
        return Response('{"message": "The JSON format is not correct"}', status=400)

    check = check_forum_body(body)
    if not check:
        return Response('{"message": "some parameter is not correct"}', status=400)

    if body['theme'] not in THEMES:
        return Response('{"message": "Theme not valid"}', status=400)
    else:
        forum_list = forum_messages_dict[body['theme']]
        forum_list.append(body)

    return Response('message created', status=200)


@app.route("/v1.0/forum", methods=['GET'])
def get_messages():

    query_parameters = request.args
    print(query_parameters)
    theme_to_filter = query_parameters.get('theme')
    print(theme_to_filter)
    if theme_to_filter is None:

        return forum_messages_dict

    else:

        message_list = forum_messages_dict[theme_to_filter]
        print(message_list)
        return {theme_to_filter: message_list}


def find_user(username):

    for user in user_list:
        if user['username'] == username:
            return True

    return False


def check_user_body(body):
    count = 0
    for attribute in USER_ATTRIBUTES:

        if attribute not in body:
            return False
        else:
            count += 1
    if count != 5:
        return False
    else:
        return True


def check_forum_body(body):
    count = 0
    for attribute in FORUM_ATTRIBUTES:

        if attribute not in body:
            return False
        else:
            count +=1
    if count != 3:
        return False
    else:
        return True
