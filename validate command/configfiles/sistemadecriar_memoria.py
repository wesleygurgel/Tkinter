"""
def indexdocombobox():
    comboboxatual = str(combobox.current())
    index_trt = {
        "0": "1",
        "1": "3",
        "2": "5",
        "3": "6",
        "4": "7",
        "-1": "1"
    }
    return index_trt.get(comboboxatual)


def salvardados(*args):
    # Requisição
    config['requisicao']['urlEndpoint'] = urlCNJ_entry.get()
    config['requisicao']['tribunal'] = tribunal_entry.get()
    config['requisicao']['passwordTribunal'] = passwordTribunal_entry.get()
    config['requisicao']['numProtocolo'] = numProtocolo_entry.get()
    config['requisicao']['statusLabel'] = combobox.get()
    config['requisicao']['statusIndex'] = indexdocombobox()
    dataDe_memoria = juntar_data(data1_entry.get())
    config['requisicao']['data_de'] = dataDe_memoria

    # Aplicação
    print(f'Salvar como arquivo: {salvarcomoarquivo.get()}')
    config['aplicacao']['savefile'] = str(salvarcomoarquivo.get())
    config['aplicacao']['sobrescrever'] = str(sobrescrever.get())
    config['aplicacao']['salvarbanco'] = str(savedatabase.get())

    if saveasfile_Entry['state'] == tk.NORMAL:
        config['aplicacao']['arquivonome'] = saveasfile_Entry.get()

    with open(file, 'w') as configfile:
        config.write(configfile)


def recuperardados():
    if memoriaOk():
        # Requisição
        urlCNJ_entry.insert(0, config['requisicao']['urlEndpoint'])
        tribunal_entry.insert(0, config['requisicao']['tribunal'])
        passwordTribunal_entry.insert(0, config['requisicao']['passwordTribunal'])
        numProtocolo_entry.insert(0, config['requisicao']['numProtocolo'])
        combobox.insert(0, config['requisicao']['statusLabel'])
        data1_entry.insert(0, config['requisicao']['data_De'])
        print(data1_entry.get())
        today = current_time()
        data2_entry.insert(0, today)

        # Aplicação
        if config['aplicacao']['savefile'] == 'True':
            salvarcomoarquivo.set(1)

            check2['state'] = tk.NORMAL
            saveasfile_Entry['state'] = tk.NORMAL

            saveasfile_Entry.insert(0, config['aplicacao']['arquivonome'])

            if config['aplicacao']['sobrescrever'] == 'True':
                sobrescrever.set(1)
        else:
            salvarcomoarquivo.set(0)
            sobrescrever.set(0)

            check2['state'] = tk.DISABLED
            saveasfile_Entry['state'] = tk.DISABLED

        if config['aplicacao']['salvarbanco'] == 'True':
            savedatabase.set(1)
        else:
            savedatabase.set(0)


def memoriaOk():
    if os.path.exists('memoria.ini'):
        print(config.sections())
        if config.sections() != ['requisicao', 'aplicacao'] and config.sections() != ['requisicao'] and config.sections() != ['aplicacao']:
            # fileErase = open('memoria.ini', 'r+')
            # fileErase.truncate(0)
            # fileErase.close()

            config.add_section('requisicao')
            config.add_section('aplicacao')

            salvarcomoarquivo.set(0)
            sobrescrever.set(0)
            saveasfile_Entry['state'] = tk.DISABLED

            salvardados()
            print('Retornei False')
            return False

        elif config.sections() == ['requisicao', 'aplicacao']:
            print('Retornei True')
            return True

        else:
            f = open("memoria.ini", "r+")
            f.seek(0)
            f.truncate()
            for section in config.sections():
                config.remove_section(section)
            recuperardados()

    else:
        open('memoria.ini', 'w+')
        recuperardados()
"""