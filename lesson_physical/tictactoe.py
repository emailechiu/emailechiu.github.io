#!/usr/bin/python3
from sense_hat import *
from sense_hat import stick
from math import *
from time import sleep
sense=SenseHat()
mystick=stick.SenseStick()
x=1
y=1
entered=1
state=[0]*9
who=1
presses=0

def add3(a,b):
    return (abs(a[0]+b[0]),abs(a[1]+b[1]),abs(a[2]+b[2]))
    
def clamp(value):
    if value>2: value=2
    if value<0: value=0
    return value

def board():
    color=(0,0,255)
    for i in range(0,8):
        sense.set_pixel(2,i,color)
        sense.set_pixel(i,2,color)
        sense.set_pixel(5,i,color)
        sense.set_pixel(i,5,color)

def display(pos,add):
    global who
    px=pos%3*3
    py=pos//3*3
    color=((64+63*who)*add, (64-63*who)*add,0)
    oldcolor=sense.get_pixel(px,py)
    newcolor=add3(oldcolor,color)
    #print(pos," pos and who ",who,"px ",px, " py ",py,oldcolor,'old and new color', newcolor)
    for z in range(0,4):
        sense.set_pixel(px+z//2,py+z%2,newcolor)

def pushed_up(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        #print("UP")
        if entered==1: entered=0
        else: display(x+3*y,-1)
        y=clamp(y-1)
        display(x+3*y,1)
def pushed_down(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        #print("DOWN")
        if entered==1: entered=0
        else: display(x+3*y,-1)
        y=clamp(y+1)
        display(x+3*y,1)
def pushed_left(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        #print("LEFT")
        if entered==1: entered=0
        else: display(x+3*y,-1)
        x=clamp(x-1)
        display(x+3*y,1)
def pushed_right(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        #print("RIGHT")
        if entered==1: entered=0
        else: display(x+3*y,-1)
        x=clamp(x+1)
        display(x+3*y,1)
def pushed_enter(event):
    global y,x,who,state,entered,presses
    if event.action!=stick.ACTION_RELEASED:                    
        #print("MIDDLE")
        presses+=1
        if state[x+3*y]==0:
            entered=1
            state[x+3*y]=who
            who=-who
            winner=evaluate()
            if winner<999:
                sleep(1)
                colors=[[128+127*winner,128-127*winner,0]]*64
                sense.set_pixels(colors)
                sleep(1)
                restart()               
##def pushed_any(event):
##    global x,y
##    if event.action!=stick.ACTION_RELEASED:
##        print(x," x and y ",y)

def evaluate():
    global state
    for i in range(0,3):
        if state[i*3]+state[i*3+1]+state[i*3+2]==3: return 1
        if state[i*3]+state[i*3+1]+state[i*3+2]==-3: return -1
        if state[i]+state[i+3]+state[i+6]==3: return 1
        if state[i]+state[i+3]+state[i+6]==-3: return -1
    if state[2]+state[4]+state[6]==3: return 1
    if state[2]+state[4]+state[6]==-3: return -1
    if state[0]+state[4]+state[8]==3: return 1
    if state[0]+state[4]+state[8]==-3: return -1
    if sum(list(map(abs,state)))==9: return 0
    return 999

def restart():
    global x,y,entered,state,who
    sense.clear()
    #sense.set_rotation(180)
    x=1
    y=1
    entered=1
    state=[0]*9
    who=1
    board()


mystick.direction_up=pushed_up
mystick.direction_down=pushed_down
mystick.direction_left=pushed_left
mystick.direction_right=pushed_right
mystick.direction_middle=pushed_enter
#mystick.direction_any=pushed_any
restart()
while presses>=0:
    presses=-1
    sleep(30) #If there are no keypresses within 30 seconds exit

sense.show_message("Game End")
sense.load_image("/home/pi/emailechiu.github.io/lesson_physical/space_invader.png")

