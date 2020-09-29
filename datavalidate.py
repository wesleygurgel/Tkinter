import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk,Image
from tkinter import filedialog
import time
from datetime import date
from maskedentry import MaskedWidget
from csv import DictWriter
from tkinter import messagebox
from csv import DictReader


root = tk.Tk()
root.title("Protocolos CNJ")
#root.iconbitmap('imagens/icon.ico')
#root.geometry("400x400")

# Dia atual função
def current_time():
    todaystring = str(date.today())

    # Variável Global sendo utilizada na validação do campo Data em validate()
    global current_year

    todaysplit = todaystring.split("-")
    current_day = todaysplit[2]
    current_month = todaysplit[1]
    current_year = todaysplit[0]

    # Parte usada para o Calendário em Período - Auxilia na parte de transformar o ano em 4 CARACTERES. Ex.:"2020"
    global year_calendario
    year_calendario = current_year
    list(year_calendario)
    year_calendario = year_calendario[2] + year_calendario[3]
    year_calendario = int(year_calendario)

    today = current_day + current_month + current_year
    return today

# Funções do DATE ------------------------------------------------------------------------------------------------------
# Funções Referentes ao ícone de Calendário para Período ---------------------------------------------------------------
def data_inicio():
    data1 = 1
    data2 = 0
    open_window_date(data1,data2)

def data_final():
    data2 = 1
    data1 = 0
    open_window_date(data1,data2)

def open_window_date(data1,data2):
    global top
    top = tk.Toplevel()
    top.title("Defina a Data")
    top.geometry("400x300")
    global cal
    cal = Calendar(top, selectmode="day", year=2020, month=6, day=27)
    cal.pack(pady=20, fill="both", expand=True)
    submitedate = tk.Button(top, text="Selecionar Data", command=lambda: grab_date(data1,data2)).pack(pady=(0,10))

def grab_date(data1,data2):
    # Mudando para estilo BR
    datastring = cal.get_date()
    data = datastring.split("/")

    # Salvando em variáves de dia, mês e ano -> Acrescentando também o '0' para os meses inferiores a Outubro (10) e para Dias
    global year
    day = data[1]
    month = data[0]
    year = data[2]

    if len(month) < 2:
        month = "0" + month

    if len(day) < 2:
        day = "0" + day

    yearInt = int(year)
    if  year_calendario >= yearInt > 0:
        year = "20"+year
    else:
        year = "19"+year


    # Colocando no Entry da tela principal
    if data1 == 1:
        data1_entry.insert(0, day+month+year)
    if data2 == 1:
        data2_entry.insert(0, day+month+year)

    top.destroy()

# ---------------------------------------------------------------------------------------------------------------------

def popuperror():
    print("Entrei em popupError")
    response = messagebox.showerror("Data", "Data digitada é inválida.\nTente novamente.")
    # data1_entry.widgets.fields[dataInicial].set("")
    data1_entry.insert(0, "")
    data1_entry.clean()


def validate(*args):
    # print(f'Data Inicial: {data1_entry.get()}')
    # print(f'Data Final: {data2_entry.get()}')
    dataInicial = data1_entry.get()
    dataFinal = data2_entry.get()

    # Divindo Data Inicial ---------------------------------------------------------------------------------------
    dataInicial_split1 = dataInicial.split("/")

    dataInicial_day = dataInicial_split1[0]
    dataInicial_month = dataInicial_split1[1]
    dataInicial_year = dataInicial_split1[2]

    # Dividindo Data Final ---------------------------------------------------------------------------------------
    dataFinal_split1 = dataFinal.split("/")

    dataFinal_day = dataFinal_split1[0]
    dataFinal_month = dataFinal_split1[1]
    dataFinal_year = dataFinal_split1[2]

    # print(f'Data Inicial day = {dataInicial_day}, {type(dataInicial_day)}')
    # print(f'Data Inicial month = {dataInicial_month}, {type(dataInicial_month)}')
    # print(f'Data Inicial year = {dataInicial_year}, {type(dataInicial_year)}\n')
    #
    # print(f'Data Final day = {dataFinal_day}, {type(dataFinal_day)}')
    # print(f'Data Final month = {dataFinal_month}, {type(dataFinal_month)}')
    # print(f'Data Final year = {dataFinal_year}, {type(dataFinal_year)}\n')
    #
    # print(f'Ano atual = {current_year}')
        # -------------------------------- DIA ---------------------------------------#
    if dataInicial_day == "__" or int(dataInicial_day) > 31 or int(dataInicial_day) == 0:
        response = messagebox.showerror("Dia Incorreto", "Preencha o campo com o valor correto.\nCampo 'Dia' em 'De:'")
        return
    elif dataFinal_day == "__" or int(dataFinal_day) > 31 or int(dataFinal_day) == 0:
        response = messagebox.showerror("Dia Incorreto", "Preencha o campo com o valor correto.\nCampo 'Dia' em 'Até:'")
        return

        # -------------------------------- MÊS ---------------------------------------#
    elif dataInicial_month == "__" or int(dataInicial_month) > 12 or int(dataInicial_month) == 0:
        popuperror()
    elif dataFinal_month == "__" or int(dataFinal_month) > 12 or int(dataFinal_month) == 0:
        popuperror()

        # -------------------------------- ANO ---------------------------------------#
    elif int(dataInicial_year) > int(dataFinal_year) or int(dataInicial_year) < 2000 or dataInicial_year == "____":
        popuperror()
    elif int(dataFinal_year) > int(current_year) or dataFinal_year == "____":
        popuperror()










# Parâmetros da Requisição
frame_requisicao = tk.LabelFrame(root, text="Parâmetros da Requisição", padx=40, pady=15)
frame_requisicao.grid(row=0, column=0, sticky=tk.E+tk.N+tk.S+tk.W, ipadx=5, ipady=5, padx=5, pady=5)


# -----------------------------------------------------------------------------------------------------

# Frame para Periodo
numero_protocolo_frame = tk.LabelFrame(frame_requisicao, text="Período Correspondido")
numero_protocolo_frame.grid(row=5, columnspan=2, sticky=tk.E+tk.N+tk.S+tk.W, padx=5, pady=5, ipadx=5, ipady=5)

# Buttons Calendar
calendarImage = ImageTk.PhotoImage(Image.open("imagens/calendar1.png").resize((20,20), Image.ANTIALIAS))

periodo_buttonInicio = tk.Button(numero_protocolo_frame, image=calendarImage, command=data_inicio)
periodo_buttonInicio.grid(row=0, column=2, padx=(5,0))

periodo_buttonFinal = tk.Button(numero_protocolo_frame, image=calendarImage, command=data_final)
periodo_buttonFinal.grid(row=0, column=5, padx=(5,0))

# -----------------------------------------------------------------------------------------------------

# Periodo Datas com Mask
global data1
data1 = 0
definedate1_label = tk.Label(numero_protocolo_frame, text="De:")
definedate1_label.grid(row=0)

data1_entry = MaskedWidget(numero_protocolo_frame, 'fixed', mask='99/99/9999')
data1_entry.grid(row=0, column=1, padx=(5,0), pady=(5,5))


global data2
data2 = 0
definedate2_label = tk.Label(numero_protocolo_frame, text="Até:")
definedate2_label.grid(row=0, column=3, padx=(10,0))

data2_entry = MaskedWidget(numero_protocolo_frame, 'fixed', mask='99/99/9999')
data2_entry.grid(row=0, column=4, padx=(5,0), pady=(5,5))

# BIND FOCUSOUT
data2_entry.bind("<FocusOut>", validate)

today = current_time()
data2_entry.insert(0, today)

# -----------------------------------------------------------------------------------------------------


buscar_paginas = tk.Button(frame_requisicao, text="Buscar Páginas")
buscar_paginas.grid(row=6, column=1, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

# -----------------------------------------------------------------------------------------------------

root.mainloop()