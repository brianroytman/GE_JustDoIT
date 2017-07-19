import requests
import json
import os



#url = 'https://ff2359d6-05b4-4a0f-9001-2533c77cfe9d.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'

url = 'https://c0c50364-3a21-4b26-b08f-222f0c2d1dcd.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'


#print(url)
payload = "grant_type=client_credentials"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    #'authorization': 'Basic ' + os.getenv('UAA_Authorization', 'dHMtY2xpZW50MTpLZld1cHhTd001Q1hmaDg=')
    #'authorization': 'Basic ' + os.getenv('UAA_Authorization', 'amRpLWNsaWVudDpqZGktc2VjcmV0')
    'authorization': 'Basic amRpLWNsaWVudDpqZGktc2VjcmV0'

    }

response     = requests.request("POST", url, data=payload, headers=headers)
#print response.text


#access_token = json.loads(response.text)['access_token']

access_token = response.json()['access_token']


print(access_token)