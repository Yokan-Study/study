import requests
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






