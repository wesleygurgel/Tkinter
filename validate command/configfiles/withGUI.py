import tkinter as tk
import os
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk,Image
from datetime import date
from maskedentry import MaskedWidget
from configparser import ConfigParser
from tkinter import filedialog

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
def openfile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Todos os Arquivos", "*.*"), ("PDF Files", "*.pdf"),("JPG Files","*.jpg"), ("PNG Files","*.png")))
    saveasfile_Entry.delete(0, tk.END)
    saveasfile_Entry.insert(0, root.filename)

def switch_button_state():
    if (check2['state'] == tk.NORMAL and saveasfile_Entry['state'] == tk.NORMAL and selectfile_button['state'] == tk.NORMAL):
        check2['state'] = tk.DISABLED
        # saveasfile_Entry.delete(0, tk.END)
        saveasfile_Entry['state'] = tk.DISABLED
        selectfile_button['state'] = tk.DISABLED
        check2.deselect()

    else:
        check2['state'] = tk.NORMAL
        saveasfile_Entry['state'] = tk.NORMAL
        selectfile_button['state'] = tk.NORMAL
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

def juntar_data(dataDesejada):
    # Função para que a data funcione na Máscara aplicada em Período
    dataList = dataDesejada.split("/")
    dataOficial = dataList[0]+dataList[1]+dataList[2]
    return dataOficial

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

def indexdocombobox():
    comboboxatual = str(combobox.current())
    index_trt = {
        "0": "1",
        "1": "3",
        "2": "5",
        "3": "6",
        "4": "7"
    }
    return index_trt.get(comboboxatual)



def salvardados(*args):
    # Requisição
    config['requisicao']['urlEndpoint'] = urlCNJ_entry.get()
    config['requisicao']['tribunal'] = tribunal_entry.get()
    config['requisicao']['passwordTribunal'] = passwordTribunal_entry.get()
    config['requisicao']['numProtocolo'] = numProtocolo_entry.get()
    config['requisicao']['statusLabel'] = combobox.get()
    config['requisicao']['statusIndex'] = str(indexdocombobox())
    dataDe_memoria = juntar_data(data1_entry.get())
    config['requisicao']['data_de'] = dataDe_memoria

    # Aplicação
    config['aplicacao']['savefile'] = str(salvarcomoarquivo.get())
    config['aplicacao']['sobrescrever'] = str(sobrescrever.get())
    config['aplicacao']['salvarbanco'] = str(savedatabase.get())
    if saveasfile_Entry['state'] == tk.NORMAL:
        config['aplicacao']['arquivonome'] = saveasfile_Entry.get()

    with open(file, 'w') as configfile:
        config.write(configfile)


def recuperardados():

    pass
    # # Requisição
    # urlCNJ_entry.insert(0, config['requisicao']['urlEndpoint'])
    # tribunal_entry.insert(0, config['requisicao']['tribunal'])
    # passwordTribunal_entry.insert(0, config['requisicao']['passwordTribunal'])
    # numProtocolo_entry.insert(0, config['requisicao']['numProtocolo'])
    # combobox.insert(0, config['requisicao']['statusLabel'])
    #
    # # Aplicação
    # if config['aplicacao']['savefile'] == 'True':
    #     salvarcomoarquivo.set(1)
    #
    #     check2['state'] = tk.NORMAL
    #     saveasfile_Entry['state'] = tk.NORMAL
    #
    #     saveasfile_Entry.insert(0, config['aplicacao']['arquivonome'])
    #
    #     if config['aplicacao']['sobrescrever'] == 'True':
    #         sobrescrever.set(1)
    # else:
    #     salvarcomoarquivo.set(0)
    #     sobrescrever.set(0)
    #
    #     check2['state'] = tk.DISABLED
    #     saveasfile_Entry['state'] = tk.DISABLED
    #
    # if config['aplicacao']['salvarbanco'] == 'True':
    #     savedatabase.set(1)
    # else:
    #     savedatabase.set(0)



#---------------------------------------------------------------------------------------------

# Parametros de Aplicação
frame_aplicacao = tk.LabelFrame(root, text="Parâmetros de Aplicação", padx=5, pady=5)
frame_aplicacao.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=tk.E+tk.N+tk.W+tk.S)

# CheckBoxes
salvarcomoarquivo = tk.BooleanVar()
sobrescrever = tk.BooleanVar()
savedatabase = tk.BooleanVar()

# FIRST FRAME - PARÂMETRO DE APLICAÇÃO
check1 = tk.Checkbutton(frame_aplicacao, text="Salvar em Arquivo", variable=salvarcomoarquivo, command=switch_button_state)
check1.bind("<Leave>", salvardados)
# print(f'Saveasfile: {salvarcomoarquivo.get()}\nSobrescrever: {sobrescrever.get()}\nSaveDataBase: {savedatabase.get()}')
check1.grid(row=0, sticky=tk.W)

check2 = tk.Checkbutton(frame_aplicacao, text="Sobrescrever conteúdo\n anterior do arquivo", variable=sobrescrever)
check2.bind("<Leave>", salvardados)
check2.grid(row=1, padx=(10,0))

namefile_label = tk.Label(frame_aplicacao, text="Nome arquivo: ")
namefile_label.grid(row=1, column=1, sticky=tk.E)
saveasfile_Entry = tk.Entry(frame_aplicacao, width=30)
saveasfile_Entry.grid(row=1,column=2)

selectfile_button = tk.Button(frame_aplicacao, text="Select a File", relief=tk.RAISED, command=openfile)
selectfile_button.grid(row=1,column=3, padx=15)


check3 = tk.Checkbutton(frame_aplicacao, text="Salvar em Banco de Dados", variable=savedatabase)
check3.bind("<Leave>", salvardados)
# check3.deselect()
check3.grid(row=3, sticky=tk.W)

# -----------------------------------------------------------------------------------------------------


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
# print(f'\nSituação Atual:\nSaveasfile: {salvarcomoarquivo.get()}\nSobrescrever: {sobrescrever.get()}\nSaveDataBase: {savedatabase.get()}')
root.mainloop()