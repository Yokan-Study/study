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
    #print(o)

    if o == '최선애':
        k = w['userdata']['#text']  
        #print(k)
        q = w['@id']
        #print(q)
        board_seqno.append(k)
        seqno.append(q)

#print(board_seqno)
#print(seqno)

#게시판 글 번호 2개 리스트를 딕셔너리로 만들기 
num_dic = {
    board_seqno: seqno for board_seqno, seqno in zip(board_seqno, seqno)
}
print(num_dic)

import requests
r = requests.get('http://admin2.gabia.com/voc/improve/service_info.php?seqno=26599&board_seqno=1891160')
#print(r.status_code)
j = r.json()
print(j)