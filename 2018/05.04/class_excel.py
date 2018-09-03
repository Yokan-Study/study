#1. 클래스 파일 class_kmk.py 모듈로 불러오기 (참고 사이트: https://wikidocs.net/29)

import class_kmk
a = class_kmk.gapiClass()
#print(a.getMember('kmkyeongkim11')) 

#2. user id에 따른 hanname 값들 출력하기  
han_1 = a.getMember('kmkyeongkim11')
han_2 = a.getMember('test1gabia')
print(han_1), print(han_2)

#3. 엑셀 파일 및 시트 활성화
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

data = [
    ['kmkyeongkim11', han_1],
    ['test1gabia', han_2],
]

 #3-1. add column headings
ws.append(["아이디", "회원 이름" ])
for row in data:
    ws.append(row)

wb.save("회원 리스트.xlsx")
