#!/usr/bin/python

# factors, groups, cyclic remainder generator
# https://blockly-games.appspot.com/turtle
import turtle,math,sys,canvasvg
def drawStar(t,x,y,sides,radius):
  concave_factor=0	
  for x in range(int(sides/4+1),int(sides/2)):
     if gcd(x,sides)==1: 
        concave_factor=x
        print("concave_factor  ",concave_factor)
        break
  if concave_factor==0: print("Cannot draw star with side " + str(sides))
  else: print("Drawing side " + str(sides) + " with 360/sides * " + str(concave_factor))
  angle = 360*concave_factor/sides
  step_app = radius * 2 * 3.14 * angle /360
  step = radius * 2 * math.sin(math.pi/180 * angle/2)
  start_angle= -90 - angle/2
  t.up()
  t.goto(x+radius*math.cos(math.pi/180*start_angle),y+radius*math.sin(math.pi/180*start_angle))
  t.down()
  for x in range(0,sides): 
     t.forward(step) 
     t.left(angle)

def gcd(small,big):
  if small==1: return 1
  else: 
     if small==0: return big
  return gcd(big%small,small)
 
turtle.clearscreen()
canvas=500
# sides = input('# of sides?')
# radius = input('radius?')
sides = [5,6,7,9,12,24]
colors = ['black','red','magenta','yellow','blue','green','purple']
dictionary = dict(zip(sides,colors[:len(sides)]))
radius=canvas/5
turtle.setup(canvas,canvas,0,0)
t=turtle.Pen()
t.seth(90)
turtle.tracer(0,0)
for side,color in dictionary.items(): 
 print(side,color)
 t.color(color) 
 drawStar (t,0,0,side,radius)

turtle.update()
canvasvg.saveall("star.svg",turtle.Screen()._canvas)
turtle.exitonclick()

