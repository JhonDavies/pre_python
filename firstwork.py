#firstwork.py

def fun1():
    fo = open("py01.csv","w")
    title = "商品编号,商品名称,商品单价,商品库存量\n"
    fo.write(title)
    Str = ""
    while Str !="0\n":
        Str = input("输入商品信息以逗号分隔,输入0结束")
        Str = Str +'\n'
        if Str == '0\n':
            break
        fo.write(Str) 
    fo.close()
    print("功能1执行完毕")
def fun2():#按编号排序
    fo = open("py01.csv","r")
    fil = fo.read()
    txt =fil.split("\n")
    num = len(txt)
    counts = {}
    for j in range(1,num):
        i = txt[j].split(",")
        counts[i[0]] = i[1:]
    items = list(counts.items())
    items.sort()
    num = len(items)

    for i in range(1,num):
        nov =items[i]
        test = nov[0]+','+",".join(nov[1])+'\n'
        print(test)
    fo.close()   
    print("功能2执行完毕")
def fun3():#按库存数量排序
    fo = open("py01.csv","r")
    fil = fo.read()
    txt =fil.split("\n")
    num = len(txt)
    counts = {}
    for j in range(1,num):
        i = txt[j].split(",")
        counts[i[-1]] = i[:]
    items = list(counts.items())
    items.sort()
    num = len(items)
    for i in range(1,num):
        nov =items[i]
        test = ",".join(nov[1])+'\n'
        print(test)
    fo.close()   
    print("功能3执行完毕")

def fun4():
    print("{:-^20}".format("1按照输入顺序输出"))
    print("{:-^20}".format("2按照编号顺序输出"))
    print("{:-^20}".format("1按照库存顺序输出"))
    num = input("please")
    if num =="1":
        pass
    elif num =="2":
        
        fo = open("py01.csv","r")
        op = open("py02.csv","w")
        title = "商品编号,商品名称,商品单价,商品库存量\n"
        op.write(title)
        fil = fo.read()
        txt =fil.split("\n")
        num = len(txt)
        counts = {}
        for j in range(1,num):
            i = txt[j].split(",")
            counts[i[0]] = i[:]
        items = list(counts.items())
        items.sort()
        num = len(items)
        
        for i in range(1,num):
            nov =items[i]
            test = ",".join(nov[1])+'\n'
            op.write(test)
        fo.close()
        op.close()
        print("已输出py02.csv文件")
    elif num =="3":
        
        fo = open("py01.csv","r")
        op = open("py03.csv","w")
        title = "商品编号,商品名称,商品单价,商品库存量\n"
        op.write(title)
        fil = fo.read()
        txt =fil.split("\n")
        num = len(txt)
        counts = {}
        for j in range(1,num):
            i = txt[j].split(",")
            counts[i[-1]] = i[:]
        items = list(counts.items())
        items.sort()
        num = len(items)
        for i in range(1,num):
            nov =items[i]
            test = ",".join(nov[1])+'\n'
            op.write(test)
        fo.close()
        op.close()
        print("已输出py03.csv文件")

print("{:*^27}".format("系统功能菜单"))
print("*     1-----------输入商品信息    *")
print("*     2-----------按编号排序      *")
print("*     3-----------按库存排序      *")
print("*     4-----------输出商品信息    *")
print("*     0-----------退出系统        *")
print("{:*^33}".format(""))

choice =""
while choice !="0":
    choice = input("选择功能")
    if choice == "1":
        fun1()
    elif choice == "2":
        fun2()
    elif choice == "3":
        fun3()
    elif choice =="4":
        fun4()
    elif choice =="0":
        break
    else:
        print("输入数字错误")

