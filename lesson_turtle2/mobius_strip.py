from turtle import *
from math import *
from mod_polygon import *
tracer(0,0)
t=Pen()
s=Shape("compound")
t.begin_poly()
drawPolygon(t,20,0,10,10) #start from bottom, counter clock to top
t.end_poly()
poly1=t.get_poly()
t.begin_poly()
drawPolygon(t,20,0,-10,10) #start from bottom, clockwise to top
t.end_poly()
poly2=t.get_poly()

if 0:
   s=Shape("compound")
   half_circle_steps=10
   color('blue','blue')
   begin_poly()
   begin_fill()
   seth(-90+90/half_circle_steps)
   speed(0)
   for i in range(half_circle_steps):
      fd(5)
      rt(180/half_circle_steps)  
   end_fill()
   end_poly()
   poly1=get_poly()

   color('red','red')
   begin_poly()
   begin_fill()
   for i in range(half_circle_steps):
      fd(5)
      rt(180/half_circle_steps)   
   end_fill()
   end_poly()
   poly2=get_poly()

s.addcomponent(poly1,"black","red")
s.addcomponent(poly2,"black","blue")
register_shape("redblue",s)

t.shape('redblue')
t.shapesize(5,1,3)
tracer(0,0)
stampPolygon(t,36,36,100,-200,-200,1,1.5)
stampPolygon(t,36,36,100,-400,0,1,1)
stampPolygon(t,36,36,100,-200,200,1,0.5)
stampPolygon(t,36,36,100,200,-200,-1,1.5)
stampPolygon(t,36,36,100,400,0,-1,1)
stampPolygon(t,36,36,100,200,200,-1,0.5)
update()
   
if 0:
    clearscreen()
    shape('redblue')
    pencolor("green") #No effect on compount shapes
    pensize(4)
    radius=100
    steps=36
    step=2*pi*radius/steps
    shapesize(1,5,3)

if 0:
    #factorx=5
    #factory=1
    tilt_rotate_factor=1.5
    rotate_degree=360/steps
    tilt_degree=rotate_degree*tilt_rotate_factor
    tilt_radian=radians(tilt_degree)
    for i in range(steps*2):
        #fillcolor(i*tilt_rotate_factor%steps/steps,0,1-i*tilt_rotate_factor%steps/steps)
        fd(step)
        lt(rotate_degree)
        tilt(tilt_degree)
        #shapetransform(factorx*cos(i*tilt_radian),factory*sin(i*tilt_radian),-factorx*sin(i*tilt_radian),factory*cos(i*tilt_radian))
        stamp()

exitonclick()

    
    
