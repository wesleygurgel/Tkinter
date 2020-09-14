from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('imagens/icon.ico')

#Variables
#v = IntVar()
#v.set("1") #Define o que vem por padrão

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, value in MODES:
    Radiobutton(root, text=text, variable=pizza, value=value).pack(anchor=W)

#Functions
def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Buttons
#Radiobutton(root, text="Option 1", variable=v, value=1, command= lambda: click(v.get())).pack()
#Radiobutton(root, text="Option 2", variable=v, value=2, command= lambda: click(v.get())).pack()

myButton = Button(root, text="Click on Me", command= lambda: click(pizza.get()))
myButton.pack()

#Label

root.mainloop()