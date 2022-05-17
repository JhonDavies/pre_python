# requests the information of books .py
import requests
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find_all(class_ = 'books')

file1 = open('pa.txt','w',encoding= 'utf-8')


for i in items:
    kind = i.find('h2')
    title = i.find(class_ = 'title')
    brief = i.find(class_ = 'info')
    
    file1.write(kind.text)
    file1.write(',')
    file1.write(title.text)
    file1.write(',')
    file1.write(title['href'])
    file1.write(',')
    file1.write(brief.text)
    file1.write('\n')
file1.close()