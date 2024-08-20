from roboid import *
import turtle
import time

hamster = HamsterS()

win = turtle.Screen()
win.bgcolor("light green")
win.title("Turtle")

stopped = False

draw = turtle.Turtle()
draw.left(90)

screen_width, screen_height = win.window_width() // 2, win.window_height() // 2

def is_near_border(turtle, screen_width, screen_height, buffer=50):
    x, y = turtle.position()
    if abs(x) >= screen_width - buffer or abs(y) >= screen_height - buffer:
        return True
    return False

# Function to check the border continuously
def check_border_continuously():
    if is_near_border(draw, screen_width, screen_height):
        draw.setpos(0,0)
    win.ontimer(check_border_continuously, 100)  # Check every 100 milliseconds

def is_turtle_off_screen(turtle):
    x, y = turtle.pos()
    screen_width = win.window_width() / 2
    screen_height = win.window_height() / 2
    
    if abs(x) > screen_width or abs(y) > screen_height:
        return True
    return False

window_size = 5 
acc_x_window = []
acc_y_window = []
acc_z_window = []

def moving_average(data, window_size):
    return sum(data) / len(data)

while True:
    acc_x = hamster.acceleration_x()
    acc_y = hamster.acceleration_y()
    acc_z = hamster.acceleration_z()

    acc_x_window.append(acc_x)
    acc_y_window.append(acc_y)
    acc_z_window.append(acc_z)

    if len(acc_x_window) > window_size:
        acc_x_window.pop(0)
        acc_y_window.pop(0)
        acc_z_window.pop(0)

    smoothed_acc_x = moving_average(acc_x_window, window_size)//200
    smoothed_acc_y = moving_average(acc_y_window, window_size)//200
    smoothed_acc_z = moving_average(acc_z_window, window_size)//200
    wait(100)

    if hamster.left_proximity() > 70 and hamster.right_proximity() > 70:
        if stopped:
            stopped = False
            print("going")
        else:
            stopped = True
            print("stopped")

    if (smoothed_acc_x > -5 and smoothed_acc_x < 5) and (smoothed_acc_y > -5 and smoothed_acc_y < 5):
        pass
    elif not stopped:
        draw.forward(-smoothed_acc_y)
        time.sleep(0.1)