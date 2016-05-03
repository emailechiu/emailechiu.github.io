from turtle import *
from numpy import array
from canvasvg import *
setworldcoordinates(-1,-0.2,3,1.2)
mix=[0.5,0.5,0.5]
class colorTurtle(Turtle):
      def __init__(self,x):
          Turtle.__init__(self,shape='turtle')
          self.speed(0)
          self.lt(90)
          self.pensize(10)
          self.shapesize(3,3,5)
          self._color=[0,0,0]
          self._color[x]=0.5
          self.color(self._color)
          self.pu()
          self.goto(x,0)
          self.pd()
          self.goto(x,1)
          self.pu()
          self.goto(x,0.5)
          self.ondrag(self.slide)
      def slide(self,x,y):
          #print("entering slide", x, y)
          self.sety(max(0,min(y,1)))
          x=self.xcor()
##          col=array(self.pencolor())
##          col_n=array([1,1,1])-col         
##          bg=array(bgcolor())/255
##          c=map(lambda a,b:a*(col_n)+b*col,bg,y)
          mix[self.xcor()]=self.ycor()
          bgcolor(mix)
          #print(col,col_n,y,bg,c)
          
      
red,green,blue=colorTurtle(0),colorTurtle(1),colorTurtle(2)
bgcolor(mix)
saveall('colorslider.svg',Screen()._canvas)
done()
