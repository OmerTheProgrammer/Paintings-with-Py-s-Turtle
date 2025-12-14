import turtle
sn=turtle.Screen()
t=turtle.Turtle()
t.isvisible(True)
t.speed(20)
x=0

for i in range(5):
    for j in range(36):
        t.fd(50+x)
        t.rt(90)
        t.fd(25+x)
        t.rt(180)
        t.fd(50+x)
        t.rt(180)
        t.fd(25+x)
        t.rt(90)
        t.fd(50+x)
        t.rt(10)
    t.lt(75)
    t.penup()
    t.fd(50+x)
    t.pendown()
    x =+ 50
