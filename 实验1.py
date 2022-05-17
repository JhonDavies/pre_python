import requests
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

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

yamdata = session.get(yzm_url, headers=yam_headers)  
tempIm = BytesIO(yamdata.content)  
im = Image.open(tempIm)  
im.show()  
Code = input('Please Enter Code:')
logindata = {
    'txtUserName': '3190241059',
    'TextBox2': 'weinanshi0116.',
    'txtSecretCode': Code
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
d = requests.post(post_url, data=logindata, headers=login_headers)
