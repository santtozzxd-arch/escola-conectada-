import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Label
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
""")
conn.commit()
def adicionar_aluno():
    nome = entry_nome.get().strip() # type: ignore
    idade = entry_idade.get().strip() # type: ignore

    if not nome or not idade:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
        return
cursor.execute("INSERT INTO alunos (nome, idade) VALUES (?, ?)", (nome, idade)) # type: ignore conn.commit()

entry_nome.delete(0, tk.END) # type: ignore
 entry_idade.delete(0, tk.END) # type: ignore
    mostrar_alunos() # type: ignore def mostrar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    listbox_alunos.delete(0, tk.END) # type: ignore
    for aluno in alunos:
        listbox_alunos.insert(tk.END, f"ID: {aluno[0]} - {aluno[1]} ({aluno[2]} anos)") # type: ignore

 root: tk.Tk() # type: ignore
 root.title("App Escola - Cadastro de Alunos") # type: ignore

tk: Label(root, text="Nome:").grid(row=0, column=0, padx=5, pady=5) # type: ignore
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=5, pady=5)
btn_adicionar = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)
istbox_alunos = tk.Listbox(root, width=40)
listbox_alunos.grid(row=3, column=0, columnspan=2, padx=5, pady=5) # pyright: ignore[reportUndefinedVariable]
mostrar_alunos() # pyright: ignore[reportUndefinedVariable]
root.mainloop()
conn.close()
