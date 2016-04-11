#!/usr/bin/python3
from turtle import *
from math import *
AU=3e8*60*8.31
TU=365*24*3600
TU=1
GMs=pow(AU,3)*pow((2*pi/TU),2)
GMe=pow(AU/363,3)*pow(2*pi/TU*12,2)
print(GMs)
setworldcoordinates(-AU,-AU,AU,AU)
s=Turtle(shape='circle');s.color('yellow')
e=Turtle(shape='circle');e.color('blue')
m=Turtle(shape='circle');m.color('purple')
e.goto(0,-0.99*AU)
e.circle(0.99*AU)
Oe = 2*pi/TU
Oem = 2*pi/TU*12

def move():
    Ve=Ve + G*Ms/D(e,s)
    Vem=Vem+G*Me/D(e,m)


