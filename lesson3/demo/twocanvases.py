from turtle import TK, TurtleScreen, RawTurtle 
root=TK.Tk()
cv1 = TK.Canvas(root,width=300,height=200,bg='yellow')
cv2 = TK.Canvas(root,width=300,height=200,bg='blue')
cv1.pack()
cv2.pack()

top = TurtleScreen(cv1)
top.bgcolor('yellow')
top_turtle=RawTurtle(top)
bottom=TurtleScreen(cv2)
bottom.bgcolor('blue')
bottom_turtle=RawTurtle(bottom)
TK.mainloop()
