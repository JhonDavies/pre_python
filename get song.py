#get song.py
import requests
from bs4 import BeautifulSoup

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for j in range(1,6):
    params = {
    'ct': '24',
    'qqmusic_ver': '1298',
    'remoteplace': 'txt.yqq.lyric',
    'searchid': '95550914902596902',
    'aggr': '0',
    'catZhida': '1',
    'lossless': '0',
    'sem': '1',
    't': '7',
    'p': str(j),
    'n': '5',
    'w': '周杰伦',
    'g_tk_new_20200303': '5381',
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0'
    }
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 7.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
    res = requests.get(url,params = params,headers = headers)

    pic = res.json()
    one = pic['data']['lyric']['list']
    for i in one:
        novel = i['content']
        print(novel.replace('\n',' '))