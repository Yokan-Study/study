# gapi 클래스 만들기
import requests
import base64
import config

class gapiClass:

# step 1. 인증 받기 위한 함수를 만든다. 
    def getToken(self, host='https://gapi.gabia.com'):
        r = requests.post('{0}/oauth/token'.format(host), data = config.api_config)
        j = r.json()
        token = j['access_token']
        return token

p = getToken()
#print(p)

# step 2. step 1에서 받은 토큰 값을 이용해 header에 넣을 인증키를 생성하는 함수를 만든다. 
    def makeHeadersAuth(self, token): 
        fucking_bytes = bytes(token, 'utf-8')
        token_encoded = base64.b64encode(fucking_bytes)
        Rjwu_bytes = token_encoded.decode('utf-8')
        return Rjwu_bytes

# step 3. 토큰 받고 인증키 입력하는 것을 한방에 해결하는 함수를 만든다. 
    def hanbang(self):
        return makeHeadersAuth(getToken())


# step 4. 
