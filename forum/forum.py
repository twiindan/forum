__author__ = 'arobres'

from bottle import run, Bottle, request, response, auth_basic
from collections import defaultdict
import ujson
from sys import argv


app = Bottle()
user_list = []
USER_ATTRIBUTES = {'name', 'username', 'password', 'role', 'email'}
FORUM_ATTRIBUTES = {'theme', 'subject', 'message'}
ROLES = ['QA', 'DEVELOPER', 'MANAGER', 'DEVOPS']
THEMES = ['Security', 'Development', 'Automation', 'Testing']
user_messages_dict = defaultdict(list)
forum_messages_dict = defaultdict(list)


def check_username(username, password):
    for user in user_list:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False


@app.get("/v1.0/reset")
@app.get("/v1.0/reset/")
def reset_data():
    del user_list[:]
    user_messages_dict.clear()
    forum_messages_dict.clear()


@app.get("/v1.0/welcome")
@app.get("/v1.0/welcome/")
def im_alive():

    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"


@app.get("/v1.0")
@app.get("/v1.0/")
def im_alive():
    return {"product": 'forum', "version": '0.2.0'}


@app.post("/v1.0/users")
@app.post("/v1.0/users/")
def create_user():
    print (request.body)
    body = b"".join(request.body)
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

    if find_user(body['username']):
        response.status = 409
        return {"message": "User exist!"}

    else:
        user_list.append(body)

    return 'user created'

@app.get("/v1.0/users")
@app.get("/v1.0/users/")
def list_users():
    if len(user_list) == 0:
        return "No users created"
    else:
        return {'users': user_list}


@app.post("/v1.0/users/inbox/<username>")
@app.post("/v1.0/users/inbox/<username>/")
def create_user_message(username):

    body = b"".join(request.body)
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

    body = b"".join(request.body)
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

        return forum_messages_dict


    if len(theme_to_filter) == 1:

        message_list = forum_messages_dict[theme_to_filter[0]]
        return {theme_to_filter[0]: message_list}




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

run(app, host='0.0.0.0', port=argv[1], reloader=True)

