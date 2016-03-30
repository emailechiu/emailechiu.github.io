#!/usr/bin/python3

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html

import turtle,math,random
from canvasvg import *
print("Content-type:text/html\n")

def drawLogo():
 colors = ['navy','red','purple','blue','green','magenta','yellow']
 radius = 100
 while (radius!=0):
  radius=int(input('Radius: ')) 
  circles=int(input('# of small circles: ')) 
  angle=360/circles
  turtle.clearscreen()
  turtle.bgcolor('black')
  turtle.tracer(0,0)
  wn = turtle.Screen()
  #t=turtle.Pen()
  for x in range(circles):
    turtle.color(random.choice(colors))
    drawPolygon(turtle,30,radius/2) 
    turtle.left(angle)
  turtle.update()
  canvasvg.saveall('logo.svg', wn._canvas)
  #wn._canvas.postscript(file='logo.ps')
  turtle.exitonclick()

def drawPolygon(t,sides,radius):
   step = 2*radius*math.sin(math.pi/sides)
   angle= 360/sides
   for x in range(sides):
     t.fd(step)
     t.left(angle) 

drawLogo()
