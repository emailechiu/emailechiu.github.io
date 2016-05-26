from turtle import *
from math import *
s=Screen()
print(s.screensize())
s.screensize(500,500)

setworldcoordinates(-600,-400,600,400)
s.screensize(400,300)
s.setup(800,600)

t=Turtle()
t.fd(200)
t.lt(90)
t.circle(200)

print(s.screensize())

