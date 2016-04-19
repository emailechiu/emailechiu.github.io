"""         turtle-example-suite:

              tdemo_teddy.py

A drawing sent in by a reader of
"Python fuer Kids", just after she had
read chapter 2, which introduces
turtle graphics.
"""
from turtle import *

from canvasvg import *
def main():
    mode("logo")
    tracer(0) ###speed(10)
    shape("arrow")
    pensize(3)
    circle(66)
    rt(180)
    circle(66)
    pu()
    lt(90)
    fd(33)
    rt(90)
    fd(34)
    pd()
    fillcolor("blue")
    begin_fill()
    circle(33)
    end_fill()
    pu()
    fd(15)
    lt(90)
    fd(4)
    rt(90)
    pd()
    fillcolor("black")
    begin_fill()
    circle(11)
    end_fill()
    pu()
    home()
    lt(90)
    fd(33)
    lt(90)
    fd(34)
    lt(180)
    pd()
    fillcolor("blue")
    begin_fill()
    circle(33)
    end_fill()
    pu()
    bk(15)
    rt(90)
    bk(4)
    lt(90)
    pd()
    fillcolor("black")
    begin_fill()
    circle(11)
    end_fill()
    pu()
    home()
    lt(180)
    fd(70)
    pd()
    fd(30)
    circle(30, 180)
    pu()
    rt(180)
    circle(-30, -180)
    lt(180)
    pd()
    circle(-30, 180)
    rt(180)
    circle(30, 90)
    rt(90)
    fillcolor("red")
    begin_fill()
    circle(30, 180)
    end_fill()
    pu()
    home()
    fd(80)
    rt(90)
    fd(100)
    fillcolor("brown")
    pd()
    lt(50)
    circle(-70, 200)
    pu()
    home()
    fd(80)
    lt(90)
    fd(100)
    pd()
    rt(50)
    circle(70, 200)
    pu()
    home()
    lt(90)
    fd(190)
    lt(90)
    fd(40)
    pd()
    circle(190, 180)
    pu()
    home()
    fd(80)
    pd()
    circle(50, 60)
    rt(180)
    circle(-50, 60)
    rt(180)
    circle(-60, 60)
    lt(180)
    circle(60, 60)
    lt(180)
    circle(-30, 60)
    pu()
    home()
    bk(110)
    lt(90)
    fd(20)
    pd()
    fd(1)
    pu()
    fd(19)
    pd()
    fd(1)
    pu()
    rt(180)
    fd(60)
    pd()
    fd(1)
    pu()
    fd(19)
    pd()
    fd(1)
    pu()
    rt(90)
    fd(10)
    rt(90)
    fd(10)
    pd()
    fd(1)
    pu()
    fd(60)
    pd()
    fd(1)
    pu()
    home()
    ht()
    update()
    saveall('teddy.svg',Screen()._canvas)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

