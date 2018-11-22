# ColorSpiral.py
# Page 20
import turtle

t = turtle.Pen()
turtle.bgcolor("black")
# You can choose between 2 and 6(Max) sides for some cool shapes!
sides = 3
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
