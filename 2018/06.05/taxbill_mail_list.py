import os
import shutil
from datetime import datetime


# 파일/디렉토리 생성에 필요한 내용 추출하기
year = datetime.today().year # 년도
month = datetime.today().month # 메일 발송월
last_month = month-1 #세금계산서 발행월


# 테스트 메일 발송 대상 만들기
test_mail_list = ['jya9055@hanmail.net', 'jya9055@gmail.com', 'jya@gabia.com', 'hsnja111@naver.com', 'hjk@gabia.com', 'lmk@gabia.com', 'junghwanlee@gabia.com', 'hdi@gabia.com', 'support3@gabia.com']
test_mail = '\n'.join(test_mail_list)


# 발송 메일, 대상자 파일 등을 넣는 디렉토리 없으면 만들기
path = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)
if not os.path.isdir(path):
    os.mkdir(path)


# 발송 대상 텍스트 파일로 저장
make_mail_list = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/테스트 발송.txt'.format(last_month)
f = open(make_mail_list, 'w')
f.write(test_mail)
f.close()


# 인증후에서 다운로드한 실제 발송 대상 엑셀 파일 가져오기
if (last_month <10):
	file_name = 'taxbill_list_{0}-0{1}.xls'.format(year, last_month)
else:
	file_name = 'taxbill_list_{0}-{1}.xls'.format(year, last_month)
# last_month를 저장하는 방식을 m이 아닌 mm으로 변경하고 싶은데 방식을 못찾겠음 ㅠ 일단 이렇게 진행

file_asis = '/Users/조양아/Downloads/{0}'.format(file_name)
file_path_tobe = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)

if os.path.isfile(file_asis):
    shutil.copy(file_asis, file_path_tobe)
else: 
    print('인증후 세금계산서 발송 대상 다운로드부터 진행하세요')

