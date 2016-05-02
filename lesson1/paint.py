from turtle import *
 
class MyTurtle(Turtle):
      def form(self,x,y):
          pencolor(self.pencolor())         
          pensize(self.pensize())
          print(pencolor,pensize)
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

def mypd(x,y):
      pu()
      goto(x,y)
      pd()

def mypu(x,y):
      pu()


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
MrRed.onclick(MrRed.form)
MrRed.onrelease(MrRed.form)
MrGreen.onclick(MrGreen.form)
MrGreen.onrelease(MrGreen.form)
MrBlue.onclick(MrBlue.form)
MrBlue.ondrag(MrBlue.goto)
onscreenclick(mypd)
onrelease(mypu)
ondrag(goto)
done()

