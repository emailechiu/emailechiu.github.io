from turtle import *
from canvasvg import *
def func(x): 
    if x<100: return 0
    elif x>300: return 0
    else: return 100-(x-200)**2/100 
for t in range(400): goto(t,func(t))
pu()
home()
shape('turtle')
for t in range(400): goto(t,func(t))
saveall('roller_coaster.svg',Screen()._canvas)
