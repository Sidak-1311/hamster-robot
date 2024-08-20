# Basic Movement
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

# move forward/backward 5 cm, turn left/right 90 degrees with default velocity(30%)
hamster.move_forward(2)
hamster.move_backward(2)
hamster.turn_left(2)
hamster.turn_right(2)