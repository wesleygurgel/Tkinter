import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk,Image
from tkinter import filedialog
import time
from datetime import date
from maskedentry import MaskedWidget
from csv import DictWriter
from csv import DictReader

root =  tk.Tk()

def salvardados():
    with open('memoria.csv', 'w', encoding="utf8", newline="") as arquivo:

        cabecalho = ['URL CNJ', 'Tribunal', 'PasswordTribunal', 'NumProtocolo']
        escritor_csv = DictWriter(arquivo, cabecalho)
        escritor_csv.writeheader()

        urlcnj = urlCNJ_entry.get()
        tribunal = tribunal_entry.get()
        senhatribunal = passwordTribunal_entry.get()
        numprotocolo = numProtocolo_entry.get()

        escritor_csv.writerow({'URL CNJ': urlcnj, 'Tribunal': tribunal, 'PasswordTribunal': senhatribunal, 'NumProtocolo': numprotocolo})


def recuperardados():
    with open('./memoria.csv', encoding="utf8") as arquivo:
        leitor_csv = DictReader(arquivo)
        for linha in leitor_csv:
            urlCNJ_entry.insert(0, linha['URL CNJ'])
            tribunal_entry.insert(0, linha['Tribunal'])
            passwordTribunal_entry.insert(0, linha['PasswordTribunal'])
            numProtocolo_entry.insert(0, linha['NumProtocolo'])



# Validates
urlcnjvalidate = root.register(salvardados)



# Parâmetros da Requisição
frame_requisicao = tk.LabelFrame(root, text="Parâmetros da Requisição", padx=40, pady=15)
frame_requisicao.grid(row=0, column=0, sticky=tk.E+tk.N+tk.S+tk.W, ipadx=5, ipady=5, padx=5, pady=5)

# Labels
urlCNJ_label = tk.Label(frame_requisicao, text="URL endpoint CNJ:").grid(row=0,sticky=tk.E, pady=(0,5))
tribunal_label = tk.Label(frame_requisicao, text="Tribunal:").grid(row=1, sticky=tk.E, pady=(0,5))
passwordTribunal_label = tk.Label(frame_requisicao, text="Senha do Tribunal:").grid(row=2, sticky=tk.E, pady=(0,5))
numProtocolo_label = tk.Label(frame_requisicao, text="Nº Protocolo:").grid(row=3, sticky=tk.E, pady=(0,5))

# Entrys
urlCNJ_entry = tk.Entry(frame_requisicao, width = 40, validate='focusout', validatecommand=urlcnjvalidate)
urlCNJ_entry.grid(row=0,column=1)
tribunal_entry = tk.Entry(frame_requisicao, width = 40, validate='focusout', validatecommand=urlcnjvalidate)
tribunal_entry.grid(row=1,column=1)
passwordTribunal_entry = tk.Entry(frame_requisicao, show="*" ,width = 40, validate='focusout', validatecommand=urlcnjvalidate)
passwordTribunal_entry.grid(row=2,column=1)
numProtocolo_entry = tk.Entry(frame_requisicao, width = 40, validate='focusout', validatecommand=urlcnjvalidate)
numProtocolo_entry.grid(row=3,column=1)

# -----------------------------------------------------------------------------------------------------

root.mainloop()