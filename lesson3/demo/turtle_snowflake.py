#!/usr/bin/python

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html

import turtle,math,random
def drawRhombus(t,step,acute_angle):
  sides=4
  #start_angle= orientation_angle + acute_angle/2
  obstuse_angle= 180 -acute_angle
  #t.seth(start_angle)
  for x in [1,2]:
    t.forward(step) 
    t.left(acute_angle)
    t.forward(step) 
    t.left(obstuse_angle)
  
turtle.tracer(0,0) 
turtle.speed(0) 
turtle.clearscreen()
canvas=500
#sides = input('# of rhombus?')
#side = input('length?')
sides = 10
center_angle=360/sides 
acute_angle=center_angle*3/2
colors = ['navy','red','purple','blue','green','magenta','yellow']
side=canvas/5
turtle.setup(canvas,canvas,0,0)
t=turtle.Pen()
t.screen.bgcolor("black")
for x in range(sides): 
 t.color(random.choice(colors)) 
 drawRhombus(t,side,acute_angle)
 t.left(center_angle)
 #t.reset()
turtle.update()
turtle.mainloop()
turtle.bye()


