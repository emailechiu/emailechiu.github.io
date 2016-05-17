#!/usr/bin/python3
from turtle import *
class MyTurtle(Turtle):
    def jump(turtle,distance):
       turtle.pu()
       turtle.fd(distance)
       turtle.pd()

you=MyTurtle()
you.jump(100)
me =MyTurtle()
me.jump(-100)
done()

