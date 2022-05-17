import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'song list'
sheet['A1'] = '歌曲名称'
sheet['B1'] = '所属专辑'
sheet['C1'] = '播放时长'
sheet['E1'] = '详细链接'
sheet.column_dimensions['A'].width = 12.78
sheet.column_dimensions['B'].width = 24.22
headers = {
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=69602973045051612&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
pic = res.json()

kinds = pic['data']['song']['list']
for i in kinds:
    name = i['name']
    type1 = i['album']['title']
    time = i['interval']
    url = 'https://y.qq.com/n/yqq/song/'+i['mid']+'.html'
    list1 = [name,type1,time,'',url]
    sheet.append(list1)

wb.save('歌单信息.xls')