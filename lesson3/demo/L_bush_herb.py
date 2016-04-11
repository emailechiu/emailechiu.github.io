from turtle import *
from math import *
speed(0)
tracer(1)
ht()
def jump(d):
  pu()
  fd(d)
  pd() 

def replace(seq,replacementRules,n):
  result=seq
  if n>0:
    newseq=""
    for element in seq:
        newseq = newseq + replacementRules.get(element,element)
    result=replace(newseq,replacementRules,n-1)
  return result

class bush():
  def __init__(self):
    self.replacementRules={".":".F[-.][+.]","F":"FF"}
    self.axiom="." 
    self.depth= 4
    self.start=(0,-200)
  def display(self):
    factor=pow(2,6-self.depth)
    trunk=3*factor
    leftup=factor
    rightup=factor
    leftside=factor
    leftside2=2*factor
    rightside1=factor
    rightside2=2*factor
    setpos(self.start)
    b=[]
    def F():
        pencolor('green')
        fd(trunk)
    def W():
        circle(-leftside2,90)
    def V():
        circle(rightside2,90)
    def l():
        pencolor('blue')
        #fd(leftup)
        lt(30) 
        #circle(-leftside2,90)
    def r():
        pencolor('red')
        #fd(rightup)
        rt(30)
        #circle(rightside2,135)
    def S():
        b.append(pos())
        b.append(heading())
    def L():
        pu()
        seth(b.pop())
        setpos(b.pop())
        pd()
    rules={"f":"F",".":F,"-":l,"F":F,"+":r,"[":S,"]":L,"T":F,"V":V,"W":W}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,self.depth)
    print(drawing)
    draw(drawing,rules)
    update()

class Tamil_ethno():
  def __init__(self):
    self.replacementRules={"B":"RFBFBFBFR","R":"RFBFR"}
    self.axiom="FBFBFBFB" 
    self.depth= 1
  def display(self):
    factor=pow(2,3-self.depth)
    greenside=5*factor
    redstep=greenside
    radius=greenside/2
    lt(45) 
    def F():
        pencolor('green')
        fd(greenside) 
    def R():
        pencolor('red')
        circle(redstep,90)
    def B():
        pencolor('black')
        fd(radius)
        circle(radius,270)
        fd(radius)
    rules={"B":B,"F":F,"R":R}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,self.depth)
    print(drawing)
    draw(drawing,rules)
    update()



#koch_snowflake().display()
#hilbert_triangle().display()
#tree().display()
#branches().display()
#Tamil_ethno().display()
#kolam().display()
bush().display()
exitonclick() 
    
