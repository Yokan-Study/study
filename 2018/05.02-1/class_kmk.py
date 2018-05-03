import requests, configparser, base64

config = configparser.ConfigParser()
config.read('config_kmk.ini')
id = config['login_info']['client_id']
pw = config['login_info']['client_secret']
type = config['login_info']['grant_type']

class gapiClass:
    def __init__(self, host='https://gapi.gabia.com'):
        self.host = host

    def getToken(self):      
        r = requests.post('{0}/oauth/token'.format(self.host), data = {'client_id': id, 'client_secret': pw, 'grant_type': type})
        j = r.json()
        k = j['access_token']
        token = 'www_front:{0}'.format(k)
        return token

# a = gapiClass()
# k = a.getToken()
# print(k)

    def encodeToken(self, token):
        encoded_token= base64.b64encode(bytes(token, 'utf-8'))
        k = encoded_token.decode('utf-8')
        return {'Authorization': 'Basic {0}'.format(k)} #한번 더 확인

    def makeHeaderAuth(self):
        return self.encodeToken(self.getToken())
# a = gapiClass()
# k = a.makeHeaderAuth()
# print(k)

    def getMember(self, user_id):
        g = requests.get('{0}/members?user_id={1}'.format(self.host, user_id), headers = self.makeHeaderAuth())
        m = g.json()
        name = m['client_info']['hanadmin']
        return name

a = gapiClass()
b = a.getMember('test1gabia')
print(b)


# p = gapiClass()
# q = p.encodeToken(p.getToken())
# print(q)
