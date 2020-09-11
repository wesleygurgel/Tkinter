from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")
root.iconbitmap('imagens/icon.ico')

frame = LabelFrame(root, text="This is my Frame", padx=15, pady=15)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Hi I'm button", command=root.quit)
b2 = Button(frame, text="I'm not a button", command=root.quit)
b.grid(row=0, column=0)
b2.grid(row=0, column=1)




root.mainloop()