from turtle import *
from math import *
d=400
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

def tilekite(depth):
    print(depth)
    if depth>=2: 
          shape('kite')
          shapesize(r**depth)
          color('black','blue')
          stamp()
    else: 
          shape('dart')
          color('black','yellow')
          shapesize(r**(depth+1))
          stamp()
          fd(d*r**(depth))
          rt(180)
          lt(36);tilekite(depth+1);rt(36)
          rt(36);tilekite(depth+1);lt(36)
          lt(180)
          bk(d*r**(depth))

def tile():
    for i in range(1):
      tilekite(0)
      lt(72)
      
 
tracer(2)
register_shape('dart',dart())
register_shape('kite',kite())
reset()
tile()
update()
exitonclick()




