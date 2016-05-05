from turtle import *
from functools import *
#print(reduce(lambda x,y:x+y, range(1,3)))
n = 6
color=['red','green','blue','purple','yellow','orange']
pegs=[n,0,0]
pile=[[],[],[]]
setworldcoordinates(-1,-1,3,n+1)
tracer(0)
ht()
for i in range(3):  
    for j in range(pegs[i],0,-1):
       t=Turtle(shape='square')
       t.shapesize(5,3*j)
       t.pu()
       t.color(color[j-1])
       t.setx(i)
       t.sety(pegs[i]-j)
       pile[i].append(t)
       #t.write("home")

def hanoi(n,src,dest,aux):
    global steps
    if n>1:
       hanoi(n-1,src,aux,dest)
       hanoi(1,src,dest,aux)
       hanoi(n-1,aux,dest,src)
    else:
       #print("from: ",pegs,end="")
       t=pile[src].pop()
       t.goto(dest,pegs[dest])
       pegs[src]=pegs[src]-1
       pegs[dest]=pegs[dest]+1
       pile[dest].append(t)
       steps+=1
       #print("to: ",pegs)

steps=0
hanoi(n,0,1,2)
update()
print("Moving",n,"Pegs requires",steps,"steps")
#exitonclick()

