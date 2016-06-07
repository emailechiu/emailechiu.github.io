#!/usr/bin/python3
from turtle import *
from canvasvg import *
mode("logo")
tracer(0)
R=100
begin_fill()
fillcolor('yellow')
circle(R,180)
circle(R/2,180)
circle(-R/2,180)
end_fill()
fillcolor('blue') 
begin_fill()
pu()
goto(-2*R,0)
pd()
circle(R,180)
circle(R/2,180)
circle(-R/2,180)
end_fill()
pu()
update()
saveall('yinyang.svg',Screen()._canvas)
exitonclick()