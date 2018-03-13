import requests

data = {'client_id': '', 'client_secret': '', 'grant_type': ''}

r = requests.post('https://gapi.gabia.com/oauth/token', data=data)
# print(r)

j = r.json()
token = j['access_token']

# print(token)