from tkinter import *
root=Tk()

our_canvas=Canvas(root,width=300,height=200,bg="white")
our_canvas.pack()
#creating rectangle
our_canvas.create_line(0,0,300,200,fill="blue")
root.mainloop()