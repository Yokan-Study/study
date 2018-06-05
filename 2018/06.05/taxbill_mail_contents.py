import os
import pystache
import pystache.defaults
import calendar
from datetime import datetime

# 메일 본문 및 파일/디렉토리 생성에 필요한 내용 추출하기
year = datetime.today().year # 년도
month = datetime.today().month # 메일 발송월
last_month = month-1 #세금계산서 발행월
end_date = calendar.monthrange(year, last_month)[1] #일수

# 발송월마다 새로운 디렉토리 만들어주기 - 이미 만들어져 있는 경우에는 만들지 않음
path = '/Users/조양아/Desktop/마케팅실/세금계산서/2018/{0}월'.format(last_month)
if not os.path.isdir(path):
    os.mkdir(path)

# 변수 넣기 전 메일 본문
text = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
<title>[공지] {year}년 {last_month}월 세금계산서 발급 마감 안내</title>
</head>

<body style="margin:0; padding:0;">
<table width="720" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
<tr>
	<td style="background:#fff;">

		<!-- Top -->
		<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<tr>
			<td style="padding:30px 40px 25px; font-size:1px; line-height:1px; border-bottom:2px #e0e0e0 solid;">
				<a href="https://www.gabia.com/" target="_blank" title="새창"><img src="http://static.gabia.com/mail/common/logo_gabia_2016.png" alt="gabia" style="vertical-align:top; border:none;" /></a>
			</td>
		</tr>
		</table>
		<!-- //Top -->

		
		<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<tr>
			<td style="width:40px;"></td>
			<td style="padding:40px 0 50px;">

<!-- +++++++ Contents ++++++++ -->
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
	<td style="font:28px/40px Malgun Gothic; letter-spacing:-1px; color:#0879c9;">
		[공지] {year}년 {last_month}월 세금계산서 발급 마감 안내
	</td>
</tr>
<tr>
	<td style="padding:30px 0 25px; font:16px/26px Malgun Gothic; color:#767676;">
		안녕하세요. ㈜가비아입니다.
	</td>
</tr>
<tr>
	<td style="padding-bottom:10px; font:16px/26px Malgun Gothic; color:#767676;">
		{year}년 {last_month}월 세금계산서 신청은 <strong style="color:#0879c9">2018년 {month}월 8일</strong>에 마감합니다.<br>
		※ 2011년부터 법인의 전자세금계산서 발급 의무화에 따라 결제일부터 다음 달 8일까지만 신청을 받고 있으니 이 점 유의하시기 바랍니다. <br>
	</td>
</tr>
<tr>
	<td style="font:14px/22px Malgun Gothic; color:#666;">
		
		<!-- -->
		<table border="0" cellpadding="0" cellspacing="0"><tr><td style="display:block; height:30px;"></td></tr></table>
		<table border="0" cellspacing="0" cellpadding="0">
		<tr>
			<td style="vertical-align:top; font:18px/25px Malgun Gothic; letter-spacing:-1px; color:#0879c9;">
				<img src="https://static.gabia.com/mail/common/bul_2016_01.png" alt="" style="vertical-align:bottom; margin:0 0 5px 0;">&nbsp;&nbsp;{year}년 {last_month}월 세금계산서 발급 마감 안내
			</td>
		</tr>
		</table>
		<table border="0" cellpadding="0" cellspacing="0"><tr><td style="display:block; height:10px;"></td></tr></table>

		<table cellpadding="0" cellspacing="0" style="width:100%;"><tr><td style="background:#a5a5a5; font-size:1px; line-height:1px; height:2px;"></td></tr></table>
		<table cellpadding="0" cellspacing="0" style="width:100%; *width:auto; table-layout:fixed; border-bottom:1px #a5a5a5 solid; word-break:break-all;">
		<col width="110"><col>
		<tr>
			<th width="110" style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; background:#f3f3f3;">
				발급 대상
			</th>
			<td style="padding:8px 10px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-left:1px #e0e0e0 solid;">
				<strong style="color:#0879c9">{year}년 {last_month}월 1일 ~ {last_month}월 {end_date}일</strong> 결제 고객
			</td>
		</tr>
		<tr>
			<th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; border-top:1px #e0e0e0 solid; background:#f3f3f3;">
				마감 기한
			</th>
			<td style="padding:8px 10px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid;">
				<strong style="color:#0879c9">{year}년 {month}월 8일까지</strong>
			</td>
		</tr>
		<tr>
			<th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; border-top:1px #e0e0e0 solid; background:#f3f3f3;">
				신청 방법
			</th>
			<td style="padding:8px 10px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid;">
				가비아 홈페이지에 로그인하신 후 [My가비아 >  결제 관리 > 세금계산서] 메뉴에서 신청
			</td>
		</tr>
		<tr>
			<th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; border-top:1px #e0e0e0 solid; background:#f3f3f3;">
				문의 사항
			</th>
			<td style="padding:8px 10px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid;">
				도메인: <a href="mailto:dpay@gabia.com" style="color:#333; text-decoration:underline;">dpay@gabia.com</a><br>
				호스팅: <a href="mailto:pay@gabia.com" style="color:#333; text-decoration:underline;">pay@gabia.com</a><br>
			</td>
		</tr>
		<tr>
			<th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; border-top:1px #e0e0e0 solid; background:#f3f3f3;">
				기타
			</th>
			<td style="padding:13px 10px 8px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid;">
				<table border="0" cellpadding="0" cellspacing="0" width="100%">
				<tr>
					<td style="width:16px; padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#333;">
						<b>ㆍ</b>
					</td>
					<td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
						2005년 4월부터 개정된 부가가치세법에 따라 신용카드로 결제하시는 경우 신용카드 매출전표가 세금계산서를 대체합니다.
					</td>
				</tr>
				<tr>
					<td style="width:16px; padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#333;">
						<b>ㆍ</b>
					</td>
					<td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
						실시간 계좌이체나 무통장(가상계좌) 결제 시, 소득공제용이나 지출증빙용 현금영수증을 발급 받으신 경우, 별도로 세금계산서를 발행하지 않으며 현금영수증으로 세금계산서를 대체합니다.
					</td>
				</tr>
				<tr>
					<td style="width:16px; padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#333;">
						<b>ㆍ</b>
					</td>
					<td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
						신용카드 영수증 및 현금영수증은 [My가비아 > 결제 관리 > 결제/미결제 내역 > 결제완료]에서 출력하실 수 있습니다(단, 현금영수증은 발급을 신청하신 분만 가능합니다).
					</td>
				</tr>
				</table>
			</td>
		</tr>
		<tr>
			<th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; letter-spacing:-1px; color:#4b5964; text-align:center; border-top:1px #e0e0e0 solid; background:#f3f3f3;">
				부가가치세법<br>시행령 개정
			</th>
			<td style="padding:8px 10px; font:14px/20px Malgun Gothic; color:#4b5964; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid;">
				당사는 2012년 개정될 부가가치세법 시행령에 관한 국세청 권고 사항으로<br>
				<span style="color:#0879c9">발급 즉시 국세청 전송</span>을 시행하고 있으니, 이 점 유의하시기 바랍니다. 
			</td>
		</tr>
		</table>

	</td>
</tr>
</table>
<!-- +++++++ //Contents ++++++++ -->

			</td>
			<td style="width:40px;"></td>
		</table>


		<!-- Footer -->
		<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<tr>
			<td style="padding:40px; border-top:2px #e0e0e0 solid; font:14px/23px 'Malgun Gothic'; color:#767676;">
				※ 이 메일은 발신 전용입니다.
			</td>
		</tr>
		<tr>
			<td style="padding:24px; border-top:1px #e0e0e0 solid; border-bottom:1px #e0e0e0 solid; font:12px/12px 'Malgun Gothic'; color:#ccc; text-align:center;">
				<a href="http://company.gabia.com" style="color:#767676; text-decoration:none;" target="_blank" title="새창">회사소개</a> &nbsp;&nbsp; | &nbsp;&nbsp;
				<a href="https://www.gabia.com/agreements/index.php" style="color:#767676; text-decoration:none;" target="_blank" title="새창">약관</a> &nbsp;&nbsp; | &nbsp;&nbsp;
				<a href="https://www.gabia.com/privacy_policy" style="color:#767676; text-decoration:none;" target="_blank" title="새창">개인정보처리방침</a> &nbsp;&nbsp; | &nbsp;&nbsp;
				<a href="https://customer.gabia.com/" style="color:#767676; text-decoration:none;" target="_blank" title="새창">고객센터</a>
			</td>
		</tr>
		<tr>
			<td style="padding:30px 10px; font:12px/20px 'Malgun Gothic'; color:#767676; text-align:center;">
				(주)가비아 경기도 성남시 분당구 대왕판교로 660(삼평동) 유스페이스1 B동 4층<br>
				대표전화 1544-4370  메일/빌/이러닝 1661-4370<br><br>
				ⓒGabia Inc. All Rights Reserved.
			</td>
		</tr>
		</table>
		<!-- //Footer -->

	</td>
</tr>
</table>
</body>
</html>
'''
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
