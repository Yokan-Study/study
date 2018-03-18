import requests
headers = {'Authorization': 'Basic {key}'}

#1명의 회원 이름 정보 가져오는 함수 getMember() 만들기

def getMember(id):
    r = requests.get('https://gapi.gabia.com/members?user_id={0}'.format(id), headers=headers)
    # print(r)
    j = r.json()
    # print(j)
    k = j['client_info']
    hanname = k['hanadmin'] # j.hanadmin
    return hanname
    # hanname = j['client_info']['hanadmin'] # j.client_info.hanadmin

p = 'planning_d'
A = getMember(p)
# print(A)

# 리스트로 넘어온 user_id를 이용해 여러명의 이름 정보 가져와서 리스트로 만들어주는 getMembers() 만들기

def getMembers(user_ids):
    # return user_ids
    members = []
    for id in user_ids:
        C = getMember(id)
        if C != None:
            members.append(C)
    return members



# ['planning_d', 'test1gabia']

# return members
# k = [getMember('planning_d'), getMember('test1gabia')]
# L = getMembers(k)
# print(L)

q = ['planning_d', 'test1gabia', 'dalimix', 'jya9055', 'abc', 1]
B = getMembers(q)
print(B)