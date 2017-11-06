#=coding:utf-8
"""
function:
    send mail by python
author:
    lzpdzlzpdz
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.hotmail.com"  #设置服务器
mail_port = 25
mail_user="lzpdzlzpdz@hotmail.com"    #用户名
mail_pass="xxxxxx"   #口令 
sender = 'lzpdzlzpdz@hotmail.com'
receivers = ['lzpdzlzpdz@hotmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
def send_mail(message): 
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
        
def send_html_mail():
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("python邮件发送教程", 'utf-8')
    message['To'] =  Header("测试", 'utf-8')
     
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
 
    #发送邮件
    send_mail(message)

        
if __name__ == '__main__':
    print 'Doing...'
    send_html_mail()
    print 'Done!'
    
    