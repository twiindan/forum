# LEARNING PYTHON REQUESTS LIBRARY
## FORUM API

### URL ROOT:

    REQUEST:

        GET HTTP://{SERVER:PORT}/v1.0

    RESPONSE:

        200 OK

        {"product": 'forum', "version": '0.2.0'}

### SEND MESSAGE TO FORUM

    REQUEST:

        POST HTTP://{SERVER:PORT}/v1.0/forum

        {'theme': <string>,
         'subject': <string>,
         'message': <string>}

    RESPONSE:

        200 OK
        'message created'

### GET MESSAGE FORUMS

    REQUEST:

        GET HTTP://{SERVER:PORT}/v1.0/forum&theme=?

    RESPONSE:

        200 OK

        {'messages': message_list}


### CREATE USER

    REQUEST

        POST HTTP://{SERVER:PORT}/v1.0/users

        {'name': <string>,
         'username': <string>,
         'password': <string>,
         'role': <string>,
         'email': <string>
        }

    RESPONSE:

        200 OK
        'user created'

        400 BAD REQUEST


### SEND PRIVATE MESSAGE TO USER

    REQUEST:

        POST HTTP://{SERVER:PORT}/v1.0/users/inbox/<username>

        body = {'message': <string>}

    RESPONSE:
        200 OK
        'message saved'

        400 BAD REQUEST
        404 NOT FOUND


### GET PRIVATE MESSAGES (BASIC AUTHENTICATION REQUIRED)

    REQUEST:

        GET HTTP://{SERVER:PORT}/v1.0/users/inbox/<username>


    RESPONSE:
        200 OK
        {"username": <username>, "messages": <LIST>}

        404 NOT FOUND


### DELETE PRIVATE MESSAGES (BASIC AUTHENTICATION REQUIRED)

    REQUEST:

        DELETE HTTP://{SERVER:PORT}/v1.0/users/inbox/<username>


    RESPONSE:
        200 OK
        404 NOT FOUND