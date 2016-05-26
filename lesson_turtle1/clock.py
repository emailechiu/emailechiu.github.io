#!/usr/bin/python3
from turtle import *
from datetime import *
from canvasvg import *
mode("logo")
clearscreen()
tracer(0,0)
#hideturtle()
#register_shape('clock_hand',((0,0),(10,0),(10,1),(11,0),(10,-1),(10,0)))
register_shape('clock_hand',((0,0),(0,100),(-10,100),(0,110),(10,100),(0,100)))
register_shape("dot", ((-3,-3), (-3,3), (3,3), (3,-3)))
register_shape("tri", ((-3, -2), (0, 3), (3, -2), (0, 0)))
hour_hand=Pen(shape='clock_hand')
hour_hand.shapesize(0.7,0.7,3)
hour_hand.color("gray","blue")
#hour_hand.seth(0)
minute_hand=Pen(shape='clock_hand')
minute_hand.shapesize(0.9,0.9,2)
minute_hand.color("yellow","purple")
#minute_hand.seth(90)
second_hand=Pen(shape='clock_hand')
second_hand.shapesize(1,1,1)
#second_hand.seth(90)
second_hand.color("green","red")
center=Pen(shape='dot')
center.shapesize(2,2,2)
center.color("orange","black")

def clockbg():
       dayofweek =["Lunes","Martes","Miercoles","Jueves","Vienes","Sabado","Domingo"]
       monthofyear =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
       t=datetime.today()
       weekday_today= dayofweek[t.weekday()]
       month_today=monthofyear[t.month]
       day_today=str(t.day)
       year_today=str(t.year)
       sety(50)
       write(weekday_today, align='center')
       sety(-50)
       write(month_today + ' '+ day_today + ',' + year_today,align='center')
       goto(0,0)

      
def mark(blank_length, mark_length):
       pu()
       fd(blank_length)
       pd()
       fd(mark_length)
       pu()
       rt(180)
       fd(mark_length+blank_length)

def clockface():
	for i in range(30):
             if i%5==0: mark(100,100/10)   	  
             else: mark(100,100/20)
             if i%5==0: mark(100,100/10)   	  
             else: mark(100,100/20)
             rt(6)

def face_rotate():
        rt(6)
        ontimer(face_rotate,1000)

def clocktick():
       t=datetime.today()
       second_hand.seth(t.second/60*360)
       minute_hand.seth(t.minute/60*360+t.second/3600*360)
       hour_hand.seth(t.hour/12*360+t.minute/12/60*360)
       # rt(6) Turn on face rotation
       ontimer(clocktick,1000)
       update()

def faceshape():
      begin_poly()
      clockface()
      end_poly()
      face_shape=get_poly()
      register_shape("face",face_shape)
      shape('face')

#faceshape()
clockface()
clockbg()
clocktick()
#face_rotate()
saveall('clock.svg',Screen()._canvas)
exitonclick()
#done()





