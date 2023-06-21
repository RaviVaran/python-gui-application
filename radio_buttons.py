"""from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("my radio buttions")
r=IntVar()
r.set("1")

def clicked(value):
    label = Label(root,text=r.get())
    label.pack()
Radiobutton(root,text="option 1",variable=r,value=1,command=lambda:clicked(r.get)).pack()
Radiobutton(root,text="option 2",variable=r,value=2,command=lambda:clicked(r.get)).pack()
Radiobutton(root,text="option 3",variable=r,value=3,command=lambda:clicked(r.get)).pack()

label = Label(root,text=r.get())
label.pack()

my_Button = Button(root,text="click me",command=lambda:clicked(r.get))
my_Button.pack()
root.mainloop()"""


from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("my radio buttions")

modes = [("onion","onion"),
         ("curry","curry"),
         ("veg","veg"),
         ("biryani","biryani")]

pizza = StringVar()
pizza.set("onion")
for text,mode in modes:
     Radiobutton(root,text=text,variable=pizza,value=mode).pack()
def clicked(value):
    label = Label(root,text=pizza.get())
    label.pack()     


label = Label(root,text=pizza.get())
label.pack()
my_Button = Button(root,text="click me",command=lambda:clicked(pizza.get))
my_Button.pack()
root.mainloop()

