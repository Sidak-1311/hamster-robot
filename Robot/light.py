from roboid import * 
import random

hamster = HamsterS()

while True:
    hamster.left_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255),)

    hamster.left_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    hamster.right_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    hamster.right_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    wait(100)
    