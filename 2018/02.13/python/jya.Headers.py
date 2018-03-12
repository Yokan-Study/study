import requests, base64


def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': '', 'client_secret': '', 'grant_type': ''})
    j = r.json()
    token_1 = j['access_token']
    token_2 = 'www_front:{0}'.format(token_1) # 크롬에서 btoa 했을 때 'www_front:{토큰}'을 넣었으니까 이렇게 해야하지 않나..?
    return token_2

print (getToken())

def makeHeadersAuth(token):
    encoded_text = token.encode()
    k = base64.b64encode(encoded_text)
    l = k.decode()
    return 'Basic {0}'.format(l)


# 테스트
token = 'www_front:NDBhZmE5NTEzYzA3N2Q1ZWY2Yzc5ZGJjN2U2MmQ5'
k = makeHeadersAuth(token)
print(k)
# 프린트 성공!!!


# 한 번에 처리하는 함수 만들기
def encoded_token():
    return makeHeadersAuth(getToken())


# 함수 실행하기
p = encoded_token()
print(p)