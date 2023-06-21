from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("my gui image app")

photo1 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay.png"))
photo2 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/Paomedia-Small-N-Flat-Flower.512.png"))
photo3 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay-60597.jpg"))

photo_list = [photo1, photo2, photo3]
label = Label(image=photo1)

def Button_fun(first_number):
    global label
    global f_Button1
    global b_Button3

    label.grid_forget()
    label = Label(image=photo_list[first_number - 1])
    f_Button1 = Button(root, text=">>", command=lambda: Button_fun(first_number + 1))
    b_Button3 = Button(root, text="<<", command=lambda: Button_fun(first_number - 1))
    
    if first_number == 1:
        f_Button1 = Button(root, text="<<", state=DISABLED)
    elif first_number == 3:
        f_Button1 = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    f_Button1.grid(row=1, column=2)
    b_Button3.grid(row=1, column=0)

f_Button1 = Button(root, text=">>", command=lambda: Button_fun(2))
my_Button2 = Button(root, text="exit program", command=root.quit, fg="red")
b_Button3 = Button(root, text="<<", command=lambda: Button_fun(0), state=DISABLED)

label.grid(row=0, column=0, columnspan=3)
f_Button1.grid(row=1, column=2)
my_Button2.grid(row=1, column=1)
b_Button3.grid(row=1, column=0)

root.mainloop()
