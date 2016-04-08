from turtle import *
speed(1)
ht()

def replace(seq,replacementRules,n):
  result=seq
  if n>=0:
    newseq=""
    for element in seq:
        newseq = newseq + replacementRules.get(element,element)
    result=replace(newseq,replacementRules,n-1)
  return result


class koch():
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
    draw(drawing,rules)
    update()
    #exitonclick() 

class triangle():
  def __init__(self):
    self.replacementRules={".":"F.B+F.B+F.B+"}
    self.axiom="."    

  def display(self):
    shape('triangle')
    def F():
        fd(11.55*2)
    def B():
        bk(11.55*2)
    def l():
        lt(120)
    def s():
        stamp()
    rules={".":s,"+":l,"F":F,"B":B}
    def draw(commands,rules):
      for element in commands:
          rules[element]() 
    drawing=replace(self.axiom,self.replacementRules,1)
    print(drawing)
    draw(drawing,rules)
    update()
    #exitonclick() 


#koch().display()
triangle().display()
    
