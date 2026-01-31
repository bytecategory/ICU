import requests
import threading
from time import sleep
import sys
url='https://jinshuju.com/graphql/f/GWSnA4'
json = [
    {
        'operationName': 'CreateFieldVerification',
        'variables': {
            'input': {
                'fieldApiCode': 'field_1',
                'formId': 'GWSnA4',
                'mobile': sys.argv[1],
             
            },
        },      
        'extensions': {
            'persistedQuery': {
                'sha256Hash': '77e2c905d36069c91d2ea55e915a1916204393b04a632087d59001301e6f7f5b'
                               
        },
    },
    }
]
requests.post(url=url, json=json)
