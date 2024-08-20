from roboid import *

hamster = Hamster()

while True:
    for hz in range(500,700,10):
        hamster.buzzer(hz)
        wait(20)

    break