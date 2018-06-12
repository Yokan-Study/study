import os
import shutil
from datetime import datetime, date
from openpyxl import load_workbook


# 파일/디렉토리 생성에 필요한 내용 추출하기
year = datetime.today().year # 년도
month = datetime.today().month # 메일 발송월
if (month == 1):
	last_month = 12
elif month in [11, 12]:
	last_month = int_month-1
else:
	last_month = '0' + str(month-1)


# 발송 메일, 대상자 파일 등을 넣는 디렉토리 없으면 만들기
path = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)
if not os.path.isdir(path):
    os.mkdir(path)



# 인증후에서 다운로드한 실제 발송 대상 엑셀 파일 가져오기
file_name = 'taxbill_list_{0}-{1}.xls'.format(year, last_month)
file_asis = '/Users/조양아/Downloads/{0}'.format(file_name)
file_path_tobe = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)

if os.path.isfile(file_asis):
    shutil.copy(file_asis, file_path_tobe)
else: 
    print('인증후 세금계산서 발송 대상 다운로드부터 진행하세요')


# 엑셀 파일로부터 실제 발송 대상 추출하기
wb_file = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/taxbill_list_{1}-{0}.xlsx'.format(last_month, year)
ws_name = 'taxbill_list_{0}-{1}'.format(year, last_month)
if os.path.isfile(wb_file):
    wb = load_workbook(wb_file)
    ws = wb[ws_name]
    real_mail_list = []
    for r in ws.rows:
        mail = r[0].value
        if mail not in real_mail_list and mail != 'email' and mail != None: # 중복 값, 첫 행, 빈 값 제외하기
            real_mail_list.append(mail)
else: 
    print('다운받은 엑셀 파일 확장자명을 xlsx로 수정하세요')


# 메일 발송을 위해 텍스트 파일로 변환하기
real_mail = '\n'.join(real_mail_list)
make_real_mail_list = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/{0}월 실제 발송.txt'.format(last_month)
f = open(make_real_mail_list, 'w')
f.write(real_mail)
f.close()