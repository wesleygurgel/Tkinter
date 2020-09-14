from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menu")
root.iconbitmap('imagens/icon.ico')
root.geometry("400x400") #Define o tamanho do root

#Drop Down Boxers

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
clicked = StringVar()
clicked.set(days[0])

drop = OptionMenu(root, clicked, *days).pack()

def day():
    myLabel = Label(root, text=clicked.get()).pack()

myButton = Button(root, text="Which day you want?", command=day).pack()


root.mainloop()
