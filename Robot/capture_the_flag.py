from roboid import *

hamster = HamsterS()

state = 0
speed = 50
Kp = 0.7
x_coord = int(input("Enter your x-coordinate: "))
x_count = 0
y_coord = int(input("Enter your y coordinate: "))
y_count = 0
while True:
    floor_l = hamster.left_floor()
    floor_r = hamster.right_floor()

    error = 50-floor_l
    proportional = error * Kp
    correction = proportional
    hamster.wheels(speed - correction, speed + correction)
    wait(0.05)
    if floor_l < 30 and floor_r < 30:
       # hamster.buzzer(1000)
        wait(100)
       # hamster.buzzer(0)
        if state == 0:
            x_count += 1
            if x_count == x_coord:
                hamster.turn_right()
                state = 1
            wait(100)
        if state == 1:
            y_count += 1

        if y_count == y_coord+1:
            hamster.wheels(0, 0)
            wait(100)
            break

    print('Done')