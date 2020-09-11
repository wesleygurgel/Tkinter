from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('imagens/icon.ico')

#showinfo, showwarning, showerror, askquestion, aksokcancel, askyesno
#Diferença entre aksquestion e askyesno
# ASKquestion | returns: YES = yes | NO = no
# ASKyesno, aksokcancel | returns: YES = 1 | NO = 0

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello your asshole?")
    Label(root, text=response).pack() #YES = 1 | NO = 0
    if response == 1:
        Label(root, text="KKKKKKKKKK assholeee").pack()
    else:
        Label(root, text="OMG I really thought you are").pack()

Button(root, text="Popup", command=popup).pack()






root.mainloop()