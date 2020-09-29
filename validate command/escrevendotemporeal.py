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


root = tk.Tk()
root.title("Protocolos CNJ")
#root.iconbitmap('imagens/icon.ico')
#root.geometry("400x400")


#---------------------------------------------------------------------------------------------

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

    today = today_day+today_month+today_year
    return today

# Funções do DATE
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


def salvardados():
    with open('memoria.csv', 'w', encoding="utf8", newline="") as arquivo:
        cabecalho = ['URL CNJ', 'Tribunal', 'PasswordTribunal', 'NumProtocolo', 'Status']
        escritor_csv = DictWriter(arquivo, cabecalho)
        escritor_csv.writeheader()

        urlcnj = urlCNJ_entry.get()
        tribunal = tribunal_entry.get()
        senhatribunal = passwordTribunal_entry.get()
        numprotocolo = numProtocolo_entry.get()
        status = combobox.get()

        if data1_entry.get() != "":
            dataDE = data1_entry.get()
        else:
            dataDE = ""

        combobox.delete(0, tk.END)
        escritor_csv.writerow({'URL CNJ': urlcnj, 'Tribunal': tribunal, 'PasswordTribunal': senhatribunal, 'NumProtocolo': numprotocolo, 'Status': status})


def recuperardados():
    with open('./memoria.csv', encoding="utf8") as arquivo:
        leitor_csv = DictReader(arquivo)
        for linha in leitor_csv:
            urlCNJ_entry.insert(0, linha['URL CNJ'])
            tribunal_entry.insert(0, linha['Tribunal'])
            passwordTribunal_entry.insert(0, linha['PasswordTribunal'])
            numProtocolo_entry.insert(0, linha['NumProtocolo'])
            combobox.insert(0, linha['Status'])


def executar():
    while progressBar['value'] < 100:
        progressBar['value'] += 25
        root.update_idletasks()
        time.sleep(1)

    paginas_processadas_entry.insert(0, "1762")
    paginas_erro_entry.insert(0, "300")
    salvardados()


#---------------------------------------------------------------------------------------------

# Parametros de Aplicação
frame_aplicacao = tk.LabelFrame(root, text="Parâmetros de Aplicação", padx=5, pady=5)
frame_aplicacao.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=tk.E+tk.N+tk.W+tk.S)

# CheckBoxes
saveasfile = tk.StringVar()
sobrescrever = tk.StringVar()
savedatabase = tk.StringVar()

# FIRST FRAME - PARÂMETRO DE APLICAÇÃO
check1 = tk.Checkbutton(frame_aplicacao, text="Salvar em Arquivo", variable=saveasfile, command=switch_button_state)
check1.deselect()
check1.grid(row=0, sticky=tk.W)

check2 = tk.Checkbutton(frame_aplicacao, text="Sobrescrever conteúdo\n anterior do arquivo", variable=sobrescrever, state=tk.DISABLED)
check2.deselect()
check2.grid(row=1, padx=(10,0))

namefile_label = tk.Label(frame_aplicacao, text="Nome arquivo: ")
namefile_label.grid(row=1, column=1, sticky=tk.E)
saveasfile_Entry = tk.Entry(frame_aplicacao, width=30, state=tk.DISABLED)
saveasfile_Entry.grid(row=1,column=2)

selectfile_button = tk.Button(frame_aplicacao, text="Select a File", relief=tk.RAISED, state=tk.DISABLED, command=openfile)
selectfile_button.grid(row=1,column=3, padx=15)


check3 = tk.Checkbutton(frame_aplicacao, text="Salvar em Banco de Dados", variable=savedatabase)
check3.deselect()
check3.grid(row=3, sticky=tk.W)



#aaaa
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
urlCNJ_entry.grid(row=0,column=1)
tribunal_entry = tk.Entry(frame_requisicao, width = 40)
tribunal_entry.grid(row=1,column=1)
passwordTribunal_entry = tk.Entry(frame_requisicao, show="*" ,width = 40)
passwordTribunal_entry.grid(row=2,column=1)
numProtocolo_entry = tk.Entry(frame_requisicao, width = 40)
numProtocolo_entry.grid(row=3,column=1)

# -----------------------------------------------------------------------------------------------------

# Frame para Periodo
numero_protocolo_frame = tk.LabelFrame(frame_requisicao, text="Período Correspondido")
numero_protocolo_frame.grid(row=5, columnspan=2, sticky=tk.E+tk.N+tk.S+tk.W, padx=5, pady=5, ipadx=5, ipady=5)

# Buttons Calendar
calendarImage = ImageTk.PhotoImage(Image.open("calendar1.png").resize((20,20), Image.ANTIALIAS))

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

# Status Combobox

status_label = tk.Label(frame_requisicao, text="Status:").grid(row=4, sticky=tk.E, pady=(0,5))
combobox = ttk.Combobox(frame_requisicao, values=[
                                "Aguardando Processamento",
                                "Processado com Sucesso",
                                "Duplicado",
                                "Processado com Erro",
                                "Erro no arquivo"],
                                postcommand=change_status, width=25)
combobox.grid(row=4, column=1)
# -----------------------------------------------------------------------------------------------------

# Buttons
limpar_campos = tk.Button(frame_requisicao, text="Limpar", command=clear_all_requisicao)
limpar_campos.grid(row=6, column=0, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

buscar_paginas = tk.Button(frame_requisicao, text="Buscar Páginas")
buscar_paginas.grid(row=6, column=1, sticky=tk.E+tk.N+tk.S+tk.W, pady=(5,0))

# -----------------------------------------------------------------------------------------------------

# FRAME Resultados
frm_result = tk.LabelFrame(root, text='Resultados', pady=5)
frm_result.grid(row=1, column=0, padx = 10, pady = 5, sticky=tk.E + tk.N + tk.S + tk.W)

# Labels - Resultados
total_paginas_label = tk.Label(frm_result, text="Total de Páginas: ")
total_paginas_label.grid(padx=(30,0), pady=(0,5), sticky=tk.E)
protocolos_por_paginas_label = tk.Label(frm_result, text="Protocolos por Página: ")
protocolos_por_paginas_label.grid(padx=(30,0), pady=(0,5), sticky=tk.E)
total_protocolos_label = tk.Label(frm_result, text="Total de Protocolos: ")
total_protocolos_label.grid(padx=(30,0), pady=(0,5), sticky=tk.E)

# Entrys - Resultados
total_paginas_entry = tk.Entry(frm_result, width=40)
total_paginas_entry.grid(row=0, column=1, sticky=tk.W)
protocolos_por_paginas_entry = tk.Entry(frm_result, width=40)
protocolos_por_paginas_entry.grid(row=1, column=1, sticky=tk.W)
total_protocolos_entry = tk.Entry(frm_result, width=40)
total_protocolos_entry.grid(row=2, column=1, sticky=tk.W)

# -----------------------------------------------------------------------------------------------------

# FRAME Resumos Painel de Progresso

# Definindo Frame para tela
frame_progresspanel = tk.LabelFrame(root, text="Painel de Progresso", pady=5)
frame_progresspanel.grid(row=1, column=1, sticky=tk.E + tk.N + tk.S + tk.W, padx = 10, pady = 5)

# Labels - Painel de Progresso
paginas_processadas_label = tk.Label(frame_progresspanel, text="Quantidade de Páginas Processadas: ")
paginas_processadas_label.grid(padx=(10,0), pady=(0,5), sticky=tk.E)
paginas_erro_label = tk.Label(frame_progresspanel, text="Quantidade de Páginas com Erro: ")
paginas_erro_label.grid(padx=(10,0), pady=(0,5), sticky=tk.E)

# Entrys - Painel de Progresso
paginas_processadas_entry = tk.Entry(frame_progresspanel, width=40)
paginas_processadas_entry.grid(row=0, column=1, sticky=tk.W)
paginas_erro_entry = tk.Entry(frame_progresspanel, width=40)
paginas_erro_entry.grid(row=1, column=1, sticky=tk.W)

# ProgressBar
progressBar = ttk.Progressbar(frame_progresspanel, orient=tk.HORIZONTAL, length=450, mode='determinate')
progressBar.grid(row=2, columnspan=2,pady=20, padx=20)

# -----------------------------------------------------------------------------------------------------

# Botão Executar
execute_button = tk.Button(root, text="Executar", relief = tk.GROOVE, command=executar)
execute_button.grid(columnspan=2, sticky=tk.E+tk.N+tk.S+tk.W, padx=5, pady=5)

# -----------------------------------------------------------------------------------------------------

recuperardados()
root.mainloop()



# a partir daqui ta o inicio de tudo
