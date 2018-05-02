import requests, configparser

# post /oauth/token 요청
# 파라미터 없이 함수 내부에서 data 변수 하드코딩

config = configparser.ConfigParser()
config.read('../../config.ini')

id = config['gAPI']['client_id']
secret = config['gAPI']['client_secret']
type = config['gAPI']['grant_type']

def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data={'client_id': id, 'client_secret': secret, 'grant_type': type})
    j = r.json()
    token = j['access_token']
    return token

# p = getToken()
# print(p)


