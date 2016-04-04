
from turtle import *
from math import *
def drawPolygon(t,sides,start,end,radius=100,x=0,y=0):
  mode("standard")
  angle = copysign(360/sides,end-start)
  step = radius * 2 * sin(pi/180 * angle/2)
  step_abs = copysign(step, 1)
  start_angle=  -90+start* angle
  end_angle = -90+end*angle
  total_length = copysign((end-start)*step,1)
  #print(sides," ",radius," ",step," ",total_length)
  t.up()
  t.goto(x+radius*cos(pi/180*start_angle),y+radius*sin(pi/180*start_angle))
  t.down()
  t.seth(angle/2+start*angle)
  while total_length>=0:
     t.forward(copysign(min(step_abs,total_length),end-start))
     t.left(angle)
     total_length-=step_abs
     #print(total_length)
  t.goto(x+radius*cos(pi/180*start_angle),y+radius*sin(pi/180*start_angle))
  mode("logo")
 
def stampPolygon(t,sides,end,radius=100,x=0,y=0,dir=1,tilt_factor=1.5):
  #print(radius," ",x," ",y)
  t.pu()
  t.goto(x,y)
  t.pd()
  t.write("tilt_factor= "+str(tilt_factor),align="center")
  angle = dir*360/sides
  step = radius * 2 * sin(pi/180 * angle/2)
  start_angle= -90 - angle/2
  t.up()
  t.goto(x+radius*cos(pi/180*start_angle),y+radius*sin(pi/180*start_angle))
  t.down()
  t.seth(90+angle/2)
  t.tilt(angle/2)
  for x in range(0,end):  
     t.stamp()
     t.forward(step)
     t.left(angle)
     t.tilt(angle*tilt_factor)
 
