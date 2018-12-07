from email_app import app
import smtpd
import smtplib
from email.message import EmailMessage
import os
from celery import Celery


@app.task
def sendemail():
    # 读取msg.txt内容, 发送出现gbk报错的话使用encoding='UFT-8'
    with open('msg.txt', 'r', encoding='UTF-8') as fp:
        # 创建 EmailMessage()实例
        msg = EmailMessage()
        # 设置要发送的内容
        msg.set_content(fp.read())

    msg['Subject'] = 'Test email'
    msg['From'] ='18814124132@139.com'
    msg['To'] = 'hupan0818@163.com'
    # 创建SMTP实例
    s = smtplib.SMTP(host='smtp.139.com', port=25)
    # 需要进行密码验证
    s.login(user='18814124132@139.com', password='slh201008')
    s.send_message(msg)
    s.quit()

