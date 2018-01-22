import requests
import ujson


url = 'https://api-testing-conference.herokuapp.com/v1.0'


#Make a GET request to the forum server

response = requests.get(url)


#get the response status code

status_code = response.status_code
print("RESPONSE STATUS CODE: {}".format(status_code))
status_ok = response.ok
print("RESPONSE IS OK?: {}".format(status_ok))


#Save the body obtained in the response in a <string>

text_body = response.text
print("RESPONSE BODY: {}".format(text_body))
print("RESPONSE BODY IS A: {}".format(type(text_body)))


#Save the body obtained in the response in a <dict>

json_body = response.json()
print("JSON RESPONSE BODY: {}".format(json_body))
print("JSON RESPONSE IS A: {}".format(type(json_body)))


#Get the response headers

response_header = response.headers
print("RESPONSE HEADER: {}".format(response_header))


#Send a POST with body

body = {'name': 'python', 'username': 'python', 'password': 'easy_pwd', 'role': 'QA', 'email': 'python@python.es'}
dict_body = ujson.dumps(body)

create_user_url = 'https://api-testing-conference.herokuapp.com/v1.0/users'
response = requests.post(url=create_user_url, data=dict_body)
response_body = response.text
print(response_body)


#Use Basic Authentication
inbox_url = 'https://api-testing-conference.herokuapp.com/v1.0/users/inbox/python'
response = requests.get(url=inbox_url, auth=('python', 'easy_pwd'))

response_body = response.json()
print(response_body)


#Request can manage cookies

url = 'https://api-testing-conference.herokuapp.com/v1.0/welcome'
response = requests.get(url)
print('BODY: {}'.format(response.text))
print(('COOKIES IN THE RESPONSE: {}').format(response.cookies))

cookie_to_send = {'visited': 'yes'}
response = requests.get(url, cookies=cookie_to_send)
print('BODY: {}'.format(response.text))





