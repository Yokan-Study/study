import smtplib
from email.mime.text import MIMEText
from email import utils

me = 'kmkgabia@gmail.com'
you = 'kmk@gabia.com'
contents = voc

msg = MIMEText(contents, _charset='UTF-8')
msg['Subject'] = voc_title
msg['From'] = me
msg['To'] = you

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('kmkgabia@gmail.com', 'pw hidden')
smtp.sendmail('kmkgabia@gmail.com', 'kmk@gabia.com', msg.as_string())

smtp.quit()

