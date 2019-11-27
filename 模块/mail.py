# coding= utf-8
"""

"""
import smtplib
from email.mime.text import MIMEText
"""
服务器
发送邮箱的地址
授权密码（不等于登录密码）：登录邮件设置

转为邮件的文本
"""
SMTPserver= "smtp.163.com"
sender ="aasun.110@163.com"
password ="sun123456"
message = "tony is good man"
msg = MIMEText(message)
mm = MIMEText()
# 邮件主题
msg["Subject"] = "handsome"
# 邮件的发送
msg["From"] = sender
#连接服务器
mailServer = smtplib.SMTP(SMTPserver, 25)
# 登录
mailServer.login(sender, password)
# 发送邮件
mailServer.sendmail(sender, [sender], msg.as_string())
mailServer.quit()

