#!/usr/bin/python3
from turtle import *
clearscreen()
#tracer(0,0)
xmax=80
setworldcoordinates(-1,-1,xmax+1,1)
def f(x):
    return 3.9*x/xmax*(1-x/xmax)

def plot(fun, plot_range,color):
  pencolor(color)
  for x in plot_range:
      print(x,fun(x))
      goto(x,fun(x))


plot(f,range(xmax),'green')
#update()

