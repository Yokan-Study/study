import requests
<<<<<<< HEAD
headers = {'Authorization' : 'Basic {KEY}'}

#1명의 회원 이름 정보 가져오는 함수 getMember() 만들기
#return 한글이름 hanadmin(string)

def getMember(user_id):
    r = requests.get('https://gapi.gabia.com/members?user_id={0}'.format(user_id), headers=headers)
    #print(r)
    j = r.json()
    name = j['client_info']['hanadmin']
    
    return name 

r = 'kmkyeongkim11'
# print getMember(r)

k = getMember(r)
print(k)

def getMembers(user_ids):
    members = []
    for id in user ids:
        c = getMember(id)
        members.append(c)

    return members

kmk1 = ['kmkyeongkim11', 'test1gabia', 'test0gabia']
kmk2 = getMembers(kmk1)

print(kmk2)


=======
headers = {'Authorization': 'Basic {KEY}'} #{KEY}값이랑 아래 headers 값은 mock 처리하랬는데 어떻게?

def getMember(user_id): #함수로 회원 정보 가져오기 
    r = requests.get('https://gapi.gabia.com/members?user_id={0}'.format(user_id), headers = headers) #포맷함수 지리구영 맞나?ㅎㅎ 
    return r.json()['client_info']['hanadmin'] #json으로 리턴된 회원 정보 중에서 한글이름 가져오기 

def getMembers(user_ids): #함수로 여러 회원 정보 가져오기
        result = []
        for user_id in user_ids:
            hanname= getMember(user_id)
            result.append(hanname)
        return result
>>>>>>> d40f2fd9efaf5a06e5c3ae377d5f01f396ff31ba




