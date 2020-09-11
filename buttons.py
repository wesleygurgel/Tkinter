from tkinter import *

root =  Tk()

#Functions
def myClick():
    myLabel = Label(root, text="OMG YOU REALLY CLICK ON ME")
    myLabel.pack()

myButton1 = Button(root, text="Click Me!", command=myClick, fg="red", bg="black") #Hexadecimal works
myButton2 = Button(root, text="I'm Disable!", state=DISABLED)
myButton3 = Button(root, text="Widht 50 and Height = 30!", padx=50, pady=30)


myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()