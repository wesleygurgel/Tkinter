import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('Text Box 2')


def open_text():
    myfile = filedialog.askopenfilename(initialdir="C:/Users/wesleygurgel/Desktop/Tkinter", title='Open Text Files',
                                        filetypes=(('Text Files', '*.txt'),))
    text_file = open(myfile, 'r')
    stuff = text_file.read()
    my_text.insert(tk.END, stuff)

    text_file.close()

def save_text():
    myfile = filedialog.askopenfilename(initialdir="C:/Users/wesleygurgel/Desktop/Tkinter", title='Open Text Files',
                                        filetypes=(('Text Files', '*.txt'),))
    text_file = open(myfile, 'w')
    text_file.write(my_text.get(1.0, tk.END))
    text_file.close()

my_text = tk.Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady=20, padx=10)

open_file = tk.Button(root, text='Open Text File', command=open_text)
open_file.pack(pady=20)

save_file = tk.Button(root, text='Save File', command=save_text)
save_file.pack(pady=20)

root.mainloop()
