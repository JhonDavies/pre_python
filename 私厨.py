import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }

url = 'https://www.xiachufang.com/explore/'

res = requests.get(url,headers = headers)

pic = res.text
soup = BeautifulSoup(pic,'html.parser')

list0 = []
items = soup.find_all(class_ = 'info pure-u')
for i in items:
    list1 = []
    kind = i.find(class_ = 'name')
    name = kind.text
    kinds = kind.find('a')
    url1 = 'www.xiachufang.com'+str(kinds['href'])
    pei = i.find(class_ = 'ing ellipsis')
    peiliao = pei.find_all(target = '_blank')
    for j in peiliao:
        list1.append(j.text)
    list0.append(list1)
fo = open('100.txt','w',encoding= 'utf-8')

for k in range(25):
    a = name+'  '+url1
    b = list0[k]
    fo.write(a)
    fo.write(str(b))
    fo.write('\n')
fo.close()
  

    