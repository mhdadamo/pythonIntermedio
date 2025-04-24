from turtle import *
from colorsys import *

speed(-25)
bgcolor("black")
h=0
for i in range(16):
    for j in range(18):
        c=hsv_to_rgb(h,1,1)
        color(c)
        h+=0.005

        rt(90)
        circle(150- j,90)

        lt(90)
        circle(150- j,90)

        rt(180)
    circle(40,24)

h = 0
penup()
setposition(0, 40)
pendown()

for i in range(36):
    c = hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.1

    circle(20)
    rt(10)
hideturtle()
done()
