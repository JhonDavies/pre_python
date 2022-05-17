#class and object
class Chinese:  #不必重复传参，传入的数据还可以被多次调用

    def __init__(self, name, birth, region):
        self.name = name   # self.name = '吴枫' 
        self.birth = birth  # self.birth = '广东'
        self.region = region  # self.region = '深圳'

    def born(self):
        print(self.name + '出生在' + self.birth)

    def live(self):
        print(self.name + '居住在' + self.region)    

person = Chinese('吴枫','广东','深圳') # 传入初始化方法的参数
person.born()
person.live()
#编写一个直观的好处就是参数的传递会比普通函数要省事很多，也不必考虑全局变量和局部变量，因为类中的方法可以直接调用属性。\
#既能包含操作数据的方法，又能包含数据本身。所以，代码的可复用性也更高。