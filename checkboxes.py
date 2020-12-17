from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Viewer")
root.iconbitmap('imagens/icon.ico')
root.geometry("400x400") #Define o tamanho do root

var = BooleanVar()
var2 = BooleanVar()
#c = Checkbutton(root, text="Check this box, I dare you!", variable=var).pack()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
d = Checkbutton(root, text="You Like food?", variable=var2)

c.pack()
c.deselect()
d.pack()
d.deselect()

def show():
    # if var.get() == 0:
    #     myLabel = Label(root, text="Unchecked").pack()
    # else:
    #     myLabel = Label(root, text="Checked").pack()
    myLabel = Label(root, text=var.get()).pack()
    myLabel2 = Label(root, text=var2.get()).pack()
    var2.set(0)

myButton = Button(root, text="Checked or Unchecked:?", command=show).pack()


root.mainloop()