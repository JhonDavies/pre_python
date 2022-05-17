import random
guess = ''
while guess not in (0,1):
    print('Guess the coin toss! ENter heads or tails:')
    guess = eval(input())
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
    print('you got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('you got it!')
    else:
        print('Nope.you are really bad at this game.')