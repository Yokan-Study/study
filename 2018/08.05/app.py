from flask import Flask, render_template, request
from jya_gAPIclass import GapiClass
from datetime import date
import datetime
import pystache
import codecs

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mail')
def mail():
	return render_template('form.html')

@app.route('/tax')
def taxmail():
	return 'To be Continued'

@app.route('/result', methods=['POST'])
def result():
	if request.method == 'POST':
		# /mail에서 입력 받은 변수 가져오기
		k = request.form
		hanname = k['hanname']
		regist_date = date.today().strftime('%Y-''%m-''%d')
		service_name = k['service_name']
		domain = k['domain']
		expiration_date = k['expiration_date']
		convert_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date() # 문자인 expiration_date를 날짜 형식으로 변환 - 남은 일수(extendable_limit)를 자동 계산하기 위함
		extension_expense = format(int(k['extension_expense']), ',') # 숫자에 자동으로 콤마 넣어주기
		extension_period = k['extension_period']
		delta = convert_date - date.today()
		extendable_limit = delta.days
		total_count = 1
		mail = k['이메일']
		
		# 메일 콘텐츠에 변수 넣어주기
		f = codecs.open('/Users/조양아/Documents/GitHub/study/2018/08.05/templates/mail_contents.html', 'r', encoding='utf-8')
		text = f.read()
		data = {
			'hanname':hanname,
			'regist_date':regist_date,
			'service_name':service_name,
			'domain':domain,
			'expiration_date':expiration_date,
			'extension_expense':extension_expense,
			'extension_period':extension_period,
			'extendable_limit':extendable_limit,
			'total_count':total_count
		}
		mail_text = pystache.render(text, data)
		
		# 메일 발송하기
		subject = '[가비아] 서비스 이용 기간을 연장해 주세요'
		instance = GapiClass()
		instance.sendMail(subject, mail_text, mail, hanname)
		return render_template('result.html')


@app.route('/send')
def send():
	return '발송 완료'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2005')