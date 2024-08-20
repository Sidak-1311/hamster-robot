from roboid import *

hamster = HamsterS()
Quit = False

hamster.open_gripper()
state = "looking"

limit = input()

def stop():
    global Quit
    Quit = True
    hamster.wheels(0,0)

while not Quit:
    if state == "looking":
        hamster.wheels(60,60)
        if (hamster.right_floor() < 60 or hamster.left_floor() < 60):
            hamster.turn_right(50)

        if hamster.right_proximity() > 50 and hamster.left_proximity() > 50:
            hamster.open_gripper()
            hamster.close_gripper()
            state = "grab"
            print("Cup grabbed")

        if hamster.right_proximity() > 65 and hamster.left_proximity() < 45:
            hamster.turn_right(20)
        if hamster.left_proximity() > 65 and hamster.right_proximity() < 45:
            hamster.turn_left(20)

        wait(100)
    if state == "grab":
        hamster.wheels(80,80)
        if hamster.right_floor() < 30 or hamster.left_floor() < 30:
            state = "looking"
            print("Cup outside")
            hamster.move_forward(5)
            hamster.open_gripper()
            hamster.move_backward(15)
            hamster.turn_right(45)


        wait(100)
