# 直接运行代码就好
import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':'2',
    'n':'10',
    'w':'周杰伦',       
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0' 
}
res = requests.get(url,params = params)
pic = res.json()

one = pic['data']['song']['list']

for i in one:
    print('歌曲名称为：'+' '+i['name'])
    print('歌曲所属专辑：'+' '+i['album']['name'])
    print('听歌链接'+' '+i['url']+' ')
    print('歌曲时长为:'+' '+str(i['interval'])+'秒'+'\n')

