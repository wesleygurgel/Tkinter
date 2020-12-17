import tkinter as tk
from datetime import date
from tkinter import messagebox

from PIL import ImageTk, Image
from tkcalendar import *

from maskedentry import MaskedWidget

root = tk.Tk()
root.title("Data Validate")
#root.iconbitmap('imagens/icon.ico')
#root.geometry("400x400")

# Dia atual função
def current_time():
    todaystring = str(date.today())

    todaysplit = todaystring.split("-")
    current_day = todaysplit[2]
    current_month = todaysplit[1]
    current_year = todaysplit[0]

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
    submitedate = tk.Button(top, text="Selecionar Data", command=lambda: grab_date_calendar(data1,data2)).pack(pady=(0,10))

def juntar_data(dataDesejada):
    # Função para que a data funcione na Máscara aplicada em Período
    dataList = dataDesejada.split("/")
    dataOficial = dataList[0]+dataList[1]+dataList[2]
    return dataOficial

def grab_date_calendar(data1, data2):
    datastring = cal.get_date()
    dataCalendar = juntar_data(datastring)

    if data1 == 1:
        data1_entry.insert(0, dataCalendar)
    if data2 == 1:
        data2_entry.insert(0, dataCalendar)

    top.destroy()

# ---------------------------------------------------------------------------------------------------------------------

def dataManipulada(dataParaManipular, funcao):
    if funcao == "inverter":
        # SPLIT EM: DD/MM/YYYY
        listaDeData = list(dataParaManipular.split("/"))
        return listaDeData[2] + '-' + listaDeData[1] + '-' + listaDeData[0]

    elif funcao in ["dia", "mes", "ano"]:
        data_index = {
            "dia": 0,
            "mes": 1,
            "ano": 2
        }
        listaDeData = list(dataParaManipular.split("/"))
        print(f'Data para mudar: {listaDeData}')
        print(funcao)
        return listaDeData[data_index.get(funcao)]

    elif funcao == "ano_atual":
        data = current_time()
        data = data[4]+data[5]+data[6]+data[7]
        return data


def validate(event):

    data = event.widget.get()
    data = data.split("/")

    dataDay = data[0]
    dataMonth = data[1]
    dataYear = data[2]

    if event.widget is data1_entry:
        evento = data1_entry
    else:
        evento = data2_entry

    data_Current_Year = dataManipulada(evento.get(), "ano_atual")

        # -------------------------------- DIA ---------------------------------------#
    if dataDay == "__" or int(dataDay) > 31 or int(dataDay) == 0:
        response = messagebox.showerror("Dia Incorreto", "Preencha o campo com o valor correto.")
        evento.clean()
        return

        # -------------------------------- MÊS ---------------------------------------#
    elif dataMonth == "__" or int(dataMonth) > 12 or int(dataMonth) == 0:
        response = messagebox.showerror("Mês Incorreto", "Preencha o campo com o valor correto.")
        evento.clean()
        return

    elif dataManipulada(data1_entry.get(), "ano") == dataManipulada(data2_entry.get(), "ano"):
        if int(dataManipulada(data1_entry.get(), "mes")) > int(dataManipulada(data2_entry.get(), "mes")):
            response = messagebox.showerror("Mês Incorreto", "Mês inserido superior ao mês da Data Final")
            evento.clean()
            return

        # -------------------------------- Ano ---------------------------------------#
    elif dataYear == "____" or int(dataYear) > int(data_Current_Year) or int(dataYear) < 2000:
        response = messagebox.showerror("Ano Incorreto", "Preencha o campo com o valor correto.")
        evento.clean()
        return



# Parâmetros da Requisição
frame_requisicao = tk.LabelFrame(root, text="Parâmetros da Requisição", padx=40, pady=15)
frame_requisicao.grid(row=0, column=0, sticky=tk.E+tk.N+tk.S+tk.W, ipadx=5, ipady=5, padx=5, pady=5)
frame_requisicao.grid_columnconfigure(0, weight=1)


# -----------------------------------------------------------------------------------------------------

# Frame para Periodo
numero_protocolo_frame = tk.LabelFrame(frame_requisicao, text="Período Correspondido")
numero_protocolo_frame.grid(row=5, columnspan=2, sticky=tk.E+tk.N+tk.S+tk.W, padx=5, pady=5, ipadx=5, ipady=5)
numero_protocolo_frame.grid_columnconfigure(0, weight=1)
numero_protocolo_frame.grid_columnconfigure(1, weight=1)
numero_protocolo_frame.grid_columnconfigure(2, weight=1)
numero_protocolo_frame.grid_columnconfigure(3, weight=1)
numero_protocolo_frame.grid_columnconfigure(4, weight=1)
numero_protocolo_frame.grid_columnconfigure(5, weight=1)

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

entry_escape = tk.Entry()
entry_escape.grid()

global data2
data2 = 0
definedate2_label = tk.Label(numero_protocolo_frame, text="Até:")
definedate2_label.grid(row=0, column=3, padx=(10,0))

data2_entry = MaskedWidget(numero_protocolo_frame, 'fixed', mask='99/99/9999')
data2_entry.grid(row=0, column=4, padx=(5,0), pady=(5,5))

# BIND FOCUSOUT
data1_entry.bind("<FocusOut>", validate)
data2_entry.bind("<FocusOut>", validate)

# Essa parte não existe mais
today = current_time()
data2_entry.insert(0, today)

# -----------------------------------------------------------------------------------------------------

buscar_paginas = tk.Button(frame_requisicao, text="Buscar Páginas")
buscar_paginas.grid(row=6, column=1, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

# -----------------------------------------------------------------------------------------------------

root.grid_columnconfigure(0, weight=1)

root.mainloop()