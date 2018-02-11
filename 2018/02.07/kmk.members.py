import requests
    headers = {'Authorization': 'Basic {KEY}'} #{KEY}값이랑 아래 headers 값은 mock 처리해야

    def getMember(user_id): #함수로 회원 정보 가져오기 
    r = requests.get('https://gapi.gabia.com/members?user_id.{0}'.format(user_id), headers = headers) #포맷함수 지리구영 맞나?ㅎㅎ 
    return r.json('hanadmin') #json으로 리턴된 회원 정보 중에서 한글이름 가져오기 

    def getMembers(user_ids): #함수로 여러 회원 정보 가져오기
        user_ids = getMember(user_id)
        for x in user_ids:
        return x

        

