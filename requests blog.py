#requests blog.py
import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find_all(class_ = 'comment-content')

for i in items:
    kind = i.find('p')
    print(kind.text)