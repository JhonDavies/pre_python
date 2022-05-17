import requests
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'song list'
sheet['A1'] = '歌曲名称'
sheet['B1'] = '所属专辑'
sheet['C1'] = '播放时长(秒)'
sheet['E1'] = '播放链接'
sheet.column_dimensions['A'].width = 18.22
sheet.column_dimensions['B'].width = 25.11

headers = {
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for i in range(1,6):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '64266274320851794',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i),
        'n': '10',
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
    res = requests.get(url,params= params,headers = headers)
    pic = res.json()
    kinds = pic['data']['song']['list']
    for j in kinds:
        name = j['name']
        type1 = j['album']['name']
        time = j['interval']
        urll = 'https://y.qq.com/n/yqq/song/'+j['mid']+'.html'
        lists = [name,type1,time,'',urll]
        sheet.append(lists)

wb.save('歌曲信息.xls')