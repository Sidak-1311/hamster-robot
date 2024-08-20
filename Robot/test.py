import time  # for sleep
import threading
import tkinter as tk    
from roboid import *
import turtle

hamster = HamsterS()

# Initialize EMA variables for each axis
alpha = 0.2  # Smoothing factor (0 < alpha <= 1). Higher alpha gives more weight to recent data.
smoothed_acc_x = hamster.acceleration_x()
smoothed_acc_y = hamster.acceleration_y()
smoothed_acc_z = hamster.acceleration_z()

def exponential_moving_average(current_value, previous_ema, alpha):
    return alpha * current_value + (1 - alpha) * previous_ema

win = turtle.Screen()
win.bgcolor("light blue")

draw = turtle.Turtle()

screen_width, screen_height = win.window_width() // 2, win.window_height() // 2

# Function to check if the turtle is within 50 pixels of the border
def is_near_border(turtle, screen_width, screen_height, buffer=50):
    x, y = turtle.position()
    if abs(x) >= screen_width - buffer or abs(y) >= screen_height - buffer:
        return True
    return False

# Function to check the border continuously
def check_border_continuously():
    if is_near_border(draw, screen_width, screen_height):
        draw.setpos(0, 0)
    win.ontimer(check_border_continuously, 100)  # Check every 100 milliseconds

while True:
    # Get current acceleration values
    check_border_continuously()
    acc_x = hamster.acceleration_x()
    acc_y = hamster.acceleration_y()
    acc_z = hamster.acceleration_z()

    # Apply EMA filter
    smoothed_acc_x = exponential_moving_average(acc_x, smoothed_acc_x, alpha)
    smoothed_acc_y = exponential_moving_average(acc_y, smoothed_acc_y, alpha)
    smoothed_acc_z = exponential_moving_average(acc_z, smoothed_acc_z, alpha)

    # Check X-axis movement (left/right)
    if abs(smoothed_acc_x) > 10:
        if smoothed_acc_x > 0:
            draw.setheading(0)  # Point right
        else:
            draw.setheading(180)  # Point left
        draw.forward(abs(smoothed_acc_x) // 200)

    # Check Y-axis movement (up/down)
    if abs(smoothed_acc_y) > 10:
        if smoothed_acc_y > 0:
            draw.setheading(90)  # Point up
        else:
            draw.setheading(270)  # Point down
        draw.forward(abs(smoothed_acc_y) // 200)

    wait(100)
