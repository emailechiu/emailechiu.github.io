from turtle import *
from canvasvg import *
for i in range(5):
    fd(200)
    rt(144)
saveall('5_star.svg',Screen()._canvas)
