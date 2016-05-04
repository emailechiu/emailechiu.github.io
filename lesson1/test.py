from turtle import *
ondrag(goto)
shape("circle")
pensize(3)
def jump(x,y):
    pu()
    goto(x,y)
    pd()

onscreenclick(jump)
for n in "0123456789":
    onkey(lambda c=int(n):
             pensize(2*c+1),n)

listen()
pencolor(0,0,1) 
done()

