#!/usr/bin/python3
from turtle import *
from math import *
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

##
##
##
##a=Turtle(shape='mill')
##a.goto(-100,-100)
##a.color('black','green')
##b=Turtle(shape='mill')
##b.color('black','red')
##b.setpos(100,-100)
##c=Turtle(shape='square')
##c.shapesize(1,1)
##c.color('grey','blue')
##c.setpos(100,-100)
##clear()
##tracer(1)
##for i in range(1,30):
##    c.sety(-100+i*5)
##    c.shapesize(1,i/2)
##    a.rt(9)
##    a.sety(-100+i*10)
##    b.lt(9)
##    b.sety(-100+i*10)


