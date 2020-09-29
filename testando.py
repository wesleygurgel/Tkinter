import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk,Image
import time
from datetime import date
from maskedentry import MaskedWidget

root = tk.Tk()

txt_dictionary = {
    'Quantidade de Páginas Processadas':'0',
    'Quantidade de Páginas com Error':'0'
}

# Definindo Frame para tela
frame_progresspanel = tk.LabelFrame(root, text="Painel de Progresso", padx=10, pady=10)
frame_progresspanel.grid(sticky=tk.E + tk.N + tk.S + tk.W)

# Painel de Progresso
txt_progress = tk.Text(frame_progresspanel, height=10, width=60, wrap=tk.WORD, padx=10, pady=10)
txt_progress.grid(row=0, column=0, pady=1)
frame_progresspanel.grid_columnconfigure(0, weight=1)
frame_progresspanel.grid_rowconfigure(1, weight=1)

# Escrevendo no TXT
txt_progress.insert(tk.INSERT, txt_dictionary['Quantidade de Páginas Processadas'] + '\n')
txt_progress.insert(tk.INSERT, txt_dictionary['Quantidade de Páginas com Error'])










# def progressbar():
#     pwin = Toplevel(root)
#     pwin.geometry('350x40+100+100')
#     pwin.title('Sample progressbar')
#     pbar = Progressbar(pwin, orient="horizontal", length=300,
#                        mode="indeterminate")
#     pbar.place(x=10, y=5, height=20, width=300)
#     print('starting loading')
#     pbar.start()
#     pwin.update()
#
#
# Button(root, text='PBAR', command=progressbar).pack()
root.mainloop()