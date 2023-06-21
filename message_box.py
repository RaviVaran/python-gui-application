from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root = Tk()

root.title("message box")
#showinfo,showwarning,showerror,askquesion,askokcancel

def popup():
    response=messagebox.askquestion("my message box","hello world")
    Label(root,text=response).pack()
    #if response == 1:
       # Label(root,text="you clicked yes ").pack()
   # else:
        #Label(root,text="you clicked nos ").pack()
       
response = Button(root,text="popup",command=popup).pack(anchor=W)


root.mainloop()