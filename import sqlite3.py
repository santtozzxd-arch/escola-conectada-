import sqlite3
import tkinter as tk
from tkinter import messagebox  
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')
conn.commit()
def adicionar_aluno():
    nome = entry_nome.get() # pyright: ignore[reportUndefinedVariable]
    idade = entry_idade.get() # pyright: ignore[reportUndefinedVariable]

    if not nome or not idade:
        messagebox.showwarning("Erro", "Preencha nome e idade")
        return
    try:
        idade = int(idade)
    except ValueError:
        messagebox.showwarning("Erro", "Idade deve ser um número")
        return

    cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()
    messagebox.showinfo("Sucesso", f"Aluno {nome} adicionado!")
    entry_nome.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_idade.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
mostrar_alunos() # pyright: ignore[reportUndefinedVariable]
def mostrar_alunos():
    cursor.execute('SELECT id, nome, idade FROM alunos')
    alunos = cursor.fetchall()

    listbox_alunos.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    for aluno in alunos:
        # listbox_alunos.insert (tk.END) f"ID: {aluno[0]} - {aluno[1]} ({aluno[2]} anos)" # pyright: ignore[reportUndefinedVariab1