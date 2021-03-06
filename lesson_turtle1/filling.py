from turtle import *
tracer(0)
##mode("standard")
##begin_poly()
##fd(100)
##bk(50)
##lt(90)
##fd(50)
##bk(100)
##end_poly()
##register_shape('cross',get_poly())
##reset()
##c=Turtle(shape='cross')
##c.fd(200)
##c.color("red")
##
##begin_poly()
##circle(50)
##end_poly()
##register_shape('circ',get_poly())
##reset()
##b=Turtle(shape='circ')
##b.fd(200)
##b.color("green")

mode("logo")
begin_poly()
fd(100)
bk(10)
lt(90)
fd(30)
bk(50)
pu()
bk(10)
end_poly()
register_shape('sross',get_poly())
reset()

begin_poly()
fd(100)
rt(90)
circle(50)

lt(90)
bk(20)
rt(90)
circle(90)

lt(90)
fd(10)
rt(90)
circle(70)

##goto(-90,200)
##goto(90,200)
##goto(0,80)

end_poly()
register_shape('sirc',get_poly())
reset()

begin_poly()
fd(100)
rt(90)
circle(-40,-180)
rt(90)
fd(60)
rt(90)
circle(-40,-180)
end_poly()
register_shape('B',get_poly())
reset()

begin_poly()
rt(90)
circle(30)
goto(15,15)
goto(0,60)
#goto(7.5,7.5)
end_poly()
register_shape('peace',get_poly())
reset()

begin_poly()
bk(100)
rt(90)
circle(-30)
rt(45)
fd(30)
rt(45)
circle(-15,180)
rt(45)
fd(30)
register_shape('teardrop',get_poly())
reset()

poly=((-30,0),(0,30),(30,0),(0,-30),(-30,0),(30,0),(0,30),(0,-30),(-30,0))
poly=((0,30),(0,0),(-30,0),(0,30),(30,0),(0,-30))
poly=((-30,30),(30,30),(30,-30),(-30,-30),(-30,30),(-20,30),(-20,-30),(-10,-30),(-10,30))
poly=((-10,30),(-10,-30),(-30,-30),(-30,30),(30,30),(30,-30),(-10,-30),(-10,30))


register_shape('circlecross',poly)
reset()
print('start of compound heading',heading())

mode('standard')
com=Shape("compound")

lt(90)
fd(100)
rt(90)
begin_poly()
circle(50)
end_poly()
com.addcomponent(get_poly(),'red','blue')

rt(90)
fd(200)
lt(90)
begin_poly()
circle(-20)
end_poly()
com.addcomponent(get_poly(),'blue','red')

register_shape('dumbell',com)
reset()

mode("logo")
s=Turtle(shape='sross')
s.fd(200)
s.color('purple')
print(s.get_shapepoly())
t=Turtle(shape='sirc')
t.color('yellow')
print(t.get_shapepoly())
u=Turtle(shape='B')
u.color('blue')
print(u.get_shapepoly())
p=Turtle(shape='peace')
p.color('green')
print(p.get_shapepoly())
update()
q=Turtle(shape='teardrop')
q.color('orange')
print(q.get_shapepoly())

r=Turtle(shape='circlecross')
r.color('magenta')
update()

d=Turtle(shape='dumbell')

for i in range(120):
    pensize(i/12)
    pencolor(i/120,0,1-i/120)
    circle(i,15,1)

fillcolor('green')
pensize(1)
n=12
begin_fill()
for i in range(n):
    circle(100)
    rt(360/n)
end_fill()


lt(90)
fd(300)
rt(90)
bgcolor('red')
fillcolor('green')
n=12

begin_fill()
for i in range(n):
    fd(50)
    pu()
    fd(90)
    pd()
    fd(50)
    rt(360/n*7)
end_fill()

update()

#exitonclick()


