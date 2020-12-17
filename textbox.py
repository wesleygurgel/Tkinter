import tkinter as tk

root = tk.Tk()
root.title('Text Box')

def clear():
    my_text.delete(1.0, tk.END)

def get_text():
    myLabel.config(text=my_text.get(1.0, tk.END))


my_text = tk.Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady=20, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

clear_button = tk.Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

gettext_button = tk.Button(button_frame, text="Get Text", command=get_text)
gettext_button.grid(row=0, column=1)

myLabel = tk.Label(root, text='')
myLabel.pack(pady=10)

root.mainloop()