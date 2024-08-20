import tkinter as tk    
from roboid import *
import turtle

hamster = HamsterS()

colors = ["blue", "green", "red", "yellow", "black"]
color = 1

alpha = 0.2 
smoothed_acc_x = hamster.acceleration_x()
smoothed_acc_y = hamster.acceleration_y()
smoothed_acc_z = hamster.acceleration_z()

#FILTER TO MAKE ACCELERATION VALUES FLUCTUATE LESS
def exponential_moving_average(current_value, previous_acc, alpha):
    return alpha * current_value + (1 - alpha) * previous_acc

win = turtle.Screen()
win.bgcolor("light blue")

draw = turtle.Turtle()
draw.setheading(0)
draw.pensize(6)

screen_width, screen_height = win.window_width() // 2, win.window_height() // 2

#CHECK IF TURTLE IS NEAR BORDER
def is_near_border(turtle, screen_width, screen_height, buffer=50):
    x, y = turtle.position()
    if abs(x) >= screen_width - buffer or abs(y) >= screen_height - buffer:
        return True
    return False

def check_border_continuously():
    if is_near_border(draw, screen_width, screen_height):
        draw.pu()
        draw.setpos(0,0)
        draw.pd()
    win.ontimer(check_border_continuously, 100) 

x = True
#STATES TO ASSIGN TURTLES DIRECTION
state = "horizontal" 

while True:
    check_border_continuously()
    acc_x = hamster.acceleration_x()
    acc_y = hamster.acceleration_y()
    acc_z = hamster.acceleration_z()

    #FILTERING OUT THE ACCELERATION VALUES AND MAKING THEM SMOOTHER
    smoothed_acc_x = exponential_moving_average(acc_x, smoothed_acc_x, alpha)//200
    smoothed_acc_y = exponential_moving_average(acc_y, smoothed_acc_y, alpha)//200
    smoothed_acc_z = exponential_moving_average(acc_z, smoothed_acc_z, alpha)//200
    
    #USING PROX SENSORS TO MAKE THE TURTLE CHANGE STATE TO HORIZONTAL OR VERTICAL
    if hamster.left_proximity() > 30 and hamster.right_proximity() > 30:
        if state == "horizontal":
            state = "vertical"
            draw.setheading(90)
        elif state == "vertical":
            draw.setheading(0)
            state = "horizontal"
        else:
            draw.setheading(0)
            state = "horizontal"
    else:
        #USING THE PROXIMITY TO MAKE THE TURTLE TURN 45 DEGREES LEFT AND RIGHT
        if hamster.right_proximity() > 30 and hamster.right_proximity() > hamster.left_proximity():
            draw.right(45)
            state = "diagonal"
        elif hamster.left_proximity() > 30 and hamster.left_proximity() > hamster.right_proximity():
            draw.left(45)
            state = "diagonal"

    #STATE AND THEIR SMOOTHED ACCELERATION VALUES TO MAKE THE TURTLE MOVE
    if state == "horizontal":
        if smoothed_acc_x < -10 or smoothed_acc_x > 10:
            draw.forward(-smoothed_acc_x)
            acc_x = 0

    if state == "vertical":
        if smoothed_acc_y < -10 or smoothed_acc_y > 10:
            draw.forward(-smoothed_acc_y)
            
            x = False

    if state == "diagonal":
        if smoothed_acc_y < -10 or smoothed_acc_y > 10:
            draw.forward(-smoothed_acc_y)

    #CHANGE THE COLOR OF THE TURTLE
    if hamster.left_floor() > 80 and hamster.right_floor() > 80:
        match color:
            case 1:
                color = 2
            case 2:
                color = 3
            case 3:
                color = 4
            case 4:
                color = 5
            case 5:
                color = 1

        draw.color(colors[color - 1])
        draw.fillcolor("black")

    wait(100)