import requests

headers = {
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
url1 = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1593260072150'
res1 = requests.get(url1)
pic1 = res1.json()

kind1 = pic1['data']

choice = input('请输入你要测试的范围')
for i in kind1:
    if i[1] == choice:
        choice1 = i[0]
        url2 = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+str(choice1)
        res2 = requests.get(url2,headers = headers)
        pic2 = res2.json()
        kind2 = pic2['data']
        for j in kind2:
            voc = j['content']
            print(voc)
            que = input('你是否认识它，认识输入y,不认识输入n')
            if que == 'y'
            