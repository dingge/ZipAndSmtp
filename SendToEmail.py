import datetime
import time
import sys
import mimetypes
import smtplib
import email.MIMEMultipart
import email.MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.Utils import COMMASPACE,formatdate
from email.mime.image import MIMEImage

reload(sys)
sys.setdefaultencoding('utf8')

def SendMail():
       msg=MIMEMultipart()
       msg['From']='fireburnbird@163.com'
       ToList = ['529077434@qq.com']
       msg['Subject'] = 'The latest sleep quality report'
       text=MIMEText('Do not look at me ,pay attention to the attach.',_charset='utf-8')
       msg.attach(text)

       file_name = 'Udisk.zip'
       ctype,encoding = mimetypes.guess_type(file_name)
       if ctype is None or encoding is not None:
              ctype = 'application/octet-stream'
       maintype,subtype = ctype.split('/',1)

       att = MIMEImage(open(file_name,'rb').read(),subtype)
       print ctype,encoding
       att['Content-Disposition']='attachment;filename=%s' % file_name
       msg.attach(att)

       smtp=smtplib.SMTP()
       smtp.connect('smtp.163.com')
       smtp.login('xxxxxxx','xxxxxxx')
       print 'Login Success,Ready to transport file.'
       smtp.sendmail(msg['From'],ToList,msg.as_string())
       print 'Congradulation,Your mail has benn sent succesfully.'
       smtp.close()


