import requests
from bs4 import BeautifulSoup
from urllib.request import quote   #生成标准url

answer = input("你想要什么电影的下载链接")
ans = answer.encode('gbk')
an = quote(ans)
url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+an

res = requests.get(url)
pic = res.text

