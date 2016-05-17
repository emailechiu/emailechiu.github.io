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

class kolam():
  def __init__(self):
    self.replacementRules={"B":"RFBFBFBFR","R":"RFBFR"}
    self.axiom="BFBFBFBF" 
    self.depth= 2
  def display(self):
    factor=pow(2,3-self.depth)
    greenside=3*factor
    redside=greenside
    blackside=greenside
    def F():
        pencolor('green')
        fd(greenside) 
        rt(45)
    def B():
        pencolor('black')
        lt(90)
        fd(blackside)
        rt(90)
        fd(blackside)
        rt(90)
        fd(blackside)
        lt(45)
    def R():
        lt(90)
        pencolor('red')
        fd(redside)
        lt(45)
    rules={"B":B,"F":F,"R":R}
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
kolam().display()
exitonclick() 
    
