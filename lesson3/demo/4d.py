from turtle import *
def next(p,a=1,b=2,c=1,d=1):
   n=[a]
   for i in range(len(p)-1):
       n.append(b*p[i]+c*p[i+1])
   n.append(d*p[len(p)-1])
   return n 


p=[1]
print("Young's Triangle")
for i in range(10):
   p=next(p,1,1,1,1)
   print(p)

p=[1]
print("Dimension n's dimension n to 1 count")
for i in range(10):
   p=next(p,1,2,1,2)
   print(p)

d=50
tracer(0)
ht()
for i in range(8):
##   fd(d)
##   rt(45)
##   fd(d)
##   rt(135)
##   fd(d)
##   rt(45)
##   fd(d)
##   rt(45)

   fd(d)
   rt(90)
   fd(d)
   rt(90)
   fd(d)
   rt(90)
   fd(d)
   rt(90)

   fd(d)
   rt(45)

update()
exitonclick()

