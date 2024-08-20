from turtle import Screen
from tkinter import *

screen = Screen()
screen.setup(width=600, height=400)


def do_something():
    print("Good bye")


canvas = screen.getcanvas()
button = Button(canvas.master, text="Exit", command=do_something)

button.pack()
button.place(x=300, y=100)  # place the button anywhere on the screen

screen.exitonclick()