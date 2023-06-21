from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("my image viewer app")

photo1 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay.png"))
photo2 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/Paomedia-Small-N-Flat-Flower.512.png"))
photo3 = ImageTk.PhotoImage(Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay-60597.jpg"))

image_list = [photo1, photo2, photo3]
# add a status bar 
status = Label(root,text="image 1 of " + str(len(image_list)))

label = Label(image=photo1)
label.grid(row=0, column=0, columnspan=3)


def f_fun(image_number):
    global label
    global f_Button
    global b_Button
    label.grid_forget()  # Remove the existing label from the grid
    label = Label(image=image_list[image_number - 1])  # Create a new label with the new image
    f_Button = Button(root, text=">>", command=lambda: f_fun(image_number + 1))
    b_Button = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == 3:
        f_Button = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    f_Button.grid(row=1, column=0)
    E_Button.grid(row=1, column=1)


def back(image_number):
    global label
    global f_Button
    global b_Button
    label.grid_forget()  # Remove the existing label from the grid
    label = Label(image=image_list[image_number - 1])  # Create a new label with the new image
    f_Button = Button(root, text=">>", command=lambda: f_fun(image_number + 1))
    b_Button = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == 1:
        b_Button = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    f_Button.grid(row=1, column=0)
    E_Button.grid(row=1, column=1)


f_Button = Button(root, text=">>", command=lambda: f_fun(2))
E_Button = Button(root, text="EXIT PROGRAM", command=root.quit, fg="red", bg="yellow")
b_Button = Button(root, text="<<", command=lambda: back(0))

f_Button.grid(row=1, column=0)
E_Button.grid(row=1, column=1)
b_Button.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3)
root.mainloop()
