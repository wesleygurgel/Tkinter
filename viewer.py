from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Me and MY Love")
root.iconbitmap('imagens/icon.ico')

myImg1 = ImageTk.PhotoImage(Image.open("imagens/1.jpg").resize((450,350), Image.ANTIALIAS))
myImg2 = ImageTk.PhotoImage(Image.open("imagens/2.jpg").resize((450,350), Image.ANTIALIAS))
myImg3 = ImageTk.PhotoImage(Image.open("imagens/3.jpg").resize((450,350), Image.ANTIALIAS))
myImg4 = ImageTk.PhotoImage(Image.open("imagens/4.jpg").resize((550,450), Image.ANTIALIAS))

image_list = [myImg1, myImg2, myImg3, myImg4]

myLabel = Label(image=myImg1)
myLabel.grid(row=0,column=0, columnspan=3)

#Functions
def forward(image_number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    myLabel.grid(row=0, column=0, columnspan=3)

def back(image_number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    myLabel.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()