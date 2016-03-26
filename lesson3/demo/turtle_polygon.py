#!/usr/bin/python

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html

import turtle,math
def drawPolygon(t,x,y,sides,radius):
  angle = 360/sides
  step_app = radius * 2 * 3.14 * angle /360
  step = radius * 2 * math.sin(math.pi/180 * angle/2)
  start_angle= -90 - angle/2
  t.up()
  t.goto(x+radius*math.cos(math.pi/180*start_angle),y+radius*math.sin(math.pi/180*start_angle))
  t.down()
  for x in range(0,sides): 
     t.forward(step) 
     t.left(angle)
  
turtle.clearscreen()
canvas=500
# sides = input('# of sides?')
# radius = input('radius?')
sides = [3,4,5,6,8,10,36]
colors = ['navy','red','purple','blue','green','magenta','yellow']
dictionary = dict(zip(sides,colors))
print(dictionary)
radius=canvas/5
turtle.setup(canvas,canvas,0,0)
t=turtle.Pen()
for side,color in dictionary.items(): 
 t.color(color) 
 drawPolygon (t,0,0,side,radius)
 #t.reset()
turtle.bye()


