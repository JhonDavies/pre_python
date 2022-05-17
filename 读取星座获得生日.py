# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


import re
s =""
while True:
    s = input("请输入星座中文名称(例如,双子座)")
    pattern = r'^[\u4E00-\u9FA5]+'
    o = re.match(pattern,s)
    if o !=None:
        s = s
        break
    else:
        print("星座输入有误，重新输入")
fo = open('PY301-SunSign.csv',"r")
ls = []
for i in fo:
    i =i.strip('\n')
    i =i.split(',')
    ls.append(i)
fo.close()
n = 0

for j in ls:
    for i in j:
        if i == s:
            num = j.index(i)
            break
    if i==s:
        break
    n +=1
start = ls[n][num+1]
end = ls[n][num+2]
print("{}的生日位于{}-{}之间".format(s,start,end))