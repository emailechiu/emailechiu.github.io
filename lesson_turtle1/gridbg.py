from turtle import *
from math import *
from canvasvg import *
def jump(x,y):
    pu()
    goto(x,y)
    pd()

def line(x1,y1,x2,y2):
    pu()
    goto(x1,y1)
    pd()
    goto(x2,y2)
    pu()

def horizontal_line(y,width):
    line(-width,y,width,y)

def vertical_line(x,height):
    line(x,-height,x,height)

def grid(width,height):
    for x in range(-width,width+1,10):
        vertical_line(x,height)
    for y in range(-height,height+1,10):
        horizontal_line(y,width)

def xaxis(width):
    jump(-width,0)
    shapesize(0.2,1)
    for x in range(-width,width+1,100):
        goto(x,0)
        write(x,align='center')
        stamp()

def yaxis(height):
    jump(0,-height)
    shapesize(1,0.2)
    for y in range(-height,height+1,100):
        goto(0,y)
        write(y,align='center')
        stamp()

def polar(radius):
    inner_radius=radius-100
    angle=30
    jump(radius,0)
    seth(0)
    shape('arrow')
    color(0.5,0.5,1)
    tilt(90)
    t=clone()
    t.color(1,0.5,0.5)
    t.pu()
    t.goto(inner_radius,0)
    t.pd()
    for i in range(0,360,30):
        stamp()
        write(abs(180-towards(0,0)),align='center')
        circle(radius,angle)
        t.stamp()
        t.write(i,align='center')
        t.circle(inner_radius,angle)

def cartesian():
    mode('logo')
    width=400
    height=400
    print(screensize())
    setup(width=2*width+50,height=2*height+50)
    screensize(100,100) #meaningful only when greater than setup size, scrolls
    print(screensize())
    #setup(0.99,0.75) #unrelated to screensize, but related to actual screen
    color('grey')
    tracer(0)
    grid(width,height)
    pensize(2)
    shape('square')
    #color('black')
    yaxis(height)
    xaxis(width)
    polar(min(width,height))
    update()
    saveall('grid.svg',Screen()._canvas)
    tracer(1)

cartesian()
       
