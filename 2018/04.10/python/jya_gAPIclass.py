import requests, base64
import config

id = config.GAPI_CONFIG['client_id']
secret = config.GAPI_CONFIG['client_secret']
type = config.GAPI_CONFIG['grant_type']

class GapiClass:
    def __init__(self, host='https://gapi.gabia.com'):
        self.__host = host
        self.__headers = self.__encoded_token()

    def __Requests_get(self, url):
        r = requests.get('{0}{1}'.format(self.__host, url), headers = self.__headers)
        j = r.json()
        return j

    def __Requests_post(self, url, data):
        r = requests.post('{0}{1}'.format(self.__host, url), data = data)
        j = r.json()
        return j

    def __getToken(self):
        j = self.__Requests_post('/oauth/token', {'client_id': id, 'client_secret': secret, 'grant_type': type})
        token_1 = j['access_token']
        token_2 = 'www_front:{0}'.format(token_1) 
        return token_2

    def __makeHeadersAuth(self, token):
        encoded_text = token.encode()
        k = base64.b64encode(encoded_text)
        l = k.decode()
        return {'Authorization': 'Basic {0}'.format(l)}

    def __encoded_token(self):
        return self.__makeHeadersAuth(self.__getToken())

    def getMember(self, id):
        j = self.__Requests_get('/members?user_id={0}'.format(id))
        hanname = j['client_info']['hanadmin']
        return hanname

# api1 = GapiClass()
# a = api1.getMember('planning_d')
# if __name__ == "__main__":
    # print(a)