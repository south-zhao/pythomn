"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time : 2023/7/24 15:07
    @Author : south(南风)
    @File : 邮件.py
    Describe:
    -*- coding: utf-8 -*-
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '2252585312'
mail_pass = 'ttlkhelsdcuydihj'

sender = '2252585312@qq.com'
receivers = ['2004@snnu.edu.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...,不知道你能不能收到信息，验证码为3366', 'plain', 'utf-8')
message['From'] = Header("south", 'utf-8')  # 发送者
message['To'] = Header("南风", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
