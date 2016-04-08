from turtle import *
from math import *
speed(0)
ht()

def replace(seq,replacementRules,n):
  result=seq
  if n>=0:
    newseq=""
    for element in seq:
        newseq = newseq + replacementRules.get(element,element)
    result=replace(newseq,replacementRules,n-1)
  return result

class Tamil_ethno():
  def __init__(self):
    #self.replacementRules={".":"B","B":"--R-G+.+G+.+G+.+G+.++----R--"}
    self.replacementRules={"B":"--R-G+B+G+B+G+B+G+++----R--"}
    self.axiom="-G+B+G+B+G+B+G+B++"  
    #self.replacementRules={"S":"LLLL","L":"+G.+",".":"B","B":"-RS--R-"}
    #self.axiom="S"  
    self.depth= 2
  def display(self):
    factor=pow(2,4-self.depth)
    shapesize(0.25)
    def G():
        pencolor('green')
        fd(11.55*factor)        
    def R():
        pencolor('red')
        fd(11.55*factor)
    def B():
        pencolor('black')
        circle(factor)
    def l():
        lt(45)
    def r():
        rt(45)
    def s():
        stamp()
    rules={"G":G,"B":B,"R":R,"-":l,"+":r,".":s}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,self.depth)
    print(drawing)
    draw(drawing,rules)
    update()



class koch_snowflake():
  def __init__(self):
    self.replacementRules={"F":"F-F+F-F"}
    self.axiom="F+F+F+"    
  def display(self):
    def F():
        fd(20)
    def r():
        rt(60)
    def l():
        lt(120)
    rules={"-":r,"+":l,"F":F}
    def draw(commands,rules):
      for element in commands:
          rules[element]()
    drawing=replace(self.axiom,self.replacementRules,1)
    print(drawing)
    draw(drawing,rules)
    update()

class hilbert_triangle():
  def __init__(self):
    self.replacementRules={".":"F.B+F.B+F.B+","F":"FF","B":"BB"}
    self.axiom="."    

  def display(self):
    shape('triangle')
    def F():
        fd(11.55)
    def B():
        bk(11.55)
    def l():
        lt(120)
    def s():
        stamp()
    rules={".":s,"+":l,"F":F,"B":B}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,3)
    print(drawing)
    draw(drawing,rules)
    update()


class tree():
  def __init__(self):
    self.replacementRules={".":"F-F.B+F.B-B","F":"FF","B":"BB"}
    self.axiom="."    
  def display(self):
    shape('triangle')
    shapesize(0.25,0.25,0.5)
    def F():
        fd(11.55)
    def B():
        bk(11.55)
    def l():
        lt(60)
    def r():
        rt(120)
    def s():
        stamp()
    rules={".":s,"+":r,"-":l,"F":F,"B":B}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,3)
    print(drawing)
    draw(drawing,rules)
    update()

class branches():
  def __init__(self):
    self.replacementRules={"F":"F-FB+F+FB-FB"}
    self.axiom="F"    
  def display(self):
    shape('triangle')
    shapesize(0.25,0.25,0.5)
    def F():
        fd(11.55)
    def B():
        bk(11.55)
    def l():
        lt(60)
    def r():
        rt(60)
    def s():
        stamp()
    rules={".":s,"+":r,"-":l,"F":F,"B":B}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,3)
    print(drawing)
    draw(drawing,rules)
    update()


#koch_snowflake().display()
#hilbert_triangle().display()
#tree().display()
#branches().display()
Tamil_ethno().display()
exitonclick() 
    
