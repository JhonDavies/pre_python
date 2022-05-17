import requests
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import re
x =[]
session = requests.session
session = requests.session()  
post_url = 'http://202.200.112.210/default2.aspx'
r = session.get(post_url)
cookies = r.headers['Set-Cookie'] 
cookies = cookies.strip('; path=/')  
yam_headers = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=ddeebpei15qafqvwy35wt0ac',
    'Host': '202.200.112.210',
    'Referer':'http://202.200.112.210/', 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
yzm_url = 'http://202.200.112.210/CheckCode.aspx'

yamdata = session.get(yzm_url, headers=yam_headers)#验证码  
tempIm = BytesIO(yamdata.content)  
im = Image.open(tempIm)  
im.show()  
Code = input('Please Enter Code:')
logindata = {
    '__VIEWSTATE':'dDwtNTE2MjI4MTQ7Oz6t4Y9oXTopXyTWshqxCcrXGG7H3g==',
    'txtUserName': '3190241059',
    'Textbox1':'',
    'TextBox2': 'weinanshi0116.',
    'txtSecretCode': Code,
    'RadioButtonList1':'%D1%A7%C9%FA',
    'Button1':'',
    'lbLanguage':'',
    'hidPdrs':'',
    'hidsc':'',
}
login_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '37',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ASP.NET_SessionId=ddeebpei15qafqvwy35wt0ac',
    'Host': '202.200.112.210',
    'Origin': 'http://202.200.112.210',
    'Referer': 'http://202.200.112.210/default2.aspx',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
login_headers['Cookie'] = cookies
post_url = 'http://202.200.112.210/default2.aspx'
d = session.post(post_url, data=logindata, headers=login_headers)#将账号，密码，验证码和表头Post上去，然后我们可以用过BeautifulSoup或者正则表达式，抓取d.text有用的信息，判断是否登录成功。
res=r'<title>(.*?)</title>'#获取标题的正则表达式
x=re.findall(res,d.text)#pat
if(x[0]=="欢迎使用正方教务管理系统！请登录"):print("登陆失败")
else:
    print("登陆成功")
    #抓一下名字
    catch='<span id="xhxm">(.*?)</span></em>'
    name=re.findall(catch,r.text)
    name=name[0]
    name=name[:-2]
    print(name)

