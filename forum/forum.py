__author__ = 'arobres'

from bottle import route, run, template, Bottle, request, response, auth_basic
from collections import defaultdict
import ujson

app = Bottle()
user_list = []
USER_ATTRIBUTES = {'name', 'username', 'password', 'role', 'email'}
FORUM_ATTRIBUTES = {'theme', 'subject', 'message'}
ROLES = ['QA', 'DEVELOPER', 'MANAGER']
THEMES = ['security', 'development', 'automation', 'testing']
user_messages_dict = defaultdict(list)
forum_messages_dict = defaultdict(list)


def check_username(username, password):
    for user in user_list:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False

@app.get("/v1.0")
@app.get("/v1.0/")
def im_alive():
    return {"product": 'forum', "version": '0.2.0'}


@app.post("/v1.0/users")
@app.post("/v1.0/users/")
def create_user():

    body = "".join(request.body)
    try:
        body = ujson.loads(body)
    except:
        response.status = 400
        return {"message": "The JSON format is not correct"}

    check = check_user_body(body)

    if not check:
        response.status = 400
        return {"message": "some parameter is not correct"}

    if body['role'] not in ROLES:
        response.status = 400
        return {"message": "Role not valid"}
    else:
        user_list.append(body)

    return 'user created'


@app.post("/v1.0/users/inbox/<username>")
@app.post("/v1.0/users/inbox/<username>/")
def create_user_message(username):

    body = "".join(request.body)
    try:
        body = ujson.loads(body)
    except:
        response.status = 400
        return {"message": "The JSON format is not correct"}

    user_exist = find_user(username=username)

    if not user_exist:
        response.status = 404
        return {"message": "The user not exists"}

    receiver_list = user_messages_dict[username]
    receiver_list.append(body)
    response.status = 200
    return 'message saved'


@app.get("/v1.0/users/inbox/<username>")
@app.get("/v1.0/users/inbox/<username>/")
@auth_basic(check_username)
def get_user_messages(username):

    receiver_list = user_messages_dict[username]
    return {"username": username, "messages": receiver_list}

@app.delete("/v1.0/users/inbox/<username>")
@app.delete("/v1.0/users/inbox/<username>/")
@auth_basic(check_username)
def delete_messages_from_user(username):

    del(user_messages_dict[username])
    return 'messages deleted'


@app.post("/v1.0/forum")
@app.post("/v1.0/forum/")
def publish_to_forum():

    body = "".join(request.body)
    try:
        body = ujson.loads(body)
    except:
        response.status = 400
        return {"message": "The JSON format is not correct"}

    check = check_forum_body(body)
    if not check:
        response.status = 400
        return {"message": "some parameter is not correct"}

    if body['theme'] not in THEMES:
        response.status = 400
        return {"message": "Theme not valid"}
    else:
        forum_list = forum_messages_dict[body['theme']]
        forum_list.append(body)
        response.status = 200

    return 'message created'

@app.get("/v1.0/forum")
@app.get("/v1.0/forum/")
def get_messages():

    theme_to_filter = request.query.getall('theme')

    if len(theme_to_filter) == 0:
        messages = []
        print type(forum_messages_dict)
        print len(forum_messages_dict)
        return {'messages': forum_messages_dict}

    if len(theme_to_filter) == 1:

        message_list = forum_messages_dict[theme_to_filter[0]]
        return {'messages': message_list}


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

run(app, host='0.0.0.0', port=8081, reloader=True)
