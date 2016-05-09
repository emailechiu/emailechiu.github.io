from turtle import *
from functools import *

class stick(Turtle):
     def __init__(self,piles,seq):
         Turtle.__init__(self,shape='square')
         self.shapesize(5,1)
         self.pu()
         self.color('green')
         self.seq=seq
         self.piles=piles
         #piles.sticks.append(self)
         self.onclick(self.rm_pile)
     def rm_pile(self,x,y):
         self.piles.rm(self.seq) 
        
class piles():
      def __init__(self,y):
          self.sticks=[]
          self.y=y
      def init(self,n):
          for i in range(n):
              t=stick(self,i)
              t.setx(i)
              t.sety(self.y)
              self.sticks.append(t)
      def rm(self,m):
           while len(self.sticks)>m: 
              t=self.sticks.pop()
              t.color('grey')
           current[self.y]=m
           analyse(current)

tracer(0)                     
start=[1,2,3]
start=[6,4,5]
current=start
nim=[1,2,3]
def sort(a):
    b=[i for i in range(len(a))]
    for i in range(len(a)):
       for j in range(i+1,len(a)):
         if a[b[i]]>a[b[j]]: t=b[i];b[i]=b[j];b[j]=t
    print("ordered index =",b)
    sorted=[a[c] for c in b]
    print("sorted entry = " ,sorted)
    return b

setup(0.5,0.75)
setworldcoordinates(-1,-1,start[len(start)-1],len(start))
for i in range(len(start)):
    nim[i]=piles(i)
    nim[i].init(start[i])
update()
tracer(1)
current_player='you'
attractors =[(0,0,0),(1,2,3),(1,4,5),(2,4,6),(2,5,7)]

def lookahead(situation):
     ordered=sort(situation)
     sorted=[situation[ordered[i]] for i in range(len(situation))]
     #if reduce(lambda x,y:x+y,current)==0: print('game over,you win')
     if sorted==[0,0,0]: return 'lose'
     elif sorted[0:-1]==[0,0]:  return 'win'
     elif sorted[0]==0 & sorted[1]==sorted[2]: return 'lose'
     elif sorted[0]==0 & sorted[1]!=sorted[2]: return 'win'
     elif sorted[0:-1]==[1,1]: return 'win'
     elif sorted[0]==1 & sorted[1]==sorted[2]: return 'win'
     elif sorted==[1,2,3]: return 'lose'
     elif sorted[0:1]==[1,2]: return 'win'  #1,2,3
     elif sorted[0:1]==[1,3]: return 'win'  #1,3,2
     elif sorted==[1,4,5]: return 'lose'
     elif sorted[0:1]==[1,4]: return 'win'  #1,4,5
     elif sorted[0:1]==[2,3]: return 'win'
     elif sorted==[2,4,5]: return 'win'     #1,4,5
     elif sorted==[2,4,6]: return 'lose'    #attractor
     elif sorted[0:1]==[2,4]: return 'win'     #2,4,6 
     elif sorted==[2,5,6]: return 'win'     #2,4,6
     elif sorted[0:1]==[2,5,7]: return 'lose' 
     elif sorted[0:1]==[2,5]: return 'win'  #2,5,7
     elif sorted[0:1]==[2,6]: return 'win'  #2,6,4
     elif sorted[0:1]==[2,7]: return 'win'  #2,7,5
           for i in range(1,sorted[2]):
               lookahead(sorted[

        if current[ordered
        #if 
     
def calculate(sorted):
    if sorted[0]==0:
       if sorted[1]==sorted[2]: return 'lose'  # attractor
       else return 'win'
    elif sorted[0]==1:
       if sorted[1]%2 & sorted[2]-sorted[1]==1: return 'lose'  #attractor
       else return 'win'
    elif sorted[0]==2:
       if sorted[1]%2 & sorted[2]-sorted[1]==1: return 'win'  #attractor
       if sorted[1]/2%2 & sorted[2]-sorted[1]==2: return 'lose'

def analyse(current): 
   if (player)=='you': 
        player='computer'; 
        analyse(current)
     write("computer's turn")
     print(current)
     write("your turn")
analyse()
done()
