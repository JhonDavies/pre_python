import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '958964640@qq.com'
password = 'ysocpzarsyjdbcia'

# 收信方邮箱
to_addr = '409530821@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

txte='''Computer is the most useful helper for us in life and there are a lot of programming langueage around the world.
However c is suitable for new people,
so you are supposed to study it seriously.'''
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(txte,'plain','utf-8')

msg['From'] = Header('爸爸')
msg['To'] = Header('儿子')
msg['Subject'] = Header('Please work hard in c')


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()