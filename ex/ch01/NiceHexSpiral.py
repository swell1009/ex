# NiceHexSpiral.py
# page 2
import turtle

colors = ['red', 'purple', 'blue',
          'green', 'yellow', 'orange', 'white']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 7])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(45)
