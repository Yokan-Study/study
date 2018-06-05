import pystache, requests, smtplib
import pystache.defaults
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
headers = {'Authorization': 'Basic {key}'}


# def get_template(number):
#     r = requests.get('https://gapi.gabia.com/mail/templates?seqno={0}'.format(number), headers=headers)
#     j = r.json()
#     contents = j['contents']
#     k = str(contents)
#     return k
# text = get_template(62)
# API를 통해 템플릿 불러오기를 하려고 했는데, 템플릿 일부 코드 수정이 필요해서 아래와 같이 텍스트로 직접 입력함

text = '''
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
    <title></title>
</head>
<body style="margin:0; padding:0;">
    <table width="720" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto;">
        <tr>
            <td style="background:#fff;">
                <!-- Top -->
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td style="padding:30px 40px 25px; font-size:1px; line-height:1px; border-bottom:2px #e0e0e0 solid;"> <a href="https://www.gabia.com/?utm_source=ems&utm_medium=email&utm_term=gabia&utm_campaign=notice&utm_content=CI" target="_blank" title="새창"><img src="http://static.gabia.com/mail/common/logo_gabia_2016.png" alt="gabia" style="vertical-align:top; border:none;" /></a>                            </td>
                    </tr>
                </table>
                <!-- //Top -->
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td style="width:40px;"></td>
                        <td style="padding:40px 0 50px;">
                            <!-- +++++++++++++++++++++++++++++++ 컨텐츠 내용 +++++++++++++++++++++++++++++++ -->
                            <!-- +++++++ Contents ++++++++ -->
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td style="font:30px/40px Malgun Gothic; letter-spacing:-1px; color:#0879c9;"> [가비아] 서비스 이용 기간을 연장해 주세요 </td>
                                </tr>
                                <!-- [ver3] 인사말 모듈 시작! -->
                                <!-- 모듈 설명 : 안녕하세요. {hanname}님 -->
                                <tr>
                                    <td style="padding:30px 0 25px; font:16px/26px Malgun Gothic; color:#767676;"> 안녕하세요. {hanname} 님 </td>
                                </tr>
                                <!-- [ver3] 인사말 모듈 끝 -->
                                <tr>
                                    <td style="padding-bottom:10px; font:16px/26px Malgun Gothic; color:#767676;"> 이용 중인 서비스의 만기일이 곧 다가옵니다.<br /> 만기 후에는 서비스 이용이 제한될 수 있으니, 아래 내용을 확인하시고<br /> 연장 가능 기한 내에 서비스를 연장해 주세요.<br /><br /> </td>
                                </tr>
                                <tr>
                                    <td style="font:14px/22px Malgun Gothic; color:#666;">
                                        <!-- -->
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="display:block; height:30px;"></td>
                                            </tr>
                                        </table>
                                        <table border="0" cellspacing="0" cellpadding="0" style="width:100%; *width:auto; table-layout:fixed;">
                                            <tr>
                                                <td style="width:20px; font-size:1px; line-height:16px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tbody>
                                                            <tr>
                                                                <td style="display:block; height:8px;"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table> <img src="http://static.gabia.com/mail/common/bul_2016_01.png" alt="" style="vertical-align:top;"> </td>
                                                <td style="vertical-align:top; font:18px/25px Malgun Gothic; letter-spacing:-1px; color:#0879c9;">
                                                대상 서비스 </td>
                                                <td style="font:14px/20px Malgun Gothic; color:#4b5964; text-align:right;"> * 작성일: {regist_date} </td>
                                            </tr>
                                        </table>
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="display:block; height:10px;"></td>
                                            </tr>
                                        </table>
                                        <table cellpadding="0" cellspacing="0" style="width:100%;">
                                            <tr>
                                                <td style="background:#a5a5a5; font-size:1px; line-height:1px; height:2px;"></td>
                                            </tr>
                                        </table>
                                        <table cellpadding="0" cellspacing="0" style="width:100%; *width:auto; table-layout:fixed; border-bottom:1px #e0e0e0 solid; word-break:break-all;">
                                            <tr>
                                                <th style="padding:8px 0; font:bold 14px/20px Malgun Gothic; color:#4b5964; letter-spacing:-1px; color:#4b5964; text-align:center; background:#f3f3f3; "> 서비스 </th>
                                                <th width="110" style="padding:8px 0; font:bold 14px/20px Malgun Gothic; color:#4b5964; letter-spacing:-1px; color:#4b5964; text-align:center; background:#f3f3f3; border-left:1px #e0e0e0 solid;">
                                                만기일 </th>
                                                <th width="110" style="padding:8px 0; font:bold 14px/20px Malgun Gothic; color:#4b5964; letter-spacing:-1px; color:#4b5964; text-align:center; background:#f3f3f3; border-left:1px #e0e0e0 solid;">
                                                기준 금액 </th>
                                                <th width="110" style="padding:8px 0; font:bold 14px/20px Malgun Gothic; color:#4b5964; letter-spacing:-1px; color:#4b5964; text-align:center; background:#f3f3f3; border-left:1px #e0e0e0 solid;">
                                                연장 가능 기한 </th>
                                            </tr>
                                            <tr>
                                                <td style="padding:8px 5px; font:14px/20px Malgun Gothic; color:#4b5964; border-top:1px #e0e0e0 solid; text-align:left;"> {service_name}<br /> <span style="font-size:13px;">{domain}</span> </td>
                                                <td style="padding:8px 5px; font:14px/20px Malgun Gothic; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid; text-align:center;">
                                                {expiration_date} </td>
                                                <td style="padding:8px 5px; font:14px/20px Malgun Gothic; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid; text-align:right;"> {extension_expense}/{extension_period} </td>
                                                <td style="padding:8px 5px; font:14px/20px Malgun Gothic; color:#4b5964; border-top:1px #e0e0e0 solid; border-left:1px #e0e0e0 solid; text-align:center;"> <b style="color:#f00;">{extendable_limit}</b>일 남음 </td>
                                            </tr> </table>
                                        <table cellpadding="0" cellspacing="0" style="width:100%; *width:auto; table-layout:fixed; border-bottom:1px #a5a5a5 solid; word-break:break-all;">
                                            <tr>
                                                <td style="text-align:right; padding:10px; font:bold 16px/1.2em Malgun Gothic; color:#000; background:#f8f8f8"> 총 {total_count} 건 </td>
                                            </tr>
                                        </table>
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="display:block; height:25px;"></td>
                                            </tr>
                                        </table>
                                        <div style="text-align:center;">
                                            <!-- <a href="https://www.gabia.com/mygabia/extend" style="display:inline-block;vertical-align:top;padding:8px 30px 10px;color:#666;font:12px/14px Malgun Gothic;text-decoration:none;border:1px solid #cdcdcd;background:#f6f6f6" target="blank" title="새창">서비스 연장하기 <img src="https://static.gabia.com/mail/common/icon_btn_arrow.png" alt="" style="padding-left:15px;vertical-align:middle; border:none;"></a> --><a href="https://www.gabia.com/mygabia/extend?utm_source=gabia&utm_medium=email&utm_term=%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%B0%EC%9E%A5%ED%95%98%EA%B8%B0&utm_campaign=%EA%B3%B5%ED%86%B5" target="_blank" title="새창"
                                                rel="noopener"><img src="http://static.gabia.com/mail/2018/ems/btn_ems_04.png" alt="서비스 연장하기"></a> </div>
                                        <!-- -->
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="display:block; height:30px;"></td>
                                            </tr>
                                        </table>
                                        <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td style="width:20px; font-size:1px; line-height:16px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="display:block; height:8px;"></td>
                                                        </tr>
                                                    </table> <img src="http://static.gabia.com/mail/common/bul_2016_01.png" alt="" style="vertical-align:top;"> </td>
                                                <td style="vertical-align:top; font:18px/25px Malgun Gothic; letter-spacing:-1px; color:#0879c9;">
                                                유의사항 </td>
                                            </tr>
                                        </table>
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tr>
                                                <td style="display:block; height:10px;"></td>
                                            </tr>
                                        </table>
                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tr>
                                                <td style="width:16px; font-size:1px; line-height:7px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="display:block; height:8px;"></td>
                                                        </tr>
                                                    </table> <img src="http://static.gabia.com/mail/common/renew_edm_bul01.gif" alt="" style="vertical-align:top; margin-left:2px;"> </td>
                                                <td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
                                                본 메일은 {regist_date}에 작성되었으므로, 이미 서비스를 연장하신 분은 다시 연장하지 않아도 됩니다. </td>
                                            </tr>
                                            <tr>
                                                <td style="width:16px; font-size:1px; line-height:7px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="display:block; height:8px;"></td>
                                                        </tr>
                                                    </table> <img src="http://static.gabia.com/mail/common/renew_edm_bul01.gif" alt="" style="vertical-align:top; margin-left:2px;"> </td>
                                                <td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
                                                만기일이 지나면 도메인 사용이 제한되며, 사용이 제한된 이후에 도메인을 연장하면 정상적으로 서비스를 이용하기까지 1 ~ 3일정도 소요될 수 있습니다. </td>
                                            </tr>
                                            <tr>
                                                <td style="width:16px; font-size:1px; line-height:7px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="display:block; height:8px;"></td>
                                                        </tr>
                                                    </table> <img src="http://static.gabia.com/mail/common/renew_edm_bul01.gif" alt="" style="vertical-align:top; margin-left:2px;"> </td>
                                                <td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
                                                도메인 삭제일이 임박하여 연장된 건에 대해서는 네트워크, 시행사 통신 등의 문제로 연장이 안 될 수 있습니다. 이에 대해서는 가비아에서 책임을 지지 않으니, 미리 연장해 주시기 바랍니다. </td>
                                            </tr>
                                            <tr>
                                                <td style="width:16px; font-size:1px; line-height:7px; vertical-align:top;">
                                                    <table border="0" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td style="display:block; height:8px;"></td>
                                                        </tr>
                                                    </table> <img src="http://static.gabia.com/mail/common/renew_edm_bul01.gif" alt="" style="vertical-align:top; margin-left:2px;"> </td>
                                                <td style="padding-bottom:5px; vertical-align:top; font:14px/20px Malgun Gothic; color:#666;">
                                                도메인 종류에 따라 <strong>만기일 전에 삭제될 수도 있습니다</strong>. 연장 가능 기한 내에 연장해야 도메인이 삭제되지 않습니다. </td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td style="width:40px;"></td>
                            </table>
                            <!-- Footer -->
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td style="padding:40px; border-top:2px #e0e0e0 solid; font:14px/23px Malgun Gothic; color:#767676;"> ※ 이 메일은 발신 전용입니다. </td>
                                </tr>
                                <tr>
                                    <td style="padding:24px; border-top:1px #e0e0e0 solid; border-bottom:1px #e0e0e0 solid; font:12px/12px Malgun Gothic; color:#ccc; text-align:center;"> <a href="https://company.gabia.com/?utm_source=ems&utm_medium=email&utm_term=footer&utm_campaign=notice&utm_content=%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C" style="color:#767676; text-decoration:none;" target="_blank"
                                            title="새창">회사소개</a> &nbsp; | &nbsp; <a href="https://www.gabia.com/agreements/index.php?utm_source=ems&utm_medium=email&utm_term=footer&utm_campaign=notice&utm_content=%EC%95%BD%EA%B4%80" style="color:#767676; text-decoration:none;"
                                            target="_blank" title="새창">약관</a> &nbsp; | &nbsp; <a href="https://www.gabia.com/privacy_policy?utm_source=ems&utm_medium=email&utm_term=footer&utm_campaign=notice&utm_content=%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EC%B7%A8%EA%B8%89%EB%B0%A9%EC%B9%A8"
                                            style="color:#767676; text-decoration:none;" target="_blank" title="새창">개인정보처리방침</a> &nbsp; | &nbsp; <a href="https://customer.gabia.com/?utm_source=ems&utm_medium=email&utm_term=footer&utm_campaign=notice&utm_content=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0"
                                            style="color:#767676; text-decoration:none;" target="_blank" title="새창">고객센터</a> </td>
                                </tr>
                                <tr>
                                    <td style="padding:30px 10px; font:12px/20px Malgun Gothic; color:#767676; text-align:center;"> (주)가비아 경기도 성남시 분당구 대왕판교로 660, B동 4층(삼평동)<br> 대표전화 1544-4370 메일/빌/이러닝 1661-4370<br><br> ⓒGabia Inc. All Rights Reserved. </td>
                                </tr>
                            </table>
                            <!-- //Footer -->
                        </td>
                        </tr>
                </table>
</body>
</html>
'''

<<<<<<< HEAD
data = {
    'hanname':'%회원이름%',
    'regist_date':'%작성일%',
    'service_list':[
        {'service_name':'%서비스명%',
        'domain':'%도메인%',
        'expiration_date':'%만기일%',
        'extension_expense':'%기준 가격%',
        'extension_period':'%기준 기간%',
        'extendable_limit':'%n%'
        },
         {'service_name':'%서비스명%',
        'domain':'%도메인%',
        'expiration_date':'%만기일%',
        'extension_expense':'%기준 가격%',
        'extension_period':'%기준 기간%',
        'extendable_limit':'%n%'
        },
         {'service_name':'%서비스명%',
        'domain':'%도메인%',
        'expiration_date':'%만기일%',
        'extension_expense':'%기준 가격%',
        'extension_period':'%기준 기간%',
        'extendable_limit':'%n%'
        }],
    'total_count':'3'
=======
# text_translated = text.translate({ord('{'):'{{', ord('}'):'}}'})
# print(text_translated)
# pystache.defaults.DELIMITERS를 통해 {{ → {로  변경하여 위 코드 제외함}

input = {
    'hanname':'조양아',
    'regist_date':'2018-06-01',
    'service_list':'22',
    'service_name':'웹호스팅',
    'domain':'gabia.com',
    'expiration_date':'2018-06-20',
    'extension_expense':'22,000원',
    'extension_period':'월',
    'extendable_limit':'19',
    'total_count':'1'
>>>>>>> parent of ce5c56f... add list
}

# input dictionary에 value에 해당하는 값을 DB에서 불러와야 함
# 아이디/서비스번호 입력 시 자동 완성되도록
# regist_date는 오늘 날짜(시스템 날짜?) 입력

pystache.defaults.DELIMITERS = ('{', '}') 
mail_text = pystache.render(text, input)
# print(mail_text)

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
<<<<<<< HEAD
smtp.login('jya9055@gmail.com', '{비밀번호}')
=======
smtp.login('{g메일 주소}', '{g메일 비밀번호}')
>>>>>>> parent of ce5c56f... add list

msg = MIMEMultipart('alternative')
msg.attach(MIMEText(mail_text, 'html'))
msg['Subject'] = '[가비아] 서비스 이용 기간을 연장해 주세요'
msg['To'] = 'jya@gabia.com'
smtp.sendmail('jya9055@gmail.com', 'jya@gabia.com', msg.as_string())

smtp.quit