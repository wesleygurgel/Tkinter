import os
from csv import DictWriter
import treinandojson as valores

def escrever_dados(entry1,entry2,entry3,entry4):
    with open('memoria.csv', 'w', encoding="utf8", newline="") as arquivo:
        if os.path.exists('./memoria.csv'):
            pass
        else:
            cabecalho = ['Cachorro', 'Gato', 'Vaca', 'Leão']
            escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
            escritor_csv.writeheader()

        cachorro = entry1
        gato = entry2
        vaca = entry3
        leao = entry4

        escritor_csv.writerow({'Cachorro': cachorro, 'Gato': gato, 'Vaca': vaca, 'Leão':leao})