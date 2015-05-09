__author__ = 'arobres'


import requests
from json import JSONEncoder
import random

URL = 'http://localhost:5000/v1.0/6571e3422ad84f7d828ce2f30373b3d4/servers/qatest'
CONTENT_TYPE_HEADER = u'content-type'
DEFAULT_CONTENT_TYPE_HEADER = u'application/json'
AUTHENTICATION_HEADER = u'X-Auth-Token'


def send_data_to_fiware_facts(server_id=None, url=URL, token=None, cpu_value=random.randint(0, 100),
                              mem_value= random.randint(0, 100)):

    encoder = JSONEncoder()
    body = {
        "originator": 'orion',
        "subscriptionId": '11111111-1111-1f1a-1e1d-c1ca38a60ff4',
        "contextResponses": [
            {
            "contextElement": {
                "attributes": [
                {
                    "contextValue": cpu_value,
                    "type": "Probe",
                    "name": "cpuLoadPct"
                },
                {
                    "contextValue": mem_value,
                    "type": "Probe",
                    "name": "usedMemPct"
                },
                {
                    "contextValue": "0.1",
                    "type": "Probe",
                    "name": "Disk"
                },
                {
                    "contextValue": "0.151",
                    "type": "Probe",
                    "name": "Network"
                }
            ],
            "type": "server",
            "id": server_id,
            "isPattern": "false"
        },
         "statusCode": {
            "code": "200",
            "details": "message",
            "reasonPhrase": "Ok"
            }
        }
        ]
    }

    header = {CONTENT_TYPE_HEADER: DEFAULT_CONTENT_TYPE_HEADER, AUTHENTICATION_HEADER: token}

    requests.post(url=url, data=encoder.encode(body), headers=header)
    assert requests.ok


