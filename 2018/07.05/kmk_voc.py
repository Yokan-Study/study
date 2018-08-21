#-*- coding: utf-8 -*-
import urllib.request
import xmltodict
import json
with urllib.request.urlopen("http://admin2.gabia.com/voc/improve/getData/service_imp_list_data.php") as url:
 
    r = url.read()
 
h = r.decode("euc-kr")
g = xmltodict.parse(h)
#print(h)
#print(g)
j = json.loads(json.dumps(g))
#print(j)
 
#특정 작업자에 해당하는 board_seqno와 seqno 추출하기
board_seqno = []
seqno = []
row = j['rows']['row']

for w in row:
    o = w['cell'][7]
    p = w['@id']
<<<<<<< HEAD
    if o == '최선애':8
=======
    if o == '최선애':
>>>>>>> b08bddcc9900f64758e44d2eac53e60888e219a2
        k = w['userdata']['#text']
        q = w['@id']
#print(k)
#print(q)
seqno.append(k)
board_seqno.append(q)
 
#print(board_seqno)
#print(seqno)
 
#게시판 글 번호 2개 리스트를 딕셔너리로 만들기 
num_dic = {
board_seqno: seqno for board_seqno, seqno in zip(board_seqno, seqno)
}
print(num_dic)
 
 
import requests
r = requests.post('http://admin2.gabia.com/voc/unite/getData/unite_info_data.php', data={'seq': k})
#print(r.status_code)
#print(text)
g = xmltodict.parse(r.text)
j = json.loads(json.dumps(g))
#print(j)
 
voc_title = j['data']['view_info']['view'][14]['#text']
voc_body = j['data']['view_info']['view'][15]['#text']
 
print("제목: " + voc_title)
#print("내용: " + voc_body)
 
import re
def remove_tag(content):
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext
 
print(remove_tag(voc_body))