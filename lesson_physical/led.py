from sense_hat import *
from time import *
from math import *
from numpy import *
myhat=SenseHat()
myhat.load_image("/home/pi/4.png")
colors2=list()
colors3=[]
colors1=[]
r=[255,0,0]
g=[0,255,0]
b=[0,0,255]
y=[255,255,0]
p=[255,0,255]
u=[0,255,255]
w=[255,255,255]
d=[0,0,0]
colors=[d,r,y,g,u,b,p,w]

for x in range(0,8):
    for y in range(0,8):
        if (x+y)>7:
            colors1.append(r)
        else:
            colors1.append(g)
        #colors2.append([x*32,y*32,0]) #only r and g
        #colors2.append([255,255*int((x+y)/8),255]) #diagonal
        colors2.append( [128+127*sign(x-y),128-127*sign(x-y),255*int((x+y)/8)])
        #colors3.append([(x+y)*16,(x+y)*16,(x+y)*16]) #all white
        #colors3.append(colors[x])
        colors3.append([32*x,32*y,int((224-32*max(x,y))*255/224)]) #OK
        #colors3.append([32*x,32*y,16*14-16*(x+y)])
       
##print(colors1)
##print(colors3)
##print(colors2)
##myhat.set_pixels(colors1)
##sleep(3)
##myhat.set_pixels(colors2)
##sleep(3)
myhat.set_pixels(colors3)
sleep(3)

##for i in range(0,3):
##    myhat.set_rotation(i*90,redraw=True)
##    sleep(1)

for i in range(0,0):
    for x in range(0,8):
        first=colors3[x*8]
        for y in range(0,8):
            if y<7:
                colors3[x*8+y]=colors3[x*8+y+1]
            else: colors3[x*8+y]=first
    myhat.set_pixels(colors3)
    sleep(1)

for i in range(0,64):
    first=colors3[0]
    for x in range(0,63):
        colors3[x]=colors3[x+1]
    colors3[63]=first
    myhat.set_pixels(colors3)
    sleep(0.1)





        

