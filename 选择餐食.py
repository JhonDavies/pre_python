import random
choice1=['小米粥','咖啡']
choice2=['米饭','面条']
choice3=['料理','烧烤']

answer=input('请问需要为你提供什么选择，1.早餐，2.午餐，3.晚餐')
if answer=='1':
    breakfast=random.choice(choice1)
    print(breakfast)
    
elif answer=='2':
    lunch=random.choice(choice2)
    print(lunch)
    
elif answer=='3':
    supper=random.choice(choice3)
    print(supper)