import pystache, requests, smtplib
import pystache.defaults
from datetime import date
from jya_gAPIclass import GapiClass


template_path = '/Users/조양아/Desktop/마케팅실/결제 운영 표준화 상세2/안내메일발송/extension_notice_template.txt'
with open(template_path) as template:
	text = template.read()

date = date.today().strftime('%Y-''%m-''%d')

data = {
    'hanname':'조양아',
    'regist_date': date,
    'service_list':[
        {'service_name':'도메인',
        'domain':'gabia.com',
        'expiration_date':'2018-08-08',
        'extension_expense':'22,000원',
        'extension_period':'년',
        'extendable_limit':'50'
        },
         {'service_name':'웹호스팅',
        'domain':'gabia.com',
        'expiration_date':'2018-08-08',
        'extension_expense':'35,000원',
        'extension_period':'월',
        'extendable_limit':'50'
        }],
    'total_count':'2'
}
# data dictionary에 value에 해당하는 값을 DB에서 불러와야 함 
# 혹은 터미널/UI에서 수동으로 입력


pystache.defaults.DELIMITERS = ('{', '}') 
mail_text = pystache.render(text, data)
mail_title = '[가비아] 서비스 이용 기간을 연장해 주세요'
email = ['jya9055@gmail.com','hsnja111@naver.com','jya@gabia.com']


# 이메일 수만큼 이름 추가하기. 메일 리스트와 이름 리스트 개수가 동일해야 발송 가능함
name = []
for i in email:
    name.append('가비아 회원')

instance = GapiClass()
instance.sendMail(mail_title , mail_text, email, name)