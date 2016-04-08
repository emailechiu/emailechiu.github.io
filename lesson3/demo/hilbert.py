from turtle import *
from math import *

def Positive(R,r,g,b):
  if R==0.5:
      color(r,g,b)
      stamp()
  else:
      fd(R*factor)
      Positive(R/2,(r+b)/2,(g+b)/2,b)
      bk(R*factor)

      lt(120)
      fd(R*factor)
      Positive(R/2,r,(r+g)/2,(r+b)/2)
      bk(R*factor)

      lt(120)
      fd(R*factor)
      Positive(R/2,(g+b)/2,g,(r+g)/2)
      bk(R*factor)
      lt(120)

def Positive_initial(R,r,g,b,d):
  if R==0.5:
      color(r,g,b)
      stamp()
  else:
      fd(R*factor)
      Positive_initial(R/2,r+R/size*(d%3==0),g+R/size*((d+1)%3==0),b+R/size*((d+2)%3==0),d)
      bk(R*factor)

      lt(120)
      fd(R*factor)
      d+=1
      Positive_initial(R/2,r+R/size*(d%3==0),g+R/size*((d+1)%3==0),b+R/size*((d+2)%3==0),d)
      bk(R*factor)

      lt(120)
      fd(R*factor)
      d+=1
      Positive_initial(R/2,r+R/size*(d%3==0),g+R/size*((d+1)%3==0),b+R/size*((d+2)%3==0),d)
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
    Positive_initial(size/2,0,0,0,0)

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
      
exitonclick()     

