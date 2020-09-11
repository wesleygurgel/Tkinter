from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Window")
root.iconbitmap('imagens/icon.ico')

def open():
    top = Toplevel()
    top.title("I'm in a next level")
    global myImg
    myImg = ImageTk.PhotoImage(Image.open("imagens/perito.png"))
    myLabel = Label(top, image=myImg).pack()
    btn2= Button(top, text="Close Window", command=top.destroy).pack()

myButton = Button(root, text="Open my second Window", command=open).pack()

root.mainloop()