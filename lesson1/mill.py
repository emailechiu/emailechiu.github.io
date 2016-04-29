#!/usr/bin/python3
from turtle import *
from canvasvg import *
from time import sleep
mode("logo")
speed(1)
fillcolor('red')
begin_poly()
pensize(3)
pencolor('green')
rt(20)
for i in range(3):
    fd(100)
    lt(90)
    circle(100,40) 
    rt(90)
    bk(100)
    lt(80)
lt(20)
end_poly()
register_shape('mill',get_poly())
clear()
shape('mill')
bk(200)
pencolor('blue')
pensize(20)
fd(200)

for i in range(30):
    rt(12)

saveall('mill.svg',Screen()._canvas)
exitonclick()
