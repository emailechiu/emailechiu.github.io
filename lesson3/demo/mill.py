from turtle import *
tracer(0)
n=5
step=50

#bear
begin_poly()
color("red","blue")
circle(step,360,20)
pu()
goto(3*step,0)
pd()
circle(step,360,20)
pu()
goto(1.5*step,0)
rt(90)
pd()
fd(step)
circle(step/4,180,10)
end_poly()
S=get_poly()
register_shape("bear",S)
b=Turtle(shape="bear")


###circle inside square
##fd(step)
##begin_poly()
##begin_fill()
##color('yellow','blue')
##circle(step,360,4)
##pu()
##lt(90)
##fd(step/3)
##rt(90)
##pd()
##circle(step/3,360,20)
##end_fill()
##end_poly
##S=get_poly()
##register_shape("donut",S)
##x=Turtle(shape="donut")
##fd(step)
##bk(step*n)
##
##begin_fill()
##color('yellow','blue')
##begin_poly()
##for j in range(1,n):
##  print(j,"in ",pos())
##  for i in range(n):
##    fd(step)
##    rt(360*j/n)
##  print(j,"ou ",pos())
##  #fd(step*2) 
##  print(j,"out",pos())
##end_fill()
##end_poly()
##S=get_poly()
##register_shape("pentagon",S)  
##t=Turtle(shape='pentagon')
##
update()
exitonclick() 
