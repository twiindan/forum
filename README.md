# LEARNING PYTHON REQUESTS LIBRARY

## HOW TO RUN THE FORUM APPLICATION

    python forum/forum.py

    The application is started in localhost using the 8081 port

## Prerequisites:

- Python 2.6 or newer

- pip installed (http://docs.python-guide.org/en/latest/starting/install/linux/)

- virtualenv installed (pip install virtalenv)

## Environment preparation:

- Create a virtual environment somewhere, e.g. in ~/venv (virtualenv ~/venv)

- Activate the virtual environment (source ~/venv/bin/activate)

- Install the requirements for the acceptance tests in the virtual environment (pip install -r requirements.txt --allow-all-external).

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
