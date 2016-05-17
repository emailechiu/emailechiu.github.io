from turtle import *
from canvasvg import *
radians()
from math import *
shape('triangle')
s=20
phi=6.89637
f=0.83282
c=1
ratio=0.885  #0.885 for initial f in Seven Ways to Use Python slide
calc_f=sqrt(pow(ratio,2) + pow(1-ratio,2)- 2*ratio*(1-ratio)*cos(pi/3))
calc_phi=asin(sin(pi/3)/calc_f*(1-ratio))
print("phi",radians(phi),"calc_phi",calc_phi,"f",f,"calc_f",calc_f)
calc_phi
for i in range(20):
   shapesize(s)
   fillcolor(c,0.5,1-c)
   stamp()
   s *=calc_f
   c *=calc_f
   rt(calc_phi)

saveall("triangle_spiral.svg",Screen()._canvas)
