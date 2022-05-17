# class.py
class Teacher():
    def __init__(self,face = '严肃'):
        self.face = face
    def fact(self):
        print("我是一名人民教师")

class Father():
    def __init__(self,face = '和蔼'):
        self.face = face
    def fact(self):
        print('我要严格的教育你')

class People1(Father,Teacher):
    def __init__(self,face = 'gentle'):
        Father.__init__(self,face)

class People2(Teacher,Father):
    pass

time3 = People1()
time4 = People2()
print(time3.face)
print(time4.face)