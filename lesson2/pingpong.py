from tkinter import *
from time import *
from random import *
def hello():
    print('Hello ' , 2+5)

tk=Tk()
button=Button(tk,text='hey',command=hello)
button.pack()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
my_image=PhotoImage(file='cat.gif')
#canvas.create_image(0,0,anchor=NW,image=my_image)            
#c1=colorchooser.askcolor()
c1=['yellow','orange']
tk.update()
#print("canvas size is ",canvas.winfo_height(),canvas.winfo_width())
class Ball:
    def __init__(self,canvas,color,paddle):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,0,300)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.x=10
        self.y=10
        self.paddle=paddle
        print("canvas size is ",self.canvas_width,self.canvas_height)
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        pos_paddle=self.canvas.coords(self.paddle.id)
        print(pos,pos_paddle,self.id,self.paddle.id, self.x,self.y)
        if pos[2]<=pos_paddle[0] or pos[0]>=pos_paddle[2]  or pos[3]<=pos_paddle[1] or pos[1]>=pos_paddle[3]:
            if pos[0]<=0 or pos[2]>=self.canvas_width: self.x=-self.x
            if pos[1]<=0 or pos[3]>=self.canvas_height: self.y=-self.y
        else: self.y=-self.y


class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(10,10,100,30,fill=color)
        self.canvas.move(self.id,0,200)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.x=10
        self.y=10
    def move(self,event):
       pos=self.canvas.coords(self.id) 
       if event.keysym=='Left' and pos[0]>0: canvas.move(self.id,-self.x,0)
       elif event.keysym=='Right' and pos[2]<self.canvas_width: canvas.move(self.id,self.x,0)
       elif event.keysym=='Up' and pos[1]>0: canvas.move(self.id,0,-self.y)
       elif event.keysym=='Down' and pos[3]<self.canvas_height: canvas.move(self.id,0,self.y)
       tk.update()


        
def moveTriangle(event):
    for x in range(60):
       if event.keysym=='Left': canvas.move(tri1,5,5)
       elif event.keysym=='Right': canvas.move(tri2,5,5)
       elif event.keysym=='Up': canvas.move(arc1,5,5)
       elif event.keysym=='Down': canvas.move(rect1,5,5)
       tk.update()
       sleep(0.05)

tri1=canvas.create_polygon(10,10,10,60,50,35,fill='red')
tri2=canvas.create_polygon(100,10,100,60,140,35,fill='green')
arc1=canvas.create_arc(10,10,200,100,extent=270,style=ARC,fill='purple')
arc2=canvas.create_arc(110,110,300,200,extent=350,style=ARC,fill='magenta')
arc2=canvas.create_oval(210,210,400,300,fill='blue')
rect1=canvas.create_rectangle(10,10,randrange(100),randrange(100),fill=c1[1])

line=canvas.create_line(0,0,500,500)
##canvas.bind_all('<KeyPress-Up>',moveTriangle)
##canvas.bind_all('<KeyPress-Down>',moveTriangle)
##canvas.bind_all('<KeyPress-Left>',moveTriangle)
##canvas.bind_all('<KeyPress-Right>',moveTriangle)


# Ball
paddle=Paddle(canvas,'blue')
ball=Ball(canvas,'red',paddle)
# Paddle
canvas.bind_all('<KeyPress-Up>',paddle.move)
canvas.bind_all('<KeyPress-Down>',paddle.move)
canvas.bind_all('<KeyPress-Left>',paddle.move)
canvas.bind_all('<KeyPress-Right>',paddle.move)
while 1:
    ball.draw()
    tk.update()
    sleep(0.05)

