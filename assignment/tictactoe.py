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

def add3(a,b): # given a =[1,2,3],b=[5,8,-2]  add(a,b)=>[6,10,1]
    return (abs(a[0]+b[0]),abs(a[1]+b[1]),abs(a[2]+b[2]))
    
def clamp(value): # clamp(3)=2 clamp(-1)=0 clamp(1)=1 clamp(2)=2 clamp(0)=0
    if value>2: value=2
    if value<0: value=0
    return value

def board(): # blue color for x=2 and y=0-7, x=5 and y=0-7, same with y
    color=[0,0,255]
    for i in range(0,8):
    # you need to fill in here


def display(pos,add): # display(0,1) will light up the first 4-LED square, display(0,0) will make it go away
    global who
    # add code here

def wholeboard(color): # this will lightup the entire board with the color, e.g [255,0,0]

def diagonal(color): # this will make the diagonal in one color

def edge(color): # this will make the edge light up in one color


def pushed_up(event): # move the display position up, shut off the previous display
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        print("UP")

def pushed_down(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        print("DOWN")

def pushed_left(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        print("LEFT")

def pushed_right(event):
    global y,x,who,entered
    if event.action!=stick.ACTION_RELEASED:
        print("RIGHT")

def pushed_enter(event): # when enter is pressed user need to see if any one wins, prepare to change color
    global y,x,who,state,entered,presses
    if event.action!=stick.ACTION_RELEASED:                    
        print("MIDDLE")

def evaluate(): # see if there is any winners, returns 1 if red wins, -1 if green wins, and 0 if no more moves but it is a tie, and 999 if game is not ended
    global state # possible state is [1 1 1 -1 0 -1 -1 1 0] and red wins

def restart(): # if game ended restart it by resetting all the global variables
    global x,y,entered,state,who
    sense.clear()
    #sense.set_rotation(180)
    x=1
    y=1
    entered=1
    state=[0]*9
    who=1
    board()

# Here is the main program
mystick.direction_up=pushed_up
mystick.direction_down=pushed_down
mystick.direction_left=pushed_left
mystick.direction_right=pushed_right
mystick.direction_middle=pushed_enter
restart()
while presses>=0:
    presses=-1
    sleep(30) #If there are no keypresses within 30 seconds exit

sense.show_message("Game End")
sense.load_image("/home/pi/emailechiu.github.io/lesson_physical/space_invader.png")

