#!/usr/bin/python3
from turtle import *
clearscreen()
tracer(0,0)
grandpa = Turtle()
grandpa.hideturtle()
def branch(parent,step):
  if step>=2:
    parent.fd(step)
    child=parent.clone()
    child.lt(45)
    parent.rt(45)
    branch(parent,step/2)
    branch(child,step/2)

branch(grandpa,128)
update()
exitonclick()
    
    

