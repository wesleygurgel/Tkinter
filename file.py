from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("File")
root.iconbitmap('imagens/icon.ico')

def open():
    global myImg
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/wesleygurgel/Desktop/Tkinter/imagens", title="Select A File",    filetypes=(("png files", "*.png"),("jpg files","*.jpg"),("all files", "*.*")))
    myLabel = Label(root, text=root.filename).pack()
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    myLabelImg = Label(image=myImg).pack()



myButton = Button(root, text="Open File", command=open).pack()



root.mainloop()