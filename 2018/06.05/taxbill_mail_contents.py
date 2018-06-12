import os
import pystache
import pystache.defaults
import calendar
from datetime import datetime, date


# 메일 본문 및 파일/디렉토리 생성에 필요한 내용 추출하기
# month는 'MM'월 형태로 표기되어야 함
year = datetime.today().year # 년도
month = date.today().strftime('%m') # 메일 발송월

if (int(month) == 1):
	last_month = 12
elif int(month) in [11, 12]:
	last_month = int_month-1
else:
	last_month = '0' + str(int(month)-1)

end_date = calendar.monthrange(year, int(last_month))[1] #일수


# 발송월마다 새로운 디렉토리 만들어주기 - 이미 만들어져 있는 경우에는 만들지 않음
path = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)
if not os.path.isdir(path):
    os.mkdir(path)


# 변수 넣기 전 메일 본문
# 본문을 붙여 넣지 않고 상위 폴더에 template.txt 생성하여 불러옴
template_path = '/Users/조양아/Desktop/마케팅실/세금계산서/template.txt'
with open(template_path) as template:
	text = template.read()


# 메일 본문 내 변수에 데이터 넣어주기
data = {
    'year': year,
    'month': month,
    'last_month': last_month,
    'end_date': end_date
}

pystache.defaults.DELIMITERS = ('{', '}') 
mail_text = pystache.render(text, data)


# html 파일 생성하여 데이터 넣어주기
make_HTML_file = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/{0}m_taxbill.html'.format(last_month)
f = open(make_HTML_file, 'w')
f.write(mail_text)
f.close()


# www 공지글 자동으로 넣어주기
notice_path = '/Users/조양아/Desktop/마케팅실/세금계산서/www_notice.txt'
with open(notice_path) as notice:
	notice_text = notice.read()

www_notice_text = pystache.render(notice_text, data)

make_txt_file = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월/{0}m_www_notice.txt'.format(last_month)
f = open(make_txt_file, 'w')
f.write(www_notice_text)
f.close()