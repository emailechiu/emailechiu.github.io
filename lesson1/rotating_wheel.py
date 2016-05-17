from turtle import *
from math import *
mode("logo")
#register_shape("cat.gif")
#shape("cat.gif")
shape("circle")


def myshape(code):
    home()
    begin_poly()
    exec(code)
    end_poly()
    return get_poly()

def line(x,y):
    pu()
    goto(x)
    pd()
    color("green")
    pensize(10)
    goto(y)
    pu()
    home()

s=Shape("compound")
s.addcomponent(myshape("fd(10);lt(90);circle(10,180)"),"red","blue")
s.addcomponent(myshape("fd(10);lt(90);circle(10,-180)"),"blue","red")
register_shape("moon",s)
clearscreen()
shape("moon")
shapesize(10)

speed(10)
line((-200,200),(600,200))
line((-200,-100),(600,-100))

for i in range(5):
   goto(i*100,i%2*100)
speed(0)
n=120
handle=Turtle(shape='square')
handle.shapesize(10,1)
handle.pu()
puller=Turtle(shape='turtle')
puller.shapesize(10,10)
puller.pu()
puller.rt(90)
puller.color('purple','purple')
for i in range(n):
   rt(360/n)
   setx(-200+i*radians(360/n)*10*10)
   handle.setx(-100+i*radians(360/n)*10*10)
   puller.setx(i*radians(360/n)*10*10)
   
#done()

