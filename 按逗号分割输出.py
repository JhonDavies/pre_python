#Calhomework.py

Str = ""
num1 = 0
num2 = 0
num3 = 0
s = ""
for i in range(100,1000):
    Str = str(i)
    num1 = eval(Str[0])
    num2 = eval(Str[1])
    num3 = eval(Str[2])
    if pow(num1,3) +\
pow(num2,3) + pow(num3,3) == i:
        s += "{},".format(i)
print(s[:-1])