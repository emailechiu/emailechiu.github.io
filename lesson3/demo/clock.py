#!/usr/bin/python3
from turtle import *
from datetime import *
mode("logo")
#register_shape('clock_hand',((0,0),(10,0),(10,1),(11,0),(10,-1),(10,0)))
register_shape('clock_hand',((0,0),(0,100),(-10,100),(0,110),(10,100),(0,100)))
register_shape("dot", ((-3,-3), (-3,3), (3,3), (3,-3)))
register_shape("tri", ((-3, -2), (0, 3), (3, -2), (0, 0)))
clearscreen()
hour_hand=Pen(shape='clock_hand')
hour_hand.shapesize(0.7,0.7,3)
hour_hand.color("gray","blue")
#hour_hand.seth(0)
minute_hand=Pen(shape='clock_hand')
minute_hand.shapesize(0.9,0.9,2)
minute_hand.color("yellow","magenta")
#minute_hand.seth(90)
second_hand=Pen(shape='clock_hand')
second_hand.shapesize(1,1,1)
#second_hand.seth(90)
second_hand.color("green","red")
center=Pen(shape='dot')
center.shapesize(2,2,2)
center.color("orange","black")

def tick():
       t=datetime.today()
       second_hand.seth(t.second/60*360)
       minute_hand.seth(t.minute/60*360+t.second/3600*360)
       hour_hand.seth(t.hour/12*360+t.minute/12/60*360)
       ontimer(tick,1000)
       done()

tick()
       


