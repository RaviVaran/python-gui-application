from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("check_box")
root.geometry("400x400")

def show():
    label = Label(root, text=clicked.get())
    label.pack()

clicked = StringVar()  # Define the variable for OptionMenu
clicked.set("Monday")  # Set an initial value
options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
drop = OptionMenu(root, clicked, *options)
drop.pack()

my_Button = Button(root, text="click", command=show)
my_Button.pack()

root.mainloop()
