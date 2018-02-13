import requests

# post /oauth/token 요청
# 파라미터 없이 함수 내부에서 data 변수 하드코딩

def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': 'www_front', 'client_secret': 'eoqhfma', 'grant_type': 'client_credentials'})
    j = r.json()
    token = j['access_token']
    return token

p = getToken()
print(p)