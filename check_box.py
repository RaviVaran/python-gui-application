from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title("check_box")
root.geometry("400x400")

def showsection():
     global my_label
     my_label = Label(root,text=var.get()).pack() 

var = StringVar()      # intvar

c = Checkbutton(root,text="check box",variable=var,onvalue="on",offvalue="off")# on=put the names
c.deselect()
c.pack()




my_Button = Button(root,text="click me",command=showsection).pack()






root.mainloop()