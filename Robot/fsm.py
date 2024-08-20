from roboid import *
import tkinter as tk
from threading import Thread

hamster=  HamsterS()

State = None
states = {}
states["red"] = [255,0,0]
states["blue"] = [0, 255, 0]
states["green"] = [0, 0, 255]
states["white"] = [0,0,0]

Quit = False

def keydown(event):
    global State
    if event.char == "1":
        State = "red"
    elif event.char == "2" and State == "red":
        State = "blue"
    elif event.char == "3" and State == "blue":
        State = "green"

def keyup(event):
    global State
    

def change_state():
    global State, Quit
    while not Quit:
        if State in states:
            color = states[State]
            hamster.left_rgb(color[0], color[1], color[2])
            hamster.right_rgb(color[0], color[1], color[2])

def stop():
    global Quit
    Quit = True

root = tk.Tk()

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

tk.Button(root, text = "Stop", command = stop).pack()

change = Thread(target = change_state)
change.start()

root.mainloop()

change.join()

print("End")