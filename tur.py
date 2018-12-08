
from turtle import *

def stop():
    global running
    running = False


def main():
    global running
    z = True
    left(10)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    print(pos())
    penup()
    goto(50,50)
    pendown()
    left(10)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
if __name__=='__main__':
    main()
    mainloop()