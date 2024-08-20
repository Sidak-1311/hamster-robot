import tkinter as tk
from roboid import *
from threading import Thread

hamster = HamsterS()

left_prox = 0
right_prox = 0
run = True
obstacle = False

def proximity():
    global run, obstacle
    #left
    left = canvas.create_line(135,125,135,125,fill='red')
    #right
    right = canvas.create_line(165,125,165,125,fill='red')
    while run:
        global left_prox, right_prox
        left_prox =  hamster.left_proximity()
        right_prox = hamster.right_proximity()
        update_left = (135, left_prox+33, 135, 125)
        canvas.coords(left, update_left)
        update_right = (165, right_prox+33, 165, 125)
        canvas.coords(right, update_right)

        wait(100)

def stop():
    global run
    run = False
    hamster.wheels(0,0)



# Create a tkinter window
root = tk.Tk()
root.title("Sensor")

# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Draw a blue rectangle
canvas.create_rectangle(125, 125, 175, 175, outline='blue', fill='blue')

tk.Button(root, text = "Stop", command=stop).pack()

prox_thread = Thread(target=proximity)
prox_thread.start()

# Run the tkinter main loop
root.mainloop()

prox_thread.join()

print("Terminated")