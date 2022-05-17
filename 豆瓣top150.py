import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '豆瓣top25'
sheet['A1'] = '序号'
sheet['B1'] = '电影名称'
sheet['C1'] = '类型'
sheet['D1'] = '评分'
sheet['E1'] = '推荐语'
sheet['G1'] = '详细页面'
sheet.column_dimensions['C'].width = 29
sheet.column_dimensions['E'].width = 93
sheet.column_dimensions['B'].width = 20


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
for k in range(6):
    page = k*25
    res = requests.get('https://movie.douban.com/top250?start='+str(page)+'&filter=',headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    kinds = soup.find(class_ = 'grid_view')
    kind = kinds.find_all('li')
    for i in kind:
        kind1 = i.find(class_ = 'hd')
        kind2 = kind1.find('a')
        href = kind2['href']
        name = kind1.find(class_ = 'title')
        kind3 = i.find(class_ = 'bd')
        kind4 = kind3.find('p')
        kind5 = kind4.text.strip()
        kind6 = kind5[kind5.rfind('/')+2:]
        type1 = kind6.strip()
        num = i.find(class_ = 'pic')
        kind7 = i.find(class_ = 'star')
        scores = kind7.find(class_ = 'rating_num')
        mind = i.find(class_ = 'inq')
        lists = [num.text,name.text,type1,scores.text,mind.text,' ',href]
        sheet.append(lists)

wb.save('豆瓣top150.xls')