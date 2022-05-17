#bmi.py
height,weight = eval(input("请输入身高（米）和体重（kg）的数值【用逗号分隔】"))
bmi = weight/pow(height,2)

if bmi < 18.5:
    who,nat = "偏瘦","偏瘦"
print("%s,%s",who,nat)