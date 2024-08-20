import turtle
import sys
from roboid import *

hamster = HamsterS()

screen = turtle.Screen()
stopped = False

def close_window(x, y):
    turtle.bye()
    sys.exit()

draw = turtle.Turtle()
draw.penup()
draw.left(90)

acc_x1 = hamster.acceleration_x()
acc_y1 = hamster.acceleration_y()
acc_z1 = hamster.acceleration_z()
wait(250)
acc_x2 = hamster.acceleration_x()
acc_y2 = hamster.acceleration_y()
acc_z2 = hamster.acceleration_z()

accelerationx = (acc_x2 - acc_x1)//75
accelerationy = (acc_y2 - acc_y1)//75
accelerationz = (acc_z2 - acc_z2)//75

if hamster.left_proximity() > 70 and hamster.right_proximity() > 70:
    if stopped:
        stopped = False
        print("going")
    else:
        stopped = True
        print("stopped")

if (accelerationx > -5 and accelerationx < 5) and (accelerationy > -5 and accelerationy < 5):
    pass
elif not stopped:
    draw.forward(accelerationy)

screen.onscreenclick(close_window)

turtle.mainloop()