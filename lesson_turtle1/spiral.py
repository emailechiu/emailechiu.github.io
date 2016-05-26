#!/usr/bin/python3

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html

import random,canvasvg
from turtle import *
def drawSpiral(angle_start=90,angle_ratio=0,step_start=50,step_ratio=0.1):
 colors = ['navy','red','purple','blue','green','magenta','yellow']
 while (angle_start!=0):
  angle_start=int(input("Starting Angle? Concave>90: ")) 
  step=step_start
  angle=angle_start
  step_delta= step_start*step_ratio
  angle_delta=angle_start*angle_ratio
  clearscreen()
  bgcolor("black")
  tracer(0,0)
  t=Pen()
  for x in range(20):
    t.color(random.choice(colors))
    t.forward(step) 
    t.left(angle)
    step+=step_delta
    angle+=angle_delta
  update()
  canvasvg.saveall("spiral.svg",Screen()._canvas)
  exitonclick()

    

def drawcockscrew():
   for i in range(72):
      fd(20)
      rt(10)
      setpos(pos()+Vec2D(5,0))

#drawcockscrew()
onclick(drawSpiral())
