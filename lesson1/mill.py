#!/usr/bin/python3
from turtle import *
from math import *
from canvasvg import *
mode("standard")
tracer(0)
n=5
step=50

###bear
##begin_poly()
##color("red","blue")
##circle(step,360,20)
##pu()
##goto(3*step,0)
##pd()
##circle(step,360,20)
##pu()
##goto(1.5*step,0)
##rt(90)
##pd()
##fd(step)
##circle(step/4,180,10)
##end_poly()
##S=get_poly()
##register_shape("bear",S)
##b=Turtle(shape="bear")


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

def arc(start,end,angle,direction=1,steps=20,col='red'):
    pencolor(col)
    jumpto(start)
    segment=end-start
    ang_sin=degrees(asin(segment[1]/abs(segment)))
    ang_cos=degrees(acos(segment[0]/abs(segment)))
    ang_segment=copysign(ang_cos,ang_sin)
    seth(ang_segment-direction*angle/2)
    radius= abs(segment)/2/sin(radians(angle/2))
    circle(direction*radius,angle,steps) #short arc

def center(start,end,angle,direction=1,col='red'):
    arc(start,end,360-2*angle,direction,2,col)

def jumpto(d):
    pu()
    goto(d)
    pd()

for direction in [-1,1]:
    start=Vec2D(50,50)
    end=Vec2D(-100,-50)
    angle=90
    col=(direction/2+1/2,1/2-direction/2,0)
    arc(start,end,angle,direction,20,col)   # short arc
    arc(start,end,360-angle,direction,20,col)   # short arc
    arc(end,start,angle,direction,20,col) #long arc
    arc(start,end,angle,direction,2,col)   # sharp segment
    arc(end,start,360-angle,direction,2,col) #obtuse segment
    center(start,end,angle,direction,col)



update()
saveall('pattern.svg',Screen()._canvas)
exitonclick() 
