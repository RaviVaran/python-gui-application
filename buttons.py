from tkinter import *

root = Tk()
e = Entry(root,width=50,bg="blue",fg="white")
e.pack()
e.insert(0,"enter your name: ")

def myclick():
    hello="hello"+e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()
mybutton = Button( root,text="enter name", command = myclick,fg="blue")
mybutton.pack()

root.mainloop()
