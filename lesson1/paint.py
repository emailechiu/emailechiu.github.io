from turtle import *
from canvasvg import *
 
class MyTurtle(Turtle):
      def __init__(self,col,size,x,y,shape):
          Turtle.__init__(self)
          self.color(col)
          self.pensize(size*10)
          self.shapesize(size)
          self.pu()
          self.goto(x,y)
          self.shape(shape)
          self.onclick(self.form)
      def form(self,x,y):
          print("init to ",self.color(),self.shapesize(),self.pencolor(), self.pensize())
          color(self.pencolor(),self.fillcolor()) # this sets pencolor as well as fillcolor
          shapesize(self.pensize()/10)
          pensize(self.pensize())
          shape(self.shape())
          print("onclick set to ", color(), shapesize(),pencolor(),pensize())
      def glow(self,x,y):
          self.fillcolor("yellow")
          self.shapesize(3)
      def unglow(self,x,y):
          self.fillcolor("")
          self.shapesize(1)
      def addmore(self,x,y):
          newT=self.clone()
          newT.pu()
          newT.setpos(x,y)
          newT.pd()
          newT.shape('turtle')
          newT.shapesize(1)

def jump(x,y):
      pu()
      goto(x,y)
      pd()
      print("jump to",x,y,pencolor(),pensize())

def f():
    fd(50)
    rt(60)

def s():
    saveall('paint.svg',Screen()._canvas)

shape('circle')
listen()
onkey(f,'a')
onkey(s,'s')
onscreenclick(jump)
ondrag(goto)

MrRed = MyTurtle('red',2,-400,200,'circle')
MrGreen = MyTurtle('green',1.5,-400,100,'triangle')
MrBlue = MyTurtle('blue',1,-400,40,'square')
MrPink = MyTurtle('pink',0.5,-400,10,'turtle')

done()

