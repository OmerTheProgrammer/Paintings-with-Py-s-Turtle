import turtle
import time

sc = turtle.Screen()
global t
t = turtle.Turtle()
t.speed(50)
t.hideturtle()
def get_colors():
    color = input("heart color: ")
    if color in ["red","blue","green","black","orange"]:
        t.color(color)
        t.fillcolor(color)
def goto(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
def heart(n):
    t.circle(150,190)
    t.rt(100)
    if n == 2:
        return 2
    else:
       return heart(n+1)

get_colors()
goto(-20,260)
t.rt(90)
t.write(input("what to write? "),False,"center",("Arial", 40, "normal"))

goto(210,-10)
t.rt(228)

t.begin_fill()
heart(1)
t.lt(100)
t.fd(250)
t.lt(75.1)
t.fd(300)
t.end_fill()

goto(-20,-260)
t.write(input("write to who? "),False,"center",("Arial", 80, "normal"))

time.sleep(4)