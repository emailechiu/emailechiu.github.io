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
           analyse()

tracer(0)                     
start=[1,2,3]
current=start
nim=[1,2,3]
setup(0.1,0.4)
setworldcoordinates(-1,-1,start[len(start)-1],len(start))
for i in range(len(start)):
    nim[i]=piles(i)
    nim[i].init(start[i])
update()
tracer(1)

def analyse(): 
     if reduce(lambda x,y:x+y,current)==0: print('game over')
     else: print(current)

analyse()
