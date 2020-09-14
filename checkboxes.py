from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Viewer")
root.iconbitmap('imagens/icon.ico')
root.geometry("400x400") #Define o tamanho do root

var = StringVar()
var2 = StringVar()
#c = Checkbutton(root, text="Check this box, I dare you!", variable=var).pack()
c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="Checked", offvalue="Unchecked")
d = Checkbutton(root, text="You Like food?", variable=var2, onvalue="Yes, I like", offvalue="No, i don't")
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

myButton = Button(root, text="Checked or Unchecked:?", command=show).pack()


root.mainloop()