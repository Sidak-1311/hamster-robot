from roboid import *
import random

hamster = HamsterS()
while True:
    key = Keyboard.read()
    if key:
        if key == "w":
            hamster.wheels(90, 90)
            flag = True
        elif key == "s":
            flag = True
            hamster.wheels(-90 , -90 )
        elif key == "a":
            flag = True
            hamster.wheels(-90 , 90)
        elif key == "d":
            flag = True
            hamster.wheels(90 ,-90)
        elif key == "x":
            hamster.wheels(0,0)

        elif key == "g":
            hamster.close_gripper()
        elif key == "h":
            hamster.open_gripper()
            
        wait(10)