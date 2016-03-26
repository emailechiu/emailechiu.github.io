#!/usr/bin/python

# factors, groups, cyclic remainder generator
# https://blockly-games.appspot.com/turtle
import turtle,math,sys
def drawStar(t,x,y,sides,radius):
  angle = 360*11/sides
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
sides = [5,6,24]
colors = ['navy','red','magenta']
dictionary = dict(zip(sides,colors))
radius=canvas/5
turtle.setup(canvas,canvas,0,0)
t=turtle.Pen()
for side,color in dictionary.iteritems(): 
 t.color(color) 
 print(side,color)
 drawStar (t,0,0,side,radius)
 #t.reset()
#turtle.bye()


