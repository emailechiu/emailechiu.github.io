from turtle import *
from math import *

def Positive(R,r,g,b):
  if R==0.5:
      color(r,cg,cb)
      stamp()
  else:
      fd(R*factor)
      Positive(R/2,r+1,g,b)
      bk(R*factor)
      lt(120)
      fd(R*factor)
      Positive(R/2,r,g+1,b)
      bk(R*factor)
      lt(120)
      fd(R*factor)
      Positive(R/2,r,g,b+1)
      bk(R*factor)
      lt(120)

def Negative(R):
  shapesize(R,R)
  stamp()
  if R>1:
      lt(120)
      bk(R*factor)
      Negative(R/2)
      fd(R*factor)

      lt(120)
      bk(R*factor)
      Negative(R/2)
      fd(R*factor)
      
      lt(120)
      bk(R*factor)
      Negative(R/2)
      fd(R*factor)

mode("logo")
tracer(0,0)
shape('triangle')
size=32
factor=20/sqrt(3)
if 1:
    Positive(size/2,0,0,0)

if 0:
    shapesize(size,size)
    goto(-300,-300)
    stamp()
    fillcolor("white")
    lt(180)
    Negative(size/2)

    shapesize(size,size)
    goto(300,300)
    stamp()
    fillcolor("black")
    lt(180)
    Negative(size/2)
    update()
      
      

