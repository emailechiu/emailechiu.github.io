#!/usr/bin/python3
from turtle import *
from numpy import array
from canvasvg import *
setworldcoordinates(-1,-0.2,3,1.2)
mix1=[0.5,0.5,0.5]
class colorTurtle(Turtle):
      def __init__(self,x):
          Turtle.__init__(self,shape='turtle')
          self.speed(0)
          self.lt(90)
          self.pensize(10)
          self.shapesize(3,3,5)
          self.colors=[0,0,0]
          self.colors[x]=1
          self.color(self.colors)
          self.pu()
          self.goto(x,0)
          self.pd()
          self.goto(x,1)
          self.pu()
          self.goto(x,0.5)
          #bgcolor(tuple(array([0,1,0]))) #if in slide() this stops next execution but no error message!
          #print(self.color()) #Type error onlyif self._color is used
          self.ondrag(self.slide)
      def slide(self,x,y):
          self.sety(max(0,min(y,1)))
          col=array(self.pencolor())
          col_n=array([1,1,1])-col
          bg=array(bgcolor())        
          #mix=map(lambda a,b:a*(col_n)+b*col,bg,self.ycor())
          #print(bg,col_n)
          mix=(bg*col_n+self.ycor()*col).tolist()
##        mix[self.xcor()]=self.ycor()          
          bgcolor(mix)
          #print("background color is",bgcolor())
          
##          
          

red,green,blue=colorTurtle(0),colorTurtle(1),colorTurtle(2)
bgcolor(mix1)
saveall('colorslider.svg',Screen()._canvas)
done()
