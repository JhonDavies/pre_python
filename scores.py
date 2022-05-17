import csv


scores = []
n = eval(input("需要输入多少个学生的成绩"))
for i in range(n):
    lists = []
    name = input("请输入学生姓名")
    num = input("请输入学生学号")
    chinese = input("请输入学生中文成绩")
    lists.append(name)
    lists.append(num)
    lists.append(chinese)
    scores.append(lists)
f = open('scores.csv','w')
head = ['姓名','学号','中文成绩']
f.write(','.join(head)+'\n')
for i in range(n):
    f.write(','.join(scores[i])+'\n')
f.close()

