
dataInicial = "10/12/2012"
dataFinal = "28/09/2020"

dataInicial_split1 = dataInicial.split("/")
print(dataInicial_split1)

dataInicial_day = dataInicial_split1[0]
dataInicial_month = dataInicial_split1[1]
dataInicial_year = dataInicial_split1[2]

print(f'Dia {dataInicial_day} do mês {dataInicial_month} no ano de {dataInicial_year}')