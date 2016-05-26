from turtle import * 
from math import *
from time import sleep
tracer(0)
angle=0
size=2
side=20*size
factor=sqrt(3)/3
radius=side*factor
p=2*radius
T={}
mode('logo')
def clone_turtles(t,oddoreven,layers=1):
    for i in range(1,layers):
       for j in range(-i,i+1):
          parity_local=(i+j)%2
          parity_global=(i+j+oddoreven)%2 
          tangential=side/2*j
          radial=(1.5*i-parity_local/2)*radius
          n=t.clone()
          n.fd(-radial)
          n.rt(90)
          n.fd(tangential) 
          n.lt(90)
          p=n.pos()
          a=degrees(asin(tangential/abs(p)))
          n.lt(a)
          #print(i," ",j," ",tangential," ",radial," ",abs(p)," ",a," ",n.heading()," ",n.pos())
          n.tilt(180*parity_local-a)
          n.color('black',(parity_global,parity_global,(1-parity_global)/2))
          T[n]=(abs(p),parity_global,n.heading())

for i in range(6):
   t=Turtle()
   t.pu()
   t.speed(0)
   t.shapesize(size)
   t.shape('triangle')
   t.color('black',(i%2,i%2,(1-i%2)/2))
   t.lt(angle)
   t.fd(radius)
   t.rt(180)
   T[t]=(abs(t.pos()),i%2,180)
   clone_turtles(t,i%2,3)
   angle+=60

stepangle=-1
p=2*cos(radians(60))
p_angle=60
for tiltangle in range(60,-361+60,stepangle):
   tracer(0)
   c=2*cos(radians(tiltangle))
   c_angle=tiltangle
   for t in T:
      #print(t.heading(), " ", T[t][2])
      t.tilt((T[t][1]%2*2-1)*(p_angle-c_angle))     
      t.fd(T[t][0]*(p-c))
   p=c
   p_angle=c_angle
   update()
exitonclick()



