from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open Image Files")
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir=r"C:\Users\dell\Desktop\gui", title="Select a file", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    label = Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


button = Button(root,text="open_file",command=open).pack()

root.mainloop()
