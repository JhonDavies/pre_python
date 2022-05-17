import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = '958964640@qq.com'
password = 'ysocpzarsyjdbcia'
receiver = input('请输入收件人的qq：')+'@qq.com'

def food():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'Host': 'www.xiachufang.com'
    }
    res = requests.get('http://www.xiachufang.com/explore/',headers = headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    kinds = soup.find(class_ = 'normal-recipe-list')
    kind1 = kinds.find(class_ = 'list')
    kind2 = kind1.find_all('li')
    lists = []
    for i in kind2:
        kind3 = i.find(class_ = 'info')
        name = kind3.find(class_ = 'name')
        href = 'www.xiachufang.com/explore'
        liao = kind3.find(class_ = 'ing')
        test = '菜品名称为：'+' '+name.text+'\n'+'配料为：'+'\n'+liao.text.strip()+'\n'+'具体网页：'+' '+href+'\n'
        lists.append(test)
    tests = ''.join(lists)
    return tests

def send_email(tests):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= tests
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日份最新菜谱'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    tests = food()
    send_email(tests)
    print('任务完成')

job()    
