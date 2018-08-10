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
    if o == '이정훈':
        t = w['userdata']['#text']
        q = w['@id']
#print(t)
#print(q)
seqno.append(t)
board_seqno.append(q) 

#print(board_seqno)
#print(seqno)
 
#print(board_seqno)
#print(seqno)
 
#게시판 글 번호 2개 리스트를 딕셔너리로 만들기 
num_dic = {
board_seqno: seqno for board_seqno, seqno in zip(board_seqno, seqno)
}
print(num_dic)
 
import requests
r = requests.post('http://admin2.gabia.com/voc/unite/getData/unite_info_data.php', data={'seq': t})
#print(r.status_code)
#print(text)
g = xmltodict.parse(r.text)
j = json.loads(json.dumps(g))
#print(j)
 
voc_title = j['data']['view_info']['view'][14]['#text']
voc_body = j['data']['view_info']['view'][15]['#text']
 
voc = voc_title + voc_body
#print(voc)
 
import re
def remove_tag(content):
    cleanr =re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext
 
print(remove_tag(voc))


#메일 발송 
import smtplib
from email.mime.text import MIMEText
from email import utils

me = 'kmkgabia@gmail.com'
you = 'kathleenminkyeongkim@gmail.com'
contents = voc

msg = MIMEText(contents, _charset='euc-kr')
msg['Subject'] = voc_title
msg['From'] = me
msg['To'] = you

smtp = smtplib.SMTP('smtp.gmail.com', 534)
smtp.ehlo()
smtp.starttls()
smtp.login('kmkgabia@gmail.com', 'Rhfenrl11!')
smtp.sendmail('kmkgabia@gmail.com', 'kathleenminkyeongkim@gmail.com', msg.as_string())

smtp.quit()