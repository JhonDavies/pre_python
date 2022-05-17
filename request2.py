# request2.py
import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find_all(class_ = 'entry-header')

for i in items:
    title = i.find('h2')
    print(title.text)
    kind = i.find(class_ = 'entry-meta')
    kinds = kind.find('a')
    time = kinds.find(class_ = 'entry-date published')
    print(time.text)
    connect = kind.find('a')
    print(connect['href'])