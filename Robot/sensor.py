import time  # for sleep
import threading
import tkinter as tk    
from roboid import *

hamster = HamsterS()

# Initialize EMA variables for each axis
alpha = 0.2 # Smoothing factor (0 < alpha <= 1). Higher alpha gives more weight to recent data.
smoothed_acc_x = hamster.acceleration_x()
smoothed_acc_y = hamster.acceleration_y()
smoothed_acc_z = hamster.acceleration_z()

def exponential_moving_average(current_value, previous_ema, alpha):
    return alpha * current_value + (1 - alpha) * previous_ema

while True:
    # Get current acceleration values
    acc_x = hamster.acceleration_x()
    acc_y = hamster.acceleration_y()
    acc_z = hamster.acceleration_z()

    # Apply EMA filter
    smoothed_acc_x = exponential_moving_average(acc_x, smoothed_acc_x, alpha)//200
    smoothed_acc_y = exponential_moving_average(acc_y, smoothed_acc_y, alpha)//200
    smoothed_acc_z = exponential_moving_average(acc_z, smoothed_acc_z, alpha)//200

    print("Smoothed Acceleration: ", smoothed_acc_x, smoothed_acc_y)

    wait(200)