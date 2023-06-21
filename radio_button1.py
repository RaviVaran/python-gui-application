from  tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("gui radio buttons")

Toppings = [("gorantla","gorantla"),
          ("hai","hai"),
          ("ravi","ravi")
        ]

pizza = StringVar()
pizza.set("ravi")
for text,toppings in Toppings:
     Radiobutton(root,text=text,variable=pizza,value=toppings).pack(anchor=W)

def click(value):
    label = Label(root,text=pizza.get())
    label.pack(anchor=W)

label = Label(root,text=pizza.get())
label.pack(anchor=W)
my_Button = Button(root,text="click me",command=lambda:click(pizza.get)).pack(anchor=W)

root.mainloop()