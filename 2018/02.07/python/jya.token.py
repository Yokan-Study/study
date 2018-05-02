import requests
import config

id = config.GAPI_CONFIG['client_id']
secret = config.GAPI_CONFIG['client_secret']
type = config.GAPI_CONFIG['grant_type']

data = {'client_id': id, 'client_secret': secret, 'grant_type': type}

r = requests.post('https://gapi.gabia.com/oauth/token', data=data)
# print(r)

j = r.json()
# print(j)

token = j['access_token']
# print(token)
