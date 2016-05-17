#!/usr/bin/python3
from turtle import *
from time import *
clearscreen()
tracer(1,0)

def serial_branch(parent,step):
  if step>=2:
    parent.fd(step)
    child=parent.clone()
    child.lt(120)
    parent.rt(120)
    serial_branch(parent,step/2)
    serial_branch(child,step/2)

def parallel_branch(plist,step):
   print(len(plist)," ",step)
   if step>=2:
     if step>=64:
       left_angle=60
       right_angle=60
     else:
       if step>=2:
         left_angle=120;
         right_angle=120  
     qlist=[]
     for parent in plist:
        parent.fd(step)
        child=parent.clone()
        parent.lt(left_angle)
        child.rt(right_angle)
        qlist.append(child)
     plist+=qlist
     parallel_branch(plist,step/1.73)

grandpa = Turtle()
grandpa.speed(0)
grandpa.hideturtle()
grandpa.pu()
grandpa.goto(-256,-200)
grandpa.pencolor("blue")
grandpa.pd()
serial_branch(grandpa,256)
#parallel_branch([grandpa],256)

grandpa.pu()
grandpa.home()
grandpa.pencolor("red")
grandpa.goto(256,-200)
grandpa.pd()
#serial_branch(grandpa,256)
parallel_branch([grandpa],256)
#update()
exitonclick()
    
    

