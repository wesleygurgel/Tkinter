import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
# Creating a Label Widget
root.title("Wesley Gurgel")
root.geometry("400x400")

def step():
    for x in range(5):
        myProgress['value'] += 20
        root.update_idletasks()
        time.sleep(1)
    if myProgress['value'] == 100:
        label = tk.Label(root, text="Yeah we finish")
        label.pack()


myProgress = ttk.Progressbar(root, orient=tk.HORIZONTAL,
                             length=300, mode='determinate')

myProgress.pack(pady=20)

myButton = tk.Button(root, text="Progress", command=step)
myButton.pack(pady=20)

root.mainloop()