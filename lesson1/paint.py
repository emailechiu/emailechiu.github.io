from turtle import *
class MyTurtle(Turtle):
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
      def move(self,x,y):
          self.fd(50)
          self.rt(60)


MrRed = MyTurtle()
MrRed.pencolor('red')
MrRed.pensize(10)
MrRed.goto(-100,0)

MrGreen=MyTurtle()
MrGreen.pencolor('green')
MrGreen.pensize(5)
MrGreen.goto(0,100)

MrBlue=MyTurtle()
MrBlue.pencolor('blue')
MrBlue.pensize(3)
MrBlue.goto(100,0)

def f():
    fd(50)
    rt(60)


listen()
onkey(f,'a')
#onscreenclick(addmore)
MrRed.onclick(MrRed.glow)
MrRed.onrelease(MrRed.unglow)
MrGreen.onclick(MrGreen.move)
MrGreen.onrelease(MrGreen.addmore)
#MrBlue.ondrag(MrBlue.goto)
ondrag(goto)
done()

