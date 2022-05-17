import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'cookbook'
sheet['A1'] = '菜名'
sheet['B1'] = '配料'
sheet['C1'] = '具体做法链接'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
res = requests.get('http://www.xiachufang.com/explore/',headers = headers)
soup = BeautifulSoup(res.text,'html.parser')
kinds = soup.find(class_ = 'normal-recipe-list')
kind = kinds.find_all('li')
for i in kind:
    name1 = i.find(class_ = 'name')
    name2 = name1.find(target = '_blank')
    href = 'http://www.xiachufang.com/explore/'+name2['href']
    need1 = i.find(class_ = 'ing ellipsis')
    need2 = need1.find_all(target = '_blank')
    list1 = []
    for j in need2:
        need3 = j.text
        list1.append(need3)
    
    lists = [name2.text,str(list1),href]
    sheet.append(lists)

wb.save('菜谱.xls')