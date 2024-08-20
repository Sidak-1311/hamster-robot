from roboid import *
import turtle
import time

hamster = HamsterS()

win = turtle.Screen()
win.bgcolor("light green")
win.title("Draw with robot")

draw = turtle.Turtle()

def stop_move():
    if hamster.left_proximity() > 70 and hamster.right_proximity > 70:
        return True
    else:
        return False

while True:
    acc_x1 = abs(hamster.acceleration_x())
    acc_y1 = abs(hamster.acceleration_y())
    wait(50)
    acc_x2 = abs(hamster.acceleration_x())
    acc_y2 = abs(hamster.acceleration_y())

    accelerationx = abs(acc_x2 - acc_x1)//100
    accelerationy = abs(acc_y2 - acc_y1)//100

    tilt = hamster.tilt()
    direction = ""
    prev_state = ""

    match tilt:
        case -3:
            direction = "up"
            time.sleep(0.2)
            prev_state = direction
        case -2:
            direction = "right"
            time.sleep(0.2)
            prev_state = direction
        case 3:
            direction = "down"
            time.sleep(0.2)
            prev_state = direction
        case 2:
            direction = "left"
            time.sleep(0.2)
            prev_state = direction
        case _:
            direction = prev_state

    match direction:
        case "up":
            draw.setheading(90)
        case "down":
            draw.setheading(270)
        case "right":
            draw.setheading(0)
        case "left":
            draw.setheading(180)

    if direction == "up":
        draw.forward(accelerationy)
    elif direction == "down":
        draw.forward(accelerationy)
    elif direction == "right":
        draw.forward(accelerationx)
    elif direction == "left":
        draw.forward(accelerationx)