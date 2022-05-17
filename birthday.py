import turtle
import random
from turtle import *
import time
from playsound import playsound
import threading

# set the background color for the page
def play_music():
    
    playsound('2.wav')

def main():
    bg = turtle.Screen()
    bg.bgcolor("light blue")
    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(75)

# draw lines
    tommy.penup()
    tommy.goto(-190, -180)
    tommy.color("yellow")
    tommy.pensize(6)
    tommy.pendown()
    tommy.goto(190,-180)
    tommy.penup()
    time.sleep(3)
    
    tommy.penup()
    tommy.goto(-160, -150)
    tommy.color("purple")
    tommy.pensize(6)
    tommy.pendown()
    tommy.goto(160,-150)
    tommy.penup()
    time.sleep(3)
    
    tommy.penup()
    tommy.goto(-130, -120)
    tommy.color("teal")
    tommy.pensize(6)
    tommy.pendown()
    tommy.goto(130,-120)
    tommy.penup()
    time.sleep(3)
# draw cake
    tommy.goto(-74,-110)
    tommy.pendown()
    tommy.color("white")
    tommy.goto(50,-110)
    tommy.left(90)
    tommy.forward(60)
    tommy.left(90)
    tommy.forward(125)
    tommy.left(90)
    tommy.forward(60)
    tommy.penup()
    time.sleep(3)
#draw candles
    tommy.goto(-60, -40)
    tommy.color("aquamarine")
    tommy.pendown()
    tommy.pensize(3)
    tommy.goto(-60, -20)
    tommy.penup()
    time.sleep(3)

    tommy.goto(-40, -40)
    tommy.color("yellow")
    tommy.pendown()
    tommy.pensize(3)
    tommy.goto(-40, -20)
    tommy.penup()
    time.sleep(3)

    tommy.goto(-20, -40)
    tommy.color("green")
    tommy.pendown()
    tommy.pensize(3)
    tommy.goto(-20, -20)
    tommy.penup()
    time.sleep(3)

    tommy.goto(0, -40)
    tommy.color("pink")
    tommy.pendown()
    tommy.pensize(3)
    tommy.goto(0, -20)
    tommy.penup()
    time.sleep(3)

    tommy.goto(20, -40)
    tommy.color("blue")
    tommy.pendown()
    tommy.pensize(3)
    tommy.goto(20, -20)
    tommy.penup()
    time.sleep(3)



    tommy.goto(-110, 35)
    tommy.color("red")
    tommy.pendown()
    tommy.write("Happy Birthday!","24pt bold")
    tommy.penup()
    tommy.goto(-250, 250)
    
    turtle.write('''誕生日おめでとう！
    Hao Liu ''',font=('red',25,'normal'))
    turtle.done()
    time.sleep(3)

threads = []
t1 = threading.Thread(target = play_music)
threads.append(t1)
t2 = threading.Thread(target= main)
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()
