import requests
headers = {'Authorization': 'Basic {key}'}

#1명의 회원 이름 정보 가져오는 함수 getMember() 만들기
def getMember(id):
    r = requests.get('https://gapi.gabia.com/members?user_id={0}'.format(id), headers=headers)
    j = r.json()
    print(j)
    hanname = j['hanadmin']
    return hanname

p = 'planning_d'
A = getMember(p)
print(A)


def getMembers(*user_ids):
    members = []
    for i in user_ids:
        members = members.append(i)
    return members

k = [getMember('planning_d'), getMember('test1gabia')]
L = getMembers(k)
print(L)