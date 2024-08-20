import time
import threading
import tkinter as tk
from roboid import *

hamster = HamsterS()
desired_distance = 50  # Desired distance from the object



def follow_object():
    while True:
        left_proximity = hamster.left_proximity()
        right_proximity = hamster.right_proximity()
        
        print("Proximity: ", left_proximity, right_proximity)
        
        # Calculate the average distance from the object
        distance = (left_proximity + right_proximity) / 2

        if distance < desired_distance:
            # Too close, slow down
            hamster.wheels(85, 85)  # Move forward slowly
        elif distance > desired_distance:
            # Too far, speed up
            hamster.wheels(100, 100)  # Move forward faster
        else:
            # Maintain current speed
            hamster.wheels(100, 100)

        # Turn towards the side with the lower proximity reading
        if left_proximity < right_proximity:
            # Object is more on the left, turn slightly right
            hamster.wheels(100, 60)
        elif right_proximity < left_proximity:
            # Object is more on the right, turn slightly left
            hamster.wheels(60, 100)
        else:
            # Object is centered, move forward
            hamster.wheels(100, 100)

        # Update GUI
        data = {
            "left_proximity": 100 - left_proximity,
            "right_proximity": 100 - right_proximity,
        }
        update_gui(data)
        time.sleep(0.1)

def update_gui(data):
    root.after(0, lambda: _update_canvas(data))

def _update_canvas(data):
    canvas.coords(left_proximity_line, 135, 125, 135, 125 - data['left_proximity'])
    canvas.coords(right_proximity_line, 165, 125, 165, 125 - data['right_proximity'])

root = tk.Tk()
root.title("Hamster Robot Sensor Data")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_rectangle(125, 125, 175, 175, outline='blue', fill='blue')

left_proximity_line = canvas.create_line(135, 125, 135, 25, fill='red')
right_proximity_line = canvas.create_line(165, 125, 165, 25, fill='red')

sensor_thread = threading.Thread(target=follow_object)
sensor_thread.daemon = True
sensor_thread.start()

root.mainloop()