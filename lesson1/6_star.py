from turtle import *
from math import *
from canvasvg import *
side=100
radius=side/sqrt(3)
print(pos())
fd(side)
rt(120)
print(pos())
fd(side)
rt(150)
print(pos())
fd(2*radius)
lt(150)
print(pos())
fd(side)
lt(120)
print(pos())
fd(side)
lt(150)
fd(2*radius)
print(pos())
saveall('6_star.svg',Screen()._canvas)
exitonclick()


