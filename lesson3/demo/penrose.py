from turtle import *
from math import *
from time import sleep
d=50
r=(sqrt(5)-1)/2
s = r*d
def dart():
    begin_fill()
    begin_poly()
    fillcolor('yellow')
    lt(36)
    fd(d)
    rt(144)
    fd(s)
    lt(36)
    fd(s)
    rt(144)
    fd(d)
    rt(144) 
    end_poly()
    end_fill()
    return get_poly()

def kite():
    begin_fill()
    begin_poly()
    fillcolor('blue')
    lt(36)
    fd(d)
    rt(108)
    fd(s)
    rt(36)
    fd(s)
    rt(108)
    fd(d)
    rt(144)
    end_poly()
    end_fill()
    return get_poly()

def tiledart(depth):
    if depth==0:
          shape('dart')
          shapesize(1)
          color('black','yellow')
          stamp()
    else:
          tiledart(depth-1)
          lt(36);fd(d*r**(-depth));rt(144);tilekite(depth-1);lt(144);bk(d*r**(-depth))
          rt(36);fd(d*r**(-depth));lt(144);tilekite(depth-1);rt(144);bk(d*r**(-depth))

def tilekite(depth):
    #print(depth)
    if depth==0: 
          shape('kite')
          shapesize(1)
          color('black','blue')
          stamp()
    else: 
          tiledart(depth-1)
          fd(d*r**(-depth))
          rt(180)
          lt(36);tilekite(depth-1);rt(36)
          rt(36);tilekite(depth-1);lt(36)
          lt(180)
          bk(d*r**(-depth))

def tile():
   ht()
   for j in range(3): 
    reset()
    ht()
    for i in range(5):
      tilekite(j)
      lt(72)
    update()
    sleep(1)
      
 
tracer(0)
register_shape('dart',dart())
register_shape('kite',kite())
tile()
exitonclick()




