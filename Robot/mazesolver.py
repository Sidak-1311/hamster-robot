from roboid import *

hamster = HamsterS()

while True:
    left_prox = hamster.left_proximity()
    right_prox = hamster.right_proximity()
    print(right_prox)
    if right_prox < 30:
        if left_prox > 50:
            hamster.wheels(100, 100)
        else:
            hamster.wheels(60, 30)
            wait(50)
    else:
        hamster.turn_right(90)