from roboid import *

hamster = HamsterS()

while True:
    print(hamster.left_floor(), hamster.right_floor())

    wait(100)