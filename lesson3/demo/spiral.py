#!/usr/bin/python3

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html

import turtle,math,random,canvasvg
def drawSpiral(angle_start=90,angle_ratio=0,step_start=100,step_ratio=0.01):
 colors = ['navy','red','purple','blue','green','magenta','yellow']
 while (angle_start!=0):
  angle_start=int(input("Starting Angle? Concave>90: ")) 
  step=step_start
  angle=angle_start
  step_delta= step_start*step_ratio
  angle_delta=angle_start*angle_ratio
  turtle.clearscreen()
  turtle.bgcolor("black")
  turtle.tracer(0,0)
  t=turtle.Pen()
  for x in range(100):
    t.color(random.choice(colors))
    t.forward(step) 
    t.left(angle)
    step+=step_delta
    angle+=angle_delta
  turtle.update()
  canvasvg.saveall("spiral.svg",turtle.Screen()._canvas)
  turtle.exitonclick()

drawSpiral()
