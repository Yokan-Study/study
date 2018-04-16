# gapi 클래스 만들기
import requests
import base64

class gapiClass:

# step 1. 인증 받기 위한 함수를 만든다. 
    def getToken(self, host='https://gapi.gabia.com'):
        self.host = host
        r = requests.post('{0}/oauth/token'.format(self.host), data={'client_id':'www_front', 'client_secret':'eoqhfma', 'grant_type':'client_credentials'})
        j = r.json()
        token = j['access_token']
        return 'www_front:{0}'.format(token)

# step 2. step 1에서 받은 토큰 값을 이용해 header에 넣을 인증키를 생성하는 함수를 만든다. 
    def makeHeadersAuth(self, token): 
        fucking_bytes = bytes(token, 'utf-8')
        token_encoded = base64.b64encode(fucking_bytes)
        Rjwu_bytes = token_encoded.decode('utf-8')
        return {'Authorization': 'Basic {0}'.format(Rjwu_bytes)}

# step 3. 토큰 받고 인증키 입력하는 것을 한방에 해결하는 함수를 만든다. 
    def hanbang(self):
        return self.makeHeadersAuth(self.getToken())

# step 4. 회원 정보에서 user id를 이용해 한글 이름 정보를 가져오는 함수를 만든다
    def getMember(self, id):
        r = requests.get('{0}/members?user_id={1}'.format(self.host, id), headers=self.hanbang())
        j = r.json()
        hanname = j['client_info']['hanadmin']
        return hanname 

k = gapiClass()
m = k.getToken()
#print(m)
y = k.makeHeadersAuth(m)
#print(y)
e = k.hanbang()
#print(e)
o = k.getMember('planning_d')
print(o)