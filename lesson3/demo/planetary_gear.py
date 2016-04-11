from turtle import *
from math import *
from mod_polygon import *
tracer(0,0)
sides=120
t=Pen()
s=Shape("compound")
t.begin_poly()
drawPolygon(t,20,0,10,1) #start from bottom, counter clock to top
t.end_poly()
poly1=t.get_poly()
t.begin_poly()
drawPolygon(t,20,0,-10,1) #start from bottom, clockwise to top
t.end_poly()
poly2=t.get_poly()
s.addcomponent(poly1,"white","red")
s.addcomponent(poly2,"white","blue")
register_shape("redblue",s)

Rr=200
Rs=100
Rcr=(Rr+Rs)/2
Rcs=(Rr-Rs)/2
r=Pen()
r.shape('redblue')
r.shapesize(Rr,Rr,Rr/50)

s=Pen()
s.shape('redblue')
s.shapesize(Rs,Rs,Rs/20)

c=Pen()
c.shape('redblue')
c.shapesize(Rcs,Rcs,Rcs/20)
c.pu()
c.goto(Rcr,0)
c.seth(-180/sides)
c.pd()
update()

Vs=2*pi*Rs/sides
Vr=2*pi*0/sides
Os=degrees(Vs/Rs)
Or=degrees(Vr/Rr)
Vcr=(Vs+Vr)/2
Vcs=(Vs-Vr)/2
Ocr=degrees(Vcr/Rcr)
Ocs=degrees(Vcs/Rcs)

def move_gears():
   s.lt(Os)
   r.lt(Or)
   c.fd(Vcr)
   c.lt(Ocr)
   c.tilt(Ocs+Ocr)
   c.stamp()
   #print(Ocr," ",Vcr)
   update()
   ontimer(move_gears,100)


move_gears()
exitonclick()

    
    
