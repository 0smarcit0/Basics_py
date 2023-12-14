from turtle import*

import turtle as t
from random import random




bgcolor("black")
color("red")
up()
goto(-50,50)
down()
speed(1)
pensize(10)

fd(50)
back(50)
right(90)
fd(100)
right(90)
fd(50)
bk(50)
right(90)
fd(50)
right(90)
fd(50)
right(90)
fd(50)
back(50)
left(90)
back(100)
left(90)
fd(50)
hideturtle()

clearscreen()




for i in range(5):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

clearscreen()
color("red")
fillcolor("yellow")
begin_fill()
speed(10)
while True:
    fd(200)
    left(170)
    if abs(pos()) <1:
        break

end_fill()
clearscreen()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
backward(100)
right(90)
forward(60)

clearscreen()
speed(5)
for steps in range(100):
    for c in ("blue", "red", "green"):
        color(c)
        forward(steps)
        right(30)


mainloop()

