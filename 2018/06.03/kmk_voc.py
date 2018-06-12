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

id = j['rows']['row']
for i in id:
    k = i['@id']
    #print(k)

worker_list = []
row = j['rows']['row']
for w in row:
    o = w['cell'][7]
    #print(o)

    if o == '최선애':
        k = w['userdata']['#text']
        #print(k)
        worker_list.append(k)
print(worker_list)

        







