#!/usr/bin/python3
from turtle import *
from math import *
AU=3e8*60*8.31
TU=365*24*3600
TU=1
Oe = 2*pi/TU
Oem = 2*pi/TU*13
Ve = Oe * Re
V
GMs=pow(AU,3)*pow(Oe,2)
GMe=pow(AU/388,3)*pow(Oem,2)
Rm=1.28*3e8
Re=AU
print(GMs/GMe)
setworldcoordinates(-AU,-AU,AU,AU)
s=Turtle(shape='circle');s.color('yellow')
e=Turtle(shape='circle');e.color('blue')
m=Turtle(shape='circle');m.color('purple')
e.goto(0,-Re)
#e.circle(Re)
m.goto(0,-Re-Rm)
def move():
    rms = s.pos()-m.pos()
    rme = e.pos()-m.pos()
    res = s.pos()-e.pos()
    Ae = GMs/pow(abs(res),3)*res 
    Am = GMs/pow(abs(rms),3)*rms+GMe/pow(abs(rme),3)*rme
    Ve=Ve + 
    Vem=Vem+G*Me/D(e,m)


