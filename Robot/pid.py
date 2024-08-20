from roboid import *
import time
import tkinter as tk
from threading import Thread

robot = HamsterS()

Kp = 0.75

integral = 0
prev_error = 0

def line_both():
    global integral
    speed = 65
    while True:
        left_prox =  robot.left_proximity()
        right_prox = robot.right_proximity()
        error = right_prox - 52
        P = Kp * error
        
        # integral += error * 0.1
        # I = Ki * integral
        

        correction = P + 0

            #90- right agnle -15 , forward-77

    #turn right --> right angle <50, 
    #turn left forward >60
        # if right_prox>40:
        #     robot.wheels(speed, speed)
        # # elif right_prox<18:
        #     robot.turn_right(90)

        robot.wheels(speed - int(correction), speed + int(correction))
        if left_prox>66:
            robot.turn_left(90)
        
        time.sleep(0.1)

line_both()