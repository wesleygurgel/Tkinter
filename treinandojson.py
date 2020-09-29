import tkinter as tk
import json
import configuracoes as configuracoes

root =  tk.Tk()
root.geometry("200x200")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)

label1 = tk.Label(root, text="Cachorro")
label2 = tk.Label(root, text="Gato")
label3 = tk.Label(root, text="Vaca")
label4 = tk.Label(root, text="Leão")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)

entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)
entry4.grid(row=3, column=1, padx=10, pady=10)

salvar = tk.Button(root, text="Salvar")
salvar["command"] = configuracoes.escrever_dados(entry1.get(),entry2.get(),entry3.get(),entry4.get())
salvar.grid(columnspan=2)

root.mainloop()