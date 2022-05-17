import requests

session = requests.session()
url1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
data = {
    'log': 'crawer222',
    'pwd': '3190241059',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}

session.post(url1,headers = headers,data = data)

url2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_ = {
    'comment': input('请输入要发表的评论'),
    'submit': '发表评论',
    'comment_post_ID': '20',
    'comment_parent': '0'
}
session.post(url2,headers = headers,data = data_)