#!/usr/bin/python3
from turtle import *
from math import *
from time import *

bgcolor("black")

def serial(n, size):
  fd(100)
  pencolor("red")
  pensize(3)
  tracer(0,0)
  for i in range(n):
     rt(360./n)
     circle(size)
  update()

def parallel(n,size,speed):
    def create_turtles(n):
      for i in range(n):
        t=Turtle()
        t.pencolor(i/n,0,1-i/n)
        t.speed(speed)
        #t.pencolor("white")
        t.seth(360/n*i)
    clearscreen()
    create_turtles(n)
    s=turtles()
    steps = 20
    step = size*2*pi/steps
    for j in range(steps):
      for i in range(n):
         s[i].fd(step)
         s[i].rt(360./steps)
       
def timedraw():
    for i in range(11):
      tp0= clock()
      tw0= time()
      parallel(36,100,i)
      print("when speed is ",i,"Process time is ",clock()-tp0," Wall time is ",time()-tw0 )

timedraw()   
onclick(serial(36,100))
done()
