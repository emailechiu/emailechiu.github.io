#!/usr/bin/python3
from turtle import *
from math import *
from canvasvg import *
mode("logo")
tracer(0)
n=5
step=50
fillcolor('blue')
#begin_fill()
begin_poly()

# eyes
circle(step,360)
circle(-step,360)
lt(90)
pu()
fd(step)
pd()
circle(step/2)
pu()
rt(180)
fd(2*step)
pd()
circle(-step/2)

pu()
home()
rt(180)
fd(step)
pd()

# nose
fd(step/3)
circle(step/3,180)
pu()
circle(step/3,180)
pd()
circle(-step/3,180)
pu()
circle(-step/3,180)

fd(step/3)
pd()
# mouth
rt(90)
fd(step/3)
lt(90)
#begin_fill()
#fillcolor('red')
circle(step/3,180)
#end_fill()

# chin
pu()
goto(-3*step,-step/2)
rt(180)
pd()
circle(3*step,180)

# ears
pu()
home()
fd(step*1.2)
lt(90)
fd(step*3/2)
rt(45)
pd()
circle(step,180)
pu()
home()
fd(step*1.2)
lt(-90)
fd(step*3/2)
rt(-45)
pd()
circle(-step,180)

# eyebrows
pu()
home()
fd(step*1.2)
pd()
circle(step,60)
circle(step,-60)
circle(-step,60)
circle(-step,-60)

pu()
home()
fd(step*2.4)
pd()
circle(step,60)
circle(step,-60)
circle(-step,60)
circle(-step,-60)

end_poly()
#end_fill()
S=get_poly()
register_shape("bear",S)
#reset()
#b=Turtle(shape="bear")


###circle inside square
##fd(step)
##begin_poly()
##begin_fill()
##color('yellow','blue')
##circle(step,360,4)
##pu()
##lt(90)
##fd(step/3)
##rt(90)
##pd()
##circle(step/3,360,20)
##end_fill()
##end_poly
##S=get_poly()
##register_shape("donut",S)
##x=Turtle(shape="donut")
##fd(step)
##bk(step*n)
##
##begin_fill()
##color('yellow','blue')
##begin_poly()
##for j in range(1,n):
##  print(j,"in ",pos())
##  for i in range(n):
##    fd(step)
##    rt(360*j/n)
##  print(j,"ou ",pos())
##  #fd(step*2) 
##  print(j,"out",pos())
##end_fill()
##end_poly()
##S=get_poly()
##register_shape("pentagon",S)  
##t=Turtle(shape='pentagon')
##



update()
saveall('teddy.svg',Screen()._canvas)
exitonclick() 
