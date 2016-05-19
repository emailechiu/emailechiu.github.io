from tkinter import *
from random import *
from time import *
tk=Tk()
canvas=Canvas(tk,height=500,width=500)
canvas.pack()
tk.update()
bgimage=PhotoImage(file='background.gif')
stickmanimage=PhotoImage(file='stick1.gif')
coords=[(10,50),(110,110),(210,110),(50,300),(200,350),(25,400)]
platforms=[]
for i in range(5):
   for j in range(5):
       canvas.create_image(i*100,j*100,anchor=NW,image=bgimage)
class Platform:
    def __init__(self,photo_image,x,y,size):
       self.photo_image=photo_image
       canvas.create_image(x,y,anchor=NW,image=photo_image)
       self.x=x
       self.y=y
       self.xr=self.x+size
       self.yr=self.y+10
       #print(self.x,self.y)
       #self.coordinates=Coords(x,y,x+size,y+size/10)
       tk.update()

class Door:
     def __init__(self):
         self.photo_image=PhotoImage(file='door1.gif')
         canvas.create_image(10,10,anchor=NW,image=self.photo_image)
         self.x=10
         self.y=10

class Stickman:
     def __init__(self,canvas,x,y):
        self.canvas=canvas
        self.photo_image=[]
        self.photo_image.append(PhotoImage(file='stick1.gif'))
        self.photo_image.append(PhotoImage(file='stick2.gif'))
        self.photo_image.append(PhotoImage(file='stick3.gif'))
        self.photo_image.append(PhotoImage(file='stick1L.gif'))
        self.photo_image.append(PhotoImage(file='stick2L.gif'))
        self.photo_image.append(PhotoImage(file='stick3L.gif'))
        self.id=canvas.create_image(x,y,anchor=NW,image=self.photo_image[0])
        self.x=x
        self.y=y
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.move(self.id,30,370)
        self.orientation=0 #right
        self.current=0 #1st one
     def move(self,event):
       pos=self.canvas.coords(self.id)
       print(pos)
       self.current=(self.current+1)%3
       if event.keysym=='Left' and pos[0]-15>0:
          self.orientation=3
          canvas.itemconfig(self.id,image=self.photo_image[self.orientation+self.current])
          canvas.move(self.id,-self.x,0)
       elif event.keysym=='Right' and pos[0]+15<self.canvas_width:
          self.orientation=0
          canvas.itemconfig(self.id,image=self.photo_image[self.orientation+self.current])
          canvas.move(self.id,self.x,0)
       elif event.keysym=='Up' and pos[1]-15>0:
          canvas.itemconfig(self.id,image=self.photo_image[self.orientation+self.current])
          canvas.move(self.id,0,-10*self.y)
       while self.onplatform()==0 and pos[1]+15<self.canvas_height:
             pos=self.canvas.coords(self.id)
             canvas.itemconfig(self.id,image=self.photo_image[self.orientation+self.current])
             canvas.move(self.id,0,1)
             tk.update()
             sleep(0.01)
       tk.update()      
     def onplatform(self):
         pos=self.canvas.coords(self.id)
         for i in platforms:
            diffx=(pos[0]-i.x)*(pos[0]-i.xr)
            diffy=(pos[1]+30-i.y)*(pos[1]+30-i.yr)
            if diffx<0 and diffy<0:
               return 1
         return 0
        
def create_platforms():
    for i in coords:
       p=Platform(PhotoImage(file='platform2.gif'),i[0],i[1],100)
       platforms.append(p)
door=Door()
create_platforms() 
stickman=Stickman(canvas,5,5)
canvas.bind_all('<KeyPress-Up>',stickman.move)
canvas.bind_all('<KeyPress-Down>',stickman.move)
canvas.bind_all('<KeyPress-Left>',stickman.move)
canvas.bind_all('<KeyPress-Right>',stickman.move)
tk.update()
mainloop()
