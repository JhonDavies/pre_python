import requests
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 7.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

}
res = requests.get('https://movie.douban.com/top250?start=0&filter=',headers = headers)
pic = res.text

soup = BeautifulSoup(pic,'html.parser')
items = soup.find_all(class_ = 'item')

fo = open('豆瓣top25.txt','w',encoding = 'utf-8')
for item in items:
    kinds = item.find(class_ = 'pic')
    kin = kinds.find('em')
    num = kin.text
    kind = item.find(class_ = 'title')
    name = kind.text
    piz = item.find(class_ = 'rating_num')
    scores = piz.text
    pix = item.find(class_ = 'inq')
    viewpoint = pix.text
    piv = item.find(class_ = 'hd')
    pib = piv.find('a')
    urll = pib['href']
    a = num+' '+'电影名:'+' '+name+' '+'评分为：'+' '+scores+'\n'+viewpoint+'\n'+'观影链接'+' '+urll+'\n'
    fo.write(a)
fo.close()