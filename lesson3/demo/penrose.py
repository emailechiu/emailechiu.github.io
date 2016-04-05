from turtle import *
from math import *
mode("standard")
radius=100
angle=72
sides=25
begin_poly()
goto(radius*cos(radians(-angle)/2),radius*sin(-radians(angle)/2))
seth(angle/2+360/sides)
circle(radius,angle,sides)
home()

