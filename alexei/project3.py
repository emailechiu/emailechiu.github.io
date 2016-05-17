from turtle import *
speed(10)
tracer(0)
pencolor('red')
fillcolor('blue')
begin_fill()
number=10
for i in range(number):
    circle(100)
    lt(360/number)

end_fill()
update()
