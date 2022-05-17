# requests bookstore.py
import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find(class_ = 'nav nav-list')
item = items.find('ul')
kind = item.find_all('li')

for i in kind:
    kinds = i.text
    print(kinds.strip()) #str.strip()可以去掉str中，字符前空格与字符后的换行