#!/usr/bin/python3
from turtle import *
from math import *
from canvasvg import *
mode("standard")
tracer(0)
mycolor=[0,0,0]
ss=200
ls=2*ss
h=ss*10
b=ss/2
m=ss/4
s=ss/6
g=ss/60
westminster=[(1,1,1,m,90),   #LFO
             (-1,1,-1,b,30), #RFI
             (1,1,1,s,90),   #LFO
             (1,1,1,h,2),   #I
             (1,1,-1,g,90)
             
    ]

def arc(start,end,angle,direction=1,steps=20,col='red'):
    pencolor(col)
    jumpto(start)
    segment=end-start
    ang_sin=degrees(asin(segment[1]/abs(segment)))
    ang_cos=degrees(acos(segment[0]/abs(segment)))
    ang_segment=copysign(ang_cos,ang_sin)
    seth(ang_segment-direction*angle/2)
    radius= abs(segment)/2/sin(radians(angle/2))
    circle(direction*radius,angle,steps) #short arc

def center(start,end,angle,direction=1,col='red'):
    arc(start,end,360-2*angle,direction,2,col)

def jumpto(d):
    pu()
    goto(d)
    pd()

def tracing(foot,direction,edge,radius=g,angle=90):
    mycolor[1]=1-mycolor[1]
    pencolor(mycolor)
    circle(foot*edge*radius,direction*angle)

def setupcanvas():
    setup(2*ss,2*ls)
    bgcolor('grey')
    color('white')
    fd(ss)
    bk(ss*2)
    fd(ss)
    lt(90)
    fd(ls)
    bk(ls*2)
    fd(ls)
    pu()
    goto(-ss/3,ls/8*7)
    lt(45)
    pd()
    color('black')
    
def geom():   
    for direction in [-1,1]:
        start=Vec2D(50,50)
        end=Vec2D(-100,-50)
        angle=90
        col=(direction/2+1/2,1/2-direction/2,0)
        arc(start,end,angle,direction,20,col)   # short arc
        arc(start,end,360-angle,direction,20,col)   # short arc
        arc(end,start,angle,direction,20,col) #long arc
        arc(start,end,angle,direction,2,col)   # sharp segment
        arc(end,start,360-angle,direction,2,col) #obtuse segment
        center(start,end,angle,direction,col)

def render(pattern):
    setupcanvas()
    previous=pattern[0]
    for i in pattern:
        print(heading())
        current=i
        fc=current[0]-previous[0]
        dc=current[1]-previous[1]
        ec=current[2]-previous[2]
        if fc!=0: pu();rt(90);fd(-fc*g);lt(90);pd()  #change foot
        else:
            if ec!=0: tracing(*previous);tracing(*current[0:3])
        if dc!=0: rt(180) #change direction
        tracing(*current)
        previous=current[0:3]

render(westminster)
update()
#saveall('pattern.svg',Screen()._canvas)
exitonclick() 
