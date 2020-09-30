import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk,Image
from datetime import date
from maskedentry import MaskedWidget
from configparser import ConfigParser

root = tk.Tk()
root.title("Protocolos CNJ")

# Abrindo Arquivo de Configuração
file = 'memoria.ini'
config = ConfigParser()
config.read(file)

listaCombobox=[ "Aguardando Processamento",
                "Processado com Sucesso",
                "Duplicado",
                "Processado com Erro",
                "Erro no arquivo"]

# Funções
# Dia atual função
def current_time():
    todaystring = str(date.today())

    todaysplit = todaystring.split("-")
    today_day = todaysplit[2]
    today_month = todaysplit[1]
    today_year = todaysplit[0]

    # Parte usada para o Calendário em Período - Auxilia na parte de transformar o ano em 4 CARACTERES. Ex.:"2020"
    global year_calendario
    year_calendario = today_year
    list(year_calendario)
    year_calendario = year_calendario[2] + year_calendario[3]
    year_calendario = int(year_calendario)

    today = today_day + today_month + today_year
    return today


# Funções do DATE
def data_inicio():
    data1 = 1
    data2 = 0
    open_window_date(data1, data2)


def data_final():
    data2 = 1
    data1 = 0
    open_window_date(data1, data2)


def open_window_date(data1, data2):
    global top
    top = tk.Toplevel()
    top.title("Defina a Data")
    top.geometry("400x300")
    global cal
    cal = Calendar(top, selectmode="day", year=2020, month=6, day=27, locale='pt_BR')
    cal.pack(pady=20, fill="both", expand=True)
    submitedate = tk.Button(top, text="Selecionar Data", command=lambda: grab_date(data1, data2)).pack(pady=(0, 10))


def grab_date(data1, data2):
    datastring = cal.get_date()
    dataList = datastring.split("/")
    dataOficial = dataList[0] + dataList[1] + dataList[2]

    if data1 == 1:
        data1_entry.insert(0, dataOficial)
    if data2 == 1:
        data2_entry.insert(0, dataOficial)

    top.destroy()


def change_status():
    combobox["values"] = ["Aguardando Processamento",
                          "Processado com Sucesso",
                          "Duplicado",
                          "Processado com Erro",
                          "Erro no arquivo"
                          ]


def clear_all_requisicao():
    urlCNJ_entry.delete(0, tk.END)
    tribunal_entry.delete(0, tk.END)
    passwordTribunal_entry.delete(0, tk.END)
    numProtocolo_entry.delete(0, tk.END)
    combobox.current(0)


def salvardados(*args):
    config['aplicacao']['urlEndpoint'] = urlCNJ_entry.get()
    config['aplicacao']['tribunal'] = tribunal_entry.get()
    config['aplicacao']['passwordTribunal'] = passwordTribunal_entry.get()
    config['aplicacao']['numProtocolo'] = numProtocolo_entry.get()
    config['aplicacao']['statusLabel'] = combobox.get()
    config['aplicacao']['statusIndex'] = str(combobox.current())

    with open(file, 'w') as configfile:
        config.write(configfile)


def recuperardados():
    urlCNJ_entry.insert(0, config['aplicacao']['urlEndpoint'])
    tribunal_entry.insert(0, config['aplicacao']['tribunal'])
    passwordTribunal_entry.insert(0, config['aplicacao']['passwordTribunal'])
    numProtocolo_entry.insert(0, config['aplicacao']['numProtocolo'])
    combobox.insert(0, config['aplicacao']['statusLabel'])


# Parâmetros da Requisição
frame_requisicao = tk.LabelFrame(root, text="Parâmetros da Requisição", padx=40, pady=15)
frame_requisicao.grid(row=0, column=0, sticky=tk.E+tk.N+tk.S+tk.W, ipadx=5, ipady=5, padx=5, pady=5)

# Labels
urlCNJ_label = tk.Label(frame_requisicao, text="URL endpoint CNJ:").grid(row=0,sticky=tk.E, pady=(0,5))
tribunal_label = tk.Label(frame_requisicao, text="Tribunal:").grid(row=1, sticky=tk.E, pady=(0,5))
passwordTribunal_label = tk.Label(frame_requisicao, text="Senha do Tribunal:").grid(row=2, sticky=tk.E, pady=(0,5))
numProtocolo_label = tk.Label(frame_requisicao, text="Nº Protocolo:").grid(row=3, sticky=tk.E, pady=(0,5))

# Entrys
urlCNJ_entry = tk.Entry(frame_requisicao, width = 40)
urlCNJ_entry.bind("<FocusOut>", salvardados)
urlCNJ_entry.grid(row=0,column=1)

tribunal_entry = tk.Entry(frame_requisicao, width = 40)
tribunal_entry.bind("<FocusOut>", salvardados)
tribunal_entry.grid(row=1,column=1)

passwordTribunal_entry = tk.Entry(frame_requisicao, show="*" ,width = 40)
passwordTribunal_entry.bind("<FocusOut>", salvardados)
passwordTribunal_entry.grid(row=2,column=1)

numProtocolo_entry = tk.Entry(frame_requisicao, width = 40)
numProtocolo_entry.bind("<FocusOut>", salvardados)
numProtocolo_entry.grid(row=3,column=1)

# -----------------------------------------------------------------------------------------------------

# Status Combobox

status_label = tk.Label(frame_requisicao, text="Status:").grid(row=4, sticky=tk.E, pady=(0,5))
combobox = ttk.Combobox(frame_requisicao, values = listaCombobox, postcommand=change_status, width=25)
combobox.bind("<FocusOut>", salvardados)
combobox.grid(row=4, column=1)

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
today = current_time()
data2_entry.insert(0, today)

# -----------------------------------------------------------------------------------------------------

# Buttons
limpar_campos = tk.Button(frame_requisicao, text="Limpar", command=clear_all_requisicao)
limpar_campos.grid(row=6, column=0, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

buscar_paginas = tk.Button(frame_requisicao, text="Buscar Páginas")
buscar_paginas.grid(row=6, column=1, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

recuperardados()
root.mainloop()