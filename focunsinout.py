from tkinter import *

def main():
    global text

    root=Tk()

    l1=Label(root,text="Field 1:")
    l2=Label(root,text="Field 2:")
    t1=Text(root,height=4,width=40)
    e1=Entry(root)
    e2=Entry(root)
    l1.grid(row=0,column=0,sticky="e")
    e1.grid(row=0,column=1,sticky="ew")
    l2.grid(row=1,column=0,sticky="e")
    e2.grid(row=1,column=1,sticky="ew")
    t1.grid(row=2,column=0,columnspan=2,sticky="nw")

    root.grid_columnconfigure(1,weight=1)
    root.grid_rowconfigure(2,weight=1)

    root.bind_class("Entry","<FocusOut>",focusOutHandler)
    root.bind_class("Entry","<FocusIn>",focusInHandler)

    text = t1
    root.mainloop()

def focusInHandler(event):
    text.insert("end","FocusIn %s\n" % event.widget)
    text.see("end")

def focusOutHandler(event):
    text.insert("end","FocusOut %s\n" % event.widget)
    text.see("end")


if __name__ == "__main__":
    main();