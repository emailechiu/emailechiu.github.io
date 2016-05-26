#!/usr/bin/python3

# trigonometry, list, dictionary, function, input, iteration
# http://www.k6-geometric-shapes.com/polygons.html
# http://www.printable-math-worksheets.com/celtic-design.html
# http://mekanizmalar.com/cardan_gear.html
from turtle import *
import math,random
from canvasvg import *
bg='white'
color1='blue'
color2='green'
color3='yellow'
pencol='red'
tracer(0,0)

def drawLogo():
 colors = ['navy','red','purple','blue','green','magenta','yellow']
 radius = 100
 while (radius!=0):
  radius=int(input('Radius: ')) 
  circles=int(input('# of small circles: ')) 
  angle=360/circles
  reset()
  color(pencol,color1)
  pu()
  fd(radius)
  lt(90)
  pd()
  begin_fill()
  circle(radius)
  color(random.choice(colors),random.choice(colors))
  end_fill()
  pu()
  home()
  pd()
  begin_fill()
  for x in range(circles):
    drawPolygon(30,radius/2) 
    left(angle)
  color(random.choice(colors),random.choice(colors))
  end_fill() 
  update()
  canvasvg.saveall('wikipedia.svg', Screen()._canvas)
  #wn._canvas.postscript(file='logo.ps')

def drawPolygon(sides,radius):
   step = 2*radius*math.sin(math.pi/sides)
   angle= 360/sides
   for x in range(sides):
     fd(step)
     left(angle) 

bgcolor(bg)
drawLogo()
done()
