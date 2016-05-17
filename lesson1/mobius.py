from turtle import *
from math import *
from canvasvg import *
s=Shape("compound")
half_circle_steps=10
color('blue','blue')
begin_poly()
begin_fill()
radius=10
step=2*sin(radians(90/half_circle_steps))*radius
bk(radius)
seth(-90+90/half_circle_steps)
speed(0)
tracer(0,0)
for i in range(half_circle_steps):
   fd(step)
   rt(180/half_circle_steps)  
end_fill()
end_poly()
poly1=get_poly()

color('red','red')
begin_poly()
begin_fill()
for i in range(half_circle_steps):
   fd(step)
   rt(180/half_circle_steps)   
end_fill()
end_poly()
poly2=get_poly()

s.addcomponent(poly1,"black","red")
s.addcomponent(poly2,"black","blue")
register_shape("redblue",s)

if 1:
    clearscreen()
    shape('redblue')
    pencolor("green") #No effect on compount shapes
    pensize(4)
    radius=100
    steps=60
    step=2*pi*radius/steps
    shapesize(5,1,2)

if 1:
    #factorx=5
    #factory=1
    tilt_rotate_factor=0
    rotate_degree=360/steps
    tilt_degree=rotate_degree*tilt_rotate_factor
    tilt_radian=radians(tilt_degree)
    for i in range(steps):
        #fillcolor(i*tilt_rotate_factor%steps/steps,0,1-i*tilt_rotate_factor%steps/steps)
        stamp()
        fd(step)
        lt(rotate_degree)
        tilt(tilt_degree)
        #shapetransform(factorx*cos(i*tilt_radian),factory*sin(i*tilt_radian),-factorx*sin(i*tilt_radian),factory*cos(i*tilt_radian))

    update()
    saveall("mobius.svg",Screen()._canvas)
    exitonclick()
