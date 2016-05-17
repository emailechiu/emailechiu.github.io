from turtle import *
shape('square')
shapesize(5,1,12)
#for i in range(1000):
    #rt(10)
begin_poly()
for i in range(3):
    for g in range(3):
        lt(120)
        forward(100)
    lt(120)
end_poly()
register_shape('wind mill',get_poly())
    
shape('wind mill')
shapesize(1,1,1)
for i in range(1000):
    rt(10)
shapesize(1,1,1)
