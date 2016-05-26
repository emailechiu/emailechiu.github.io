#!/usr/bin/python3
from turtle import *
from math import *
from time import *

bgcolor("black")

def wiki_serial(n, size):
  fd(100)
  pencolor("red")
  pensize(3)
  tracer(0,0)
  for i in range(n):
     rt(360./n)
     circle(size)
  update()

def wiki_serialEvent(x,y):
   wiki_serial(36,100)

def wiki_parallel(n,size,speed,speedup,slowdown):
    def create_turtles(n):
      for i in range(n):
        t=Turtle()
        t.pencolor(i/n,0,1-i/n)
        t.speed(speed)
        #t.pencolor("white")
        t.seth(360/n*i)
    clearscreen()
    tracer(speedup,slowdown)
    create_turtles(n)
    s=turtles()
    steps = 20
    step = size*2*pi/steps
    for j in range(steps):
      for i in range(n):
         s[i].fd(step)
         s[i].rt(360./steps)
    update()  #Comment to skip circles
 
       
def timedraw(speedrange,speeduprange,slowdown):
    for i in speeduprange:
      for j in speedrange:
        tp0= clock()
        tw0= time()
        wiki_parallel(36,100,j,i,slowdown)
        print("when speedup is ",j,"when speed is ",i,"Process time is ",clock()-tp0," Wall time is ",time()-tw0 )

#wiki_parallel(36,100,0) # speed 1 is slowest tracer speedup=1, 270s at slowest=1, 30s at fastest=0
timedraw([1],[1],0) # tracer 2 is slowest tracer speedup=(0, 0.15s), (1,11s),(2,32s),(4,16s),(64,1s), slwodown has no effect
onscreenclick(wiki_serialEvent)
done()

#Macrocontrol speedup=0  for very fast, speedup=2 for verys low.  speedup=1 and fine tune speed with 8x between 0 and 1
#generally (0,x) fastest, (1,1) slowest, but make sure to check (2,1) which is sometimes slower.
#when speed is  0 speedup is  1 Process time is  2.6399999999999997  Wall time is  11.750622749328613
#when speed is  1 speedup is  1 Process time is  25.490000000000002  Wall time is  106.69523286819458
#when speed is  0 speedup is  2 Process time is  24.43  Wall time is  34.93558883666992
#when speed is  1 speedup is  2 Process time is  24.499999999999996  Wall time is  35.08503341674805
#Surprise! Notice speedup 2 is actually slower than speedup 1 for certain speeds


