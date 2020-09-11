from tkinter import *

root =  Tk()

e = Entry(root, width=50, borderwidth= 5)
e.pack()
e.insert(0, "Enter you Name: ")

#Functions
def myClick():
    hello = "Hello my Dear friend, " + e.get() #GET PEGA O QUE TA ESCRITO NO INPUT
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton1 = Button(root, text="Click Me!", command=myClick, fg="white", bg="black") #Hexadecimal works

myButton1.pack()

root.mainloop()