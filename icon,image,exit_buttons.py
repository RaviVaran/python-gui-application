from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("My GUI")
root.iconbitmap("C:\\Users\\dell\\Desktop\\gui\\icons8-favicon-48.png")


# Load the image using PIL
image = Image.open("C:/Users/dell/Desktop/gui/pexels-pixabay-60597.jpg")

# Create a Tkinter-compatible photo image from the PIL image
photo = ImageTk.PhotoImage(image)

# Create a label and set the photo as its image
label = Label(root, image=photo)
label.pack()
my_button = Button(root,text="exit program",command=root.quit)
my_button.pack()

root.mainloop()
