#=coding:utf-8
"""
function:
    regex function
author:
    lzpdzlzpdz
"""

import smtplib  
from email.mime.text import MIMEText  
  
sender = 'yutou'  
receiver = 'lzpdz'  
subject = 'python email test'  
smtpserver = 'smtp.sina.cn'  
username = 'lzpdzlzpdz@sina.cn' 
password = '139zhuyu'  
  
msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')  
  
msg['Subject'] = subject  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.sina.cn')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

