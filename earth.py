import turtle
sn = turtle.Screen()
t = turtle.Turtle()
t.speed(50)
colors = ["0","red","orange","tomato","saddle brown","lime green"]
for i in range(1,6):
    t.color(colors[i])
    for y in range(360):
        t.circle(i*25)
        t.rt(1)

