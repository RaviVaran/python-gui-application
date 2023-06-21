from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title("slides")
root.geometry("400x400")
vertical = Scale(root,from_=0,to=200)
vertical.pack()
horizantal = Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizantal.pack()

def open():
    global my_label
    my_label = Label(root,text=horizantal.get()).pack()

my_Button = Button(root,text="click me",command=open).pack()
root.mainloop()