import turtle

t = turtle.Turtle()
t.fillcolor("blue")
t.color("blue")
t.speed(50) 
t.pensize(10)
def go_to(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
go_to(-770,370)
for i in range(2):
    t.begin_fill()
    for i in range(2):
        t.fd(1600)
        t.rt(90)
        t.fd(100)
        t.rt(90)
    t.end_fill()
    go_to(-770,-260)
go_to(55,75)
for i in range(3):
    t.rt(120)
    t.fd(150)
go_to(55,-15)
for i in range(3):
    t.lt(120)
    t.fd(150)
t.ht()
