from turtle import*
import turtle as t


bgcolor("black")
pencolor("white")
speed(20)
hideturtle()
#fd(100)
#t.circle(100,200,600)
#t.clear()
#penup()
#home()
pendown()
for i in range(216):
    for c in ("blue", "red", "green"):
     color(c)
     left(45+i)
     fd(100)
     right(90+i)
     fd(50)


mainloop()
