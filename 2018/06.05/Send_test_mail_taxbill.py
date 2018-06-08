from jya_gAPIclass import GapiClass
from datetime import datetime, date


# 메일 발송에 필요한 날짜 정보 
year = datetime.today().year # 년도
month = datetime.today().month # 메일 발송월
if (month == 1):
	last_month = 12
elif month in [11, 12]:
	last_month = int_month-1
else:
	last_month = '0' + str(month-1)

# 메일 제목
mail_title = '[공지] {0}년 {1}월 세금계산서 발급 마감 안내'.format(year, last_month)

# 메일 내용 불러오기
mail_contents = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/{0}m_taxbill.html'.format(last_month)
with open(mail_contents) as template:
	mail_text = template.read()


# 테스트 메일 발송 대상 만들기
# email = ['jya9055@hanmail.net', 'jya9055@gmail.com', 'jya@gabia.com', 'hsnja111@naver.com', 'hjk@gabia.com', 'lmk@gabia.com', 'junghwanlee@gabia.com', 'hdi@gabia.com', 'support3@gabia.com']
email = ['jya9055@hanmail.net', 'jya9055@gmail.com', 'jya@gabia.com', 'hsnja111@naver.com']




# 이메일 수만큼 이름 추가하기. 메일 리스트와 이름 리스트 개수가 동일해야 발송 가능함
name = []
k = 0
while k < len(email):
    name.append('가비아 회원')
    k += 1


# 메일 발송하기
instance = GapiClass()
instance.sendMail(mail_title , mail_text, email, name)