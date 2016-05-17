#!/usr/bin/python3
from turtle import *
from math import *
tracer(10)
speed(0)
G = 6.67e-11
AU=3e8*60*8.31
TU=365*24*3600
#TU=1
Oe = 2*pi/TU
Oem = 2*pi/TU*13
Rem=1.28*3e8
Re=AU
Ve = Oe * Re
Vem = Rem * Oem
GMs=pow(AU,3)*pow(Oe,2)
GMe=pow(AU/388,3)*pow(Oem,2) #1/333333 Ms
GMm = GMe/81.632
DT = 7200
fx = 1.2e10
print(GMs," ",GMe," ",GMm," ",Ve," ",Vem)
class Star(Turtle):
    def __init__(self,p,v,GM,typ):
        Turtle.__init__(self)
        self.v=v
        self.typ=typ
        self.gm=GM
        self.setpos(p)
    def step(self,a,DT):
        #print(self.typ," ",a," ",self.v)
        self.v=self.v+a*DT
        self.setpos(self.pos()+self.v*DT)

class GravSys():
    def __init__(self):
        self.planets=[]
        self.dt=DT
    def init(self):
       for i in self.planets:
        i.v=i.v + 0.5*DT*self.acc(i)
    def add(self,planet):
        self.planets.append(planet)
    def acc(self,planet):
        a =Vec2D(0,0)
        for i in self.planets:
            d = i.pos() - planet.pos()
            if (i!=planet): a=a+i.gm/pow(abs(d),3)*d
        return a
    def start(self): 
      for j in range (10000):
        for i in self.planets:
            if (i.typ!='sun'): i.step(self.acc(i),self.dt)
            if (i.typ=='earth'): 
               x,y=i.pos()-0.92*3/4*fx/abs(i.v)*i.v
               setworldcoordinates(x-fx,y-3/4*fx,x+fx,y+3/4*fx)
               #setworldcoordinates(x-Rem,y-Rem,x+Rem,y+Rem)
        

def main():
    setworldcoordinates(-2*AU,-2*2*AU,2*AU,2*AU)
    s = Star(Vec2D(0,0),Vec2D(0,0),GMs,'sun')
    s.shapesize(1.8)
    s.color('yellow')
    s.shape('circle')
    e = Star(Vec2D(Re,0),Vec2D(0,Ve),GMe,'earth')
    e.shapesize(0.8)
    e.color('blue')
    e.shape('circle')
    m = Star(Vec2D(Re+Rem,0),Vec2D(0,Ve+Vem),GMm,'moon')
    m.shapesize(0.5)
    m.color('purple')
    m.shape('circle')
    gs=GravSys()
    gs.add(s)
    gs.add(e)
    gs.add(m)
    #gs.init()
    gs.start()
    update()



main()
