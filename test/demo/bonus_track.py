__author__ = 'arobres'
import requests

### CUSTOM HEADERS ###

headers = {'my_header': 'important_header', 'content-type': 'application/json'}
response = requests.get('http://localhost:8081/v1.0', headers=headers)


### COOKIES ###

url = 'http://httpbin.org/cookies'
cookies = {'my_cookie_is': 'delicious'}

response = requests.get(url=url, cookies=cookies)
print response.status_code
response.content


### Multipart ###

url = 'http://httpbin.org/post'
files = {'file': open('__init__.py', 'rb')}

response = requests.post(url, files=files)
print response.status_code
response.content

### ANOTHER TOPICS

# YOU CAN VERIFY SSL CERTIFICATES
# YOU CAN CONTROL THE BODY CONTENT WORKFLOW (NOT DOWNLOAD THE DATA)
# YOU CAN USE PROXIES