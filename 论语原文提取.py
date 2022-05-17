fo = open("论语.txt","r",encoding="utf-8")
str1 =""
for lines in fo:
    lines = lines.strip("\n")
    lines = lines.strip("  ")
    if len(lines) ==0:
        continue
    str1 = str1+lines+','
str1 = str1.strip(",")
lists = str1.split(",")
str1 =""
num1 =[i for i,x in enumerate(lists) if x== '【原文】']
fil = open("论语-原文.txt","w",encoding="utf-8")  
for j in num1:
    str1 = lists[j+1]+'\n'
    fil.write(str1)
fo.close()
fil.close()  