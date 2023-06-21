from tkinter import *

from PIL import ImageTk,Image

root = Tk()

root.title("frames")
frame = LabelFrame (root,text="my label",padx=20,pady=20)
frame.pack(padx=10,pady=10)

my_Button = Button(frame,text="dont'click me",fg="red")
my_Button.grid(row=0,column=0)

my_Button1 = Button(frame,text="dont'click me",fg="yellow")
my_Button1.grid(row=1,column=1)


root.mainloop()