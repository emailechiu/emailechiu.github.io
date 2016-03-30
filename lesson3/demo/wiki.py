#!/usr/bin/python3
from turtle import *
tracer(0,0)
def mn_eck(n, size):
  for i in range(n):
     rt(360./n)
     circle(size)
bgcolor("black")
pencolor("red")
pensize(3)
mn_eck(36, 100)
update()
done()
