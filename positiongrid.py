from tkinter import *

root =  Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My names is Oliver Queen!")
myLabel3 = Label(root, text="            ")
myLabel4 = Label(root, text="Submit bro!").grid(row=2,column=0) # We can do that

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()