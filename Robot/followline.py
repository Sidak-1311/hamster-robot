from roboid import *
import time
import tkinter as tk
from threading import Thread


hamster = HamsterS()
Quit = False


def line_both():
   global Quit
   speed = 40
   kp = 0.6


   while not Quit:
       floor_r = hamster.right_floor()
       floor_l = hamster.left_floor()
       d = floor_r - floor_l
       print(d)
       correction = int(d*kp)
       hamster.wheels(speed-correction, speed + correction)
       time.sleep(0.1)


def stop():
   global Quit
   Quit = True
   hamster.wheels(0,0)


root = tk.Tk()
root.geometry("300x300")


tk.Button(root, text = "Stop", command = stop).pack()


follow = Thread(target = line_both)
follow.start()


root.mainloop()


follow.join()
print("Terminated")