from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Wesleyzinho")
root.iconbitmap('imagens/icon.ico')

myImg = ImageTk.PhotoImage(Image.open("imagens/perito.png"))
myLabel = Label(image=myImg)
myLabel.pack()








button_quit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_quit.pack()
root.mainloop()