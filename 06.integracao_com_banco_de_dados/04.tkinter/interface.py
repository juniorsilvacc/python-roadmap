import tkinter as tk
import orm
from tkinter import messagebox

def adicionar_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adicionar_filme(nome, ano, nota)
    messagebox.showinfo("success", "Filme cadastrado com sucesso!")

def atualizar_filme():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.atualizar_filme(id, nome, ano, nota)
    messagebox.showinfo("success", "Filme atualizado com sucesso!")

def excluir_filme():
    id = entry_id.get()
    orm.excluir_filme(id)
    messagebox.showinfo("success", "Filme excluido com sucesso!")

# Interface
root = tk.Tk()
root.title("Gerenciador de Filmes")

label_id = tk.Label(root, text="ID")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=10)

label_nome = tk.Label(root, text="Nome")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_ano = tk.Label(root, text="Ano")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=10)

label_nota = tk.Label(root, text="Nota")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=10)

button_adicionar = tk.Button(root, text="Adicionar", command=adicionar_filme)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar", command=atualizar_filme)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = tk.Button(root, text="Excluir", command=excluir_filme)
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()