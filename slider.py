from tkinter import *
from PIL import ImageTk, Image
import progresbar as progressbar

root = Tk()
root.title("Viewer")
root.iconbitmap('imagens/icon.ico')
root.geometry("400x400") #Define o tamanho do root

vertical = Scale(root, from_=400, to=1000)
vertical.pack()

def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))  # Define o tamanho do root

horizontal = Scale(root, from_=400, to=1000, orient=HORIZONTAL)
horizontal.pack()

myButton = Button(root, text="Click Me!", command=slide).pack() #usando o button você deve tirar a variavel var

root.mainloop()