from turtle import *
from time import *
tracer(0,0)
ht()
def koch(d,d_min):
  if d<=d_min:
       fd(d)
  else:
       koch(d/3,d_min)
       rt(60)
       koch(d/3,d_min)
       lt(120)
       koch(d/3,d_min)
       rt(60)
       koch(d/3,d_min)

def snowflake(size,d_min):
    koch(size,d_min)       
    lt(120)
    koch(size,d_min)
    lt(120)
    koch(size,d_min)
    lt(120)

def animate(size,d_min):
    for i in range(5):
       d_min=d_min/3
       snowflake(size,d_min)
       update()
       sleep(1)
       reset() 
       ht() 
    ontimer(animate(243,243),0)
    exitonclick()

#snowflake(243,81)
#update()
#exitonclick()
animiate(243,243)



