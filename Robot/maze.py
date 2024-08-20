import tkinter as tk
from roboid import *
from threading import Thread


hamster = HamsterS()

notes = ["C4", "E4", "D4", "F4", "E4", "G4", "F4", "A4", "C5"]
left_prox = 0
right_prox = 0
run = True


def proximity():
   global run
   #left
   left = canvas.create_line(135, 125, 135, 125, fill='red')
   #right
   right = canvas.create_line(165, 125, 165, 125, fill='red')


   while run:
       global left_prox, right_prox
       left_prox = hamster.left_proximity()
       right_prox = hamster.right_proximity()
       update_left = (135, left_prox+33, 135, 125)
       canvas.coords(left, update_left)
       update_right = (165, right_prox+33, 165, 125)
       canvas.coords(right, update_right)

       l_floor, r_floor = hamster.left_floor(), hamster.right_floor()

       wait(100)


def stop():
   global run
   run = False




def keydown(event):
    if event.char == "w":
        hamster.wheels(90,90)
    elif event.char == "s":
        hamster.wheels(-90,-90)
    elif event.char == "a":
        hamster.wheels(-90,90)
    elif event.char == "d":
        hamster.wheels(90,-90)
    elif event.char == "g":
        hamster.close_gripper()
    elif event.char == "h":
        hamster.open_gripper()

def keyup(event):
    if event.char == "w" or event.char == "s" or event.char == "a" or event.char == "d" or event.char == "g" or event.char == "h":
        hamster.wheels(0,0)

# Create a tkinter window
root = tk.Tk()
root.title("Maze")


# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


# Draw a blue rectangle
canvas.create_rectangle(125, 125, 175, 175, outline='blue', fill='blue')


tk.Button(root, text="Stop", command=stop).pack()


# Start threads for proximity detection and keyboard control
prox_thread = Thread(target=proximity)
prox_thread.start()

root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

# Run the tkinter main loop
root.mainloop()


# Wait for threads to finish
run = False
prox_thread.join()
print("terminated")