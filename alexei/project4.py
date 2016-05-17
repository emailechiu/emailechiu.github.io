from turtle import *
shape('triangle')
speed(10)
pencolor('red')
fillcolor('blue')
begin_fill()
number=8
for i in range(number):
    for g in range(3):
        lt(120)
        forward(100)
    lt(360/number) 
    

end_fill()
update() 
