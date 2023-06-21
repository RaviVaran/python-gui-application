from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("create new window")
top = Toplevel()

my_Image = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay.png"))
my_label = Label(top,image=my_Image).pack()

root.mainloop()
