import requests
import base64

def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data = {'client_id':'www_front', 'client_secret':'eoqhfma', 'grant_type':'client_credentials'})
    j = r.json()
    token = j['access_token']
    return token

p = getToken()
print(p)


def makeHeadersAuth(token):
    token_encoded = base64.b64encode(token)
    # 모르겠다아아~~~~~
    # 힌트 좀 주세요~~~~~
    return auth
 