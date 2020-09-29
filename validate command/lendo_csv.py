"""
Lendo Arquivos CSV
"""
# possível de se trabalhar, mas não é ideal

# with open('lutadores.csv', encoding="utf8") as arquivo:
#     dados = arquivo.read()
#     dados = dados.split(',')[2::]
#     print(dados)

# Reader
"""
from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pula o cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede exatos {linha[2]} cm ')
"""

# DictReader
from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo) #Separador diferente era só fazer DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']}, nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}cm")










