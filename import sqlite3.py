import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import datetime
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS problemas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        lugar TEXT NOT NULL,
        descricao TEXT NOT NULL,
        FOREIGN KEY(aluno_id) REFERENCES alunos(id)
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS jornal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        conteudo TEXT NOT NULL,
        data TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS avisos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT NOT NULL,
        data TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS calendario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evento TEXT NOT NULL,
        data TEXT NOT NULL,
        descricao TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS horarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dia_semana TEXT NOT NULL,
        horario TEXT NOT NULL,
        materia TEXT NOT NULL,
        professor TEXT
    )
""")
conn.commit()
def validar_email(email):
    return email.endswith("@gmail.com")

def adicionar_aluno():
    nome = entry_nome.get().strip() # pyright: ignore[reportUndefinedVariable]
    idade = entry_idade.get().strip() # pyright: ignore[reportUndefinedVariable]
    email = entry_email.get().strip() # pyright: ignore[reportUndefinedVariable]

    if not nome or not idade or not email:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    try:
        idade_int = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser número inteiro.")
        return
    if not validar_email(email):
        messagebox.showerror("Erro", "Email deve ser @gmail.com")
        return
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", (nome, idade_int, email)) # pyright: ignore[reportUndefinedVariable]
conn.commit()

entry_nome.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
entry_idade.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
entry_email.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
mostrar_alunos() # pyright: ignore[reportUndefinedVariable]
def mostrar_alunos():
    listbox_alunos.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for a in alunos:
        listbox_alunos.insert(tk.END, f"ID: {a[0]} - {a[1]} ({a[2]} anos) - {a[3]}") # pyright: ignore[reportUndefinedVariable]
        def relatar_problema():
            aluno_id = entry_problema_aluno_id.get().strip() # pyright: ignore[reportUndefinedVariable]
    lugar = entry_lugar.get().strip() # pyright: ignore[reportUndefinedVariable]
    descricao = text_descricao.get("1.0", tk.END).strip() # pyright: ignore[reportUndefinedVariable]
    if not aluno_id or not lugar or not descricao: # pyright: ignore[reportUndefinedVariable]
        messagebox.showwarning("Atenção", "Preencha todos os campos do problema.")
        return
    try:
        aluno_id_int = int(aluno_id) # pyright: ignore[reportUndefinedVariable]
    except ValueError:
        messagebox.showerror("Erro", "ID do aluno deve ser número inteiro.")
        return
    cursor.execute("SELECT id FROM alunos WHERE id = ?", (aluno_id_int,))
    if cursor.fetchone() is None:
        messagebox.showerror("Erro", "Aluno não encontrado.")
        return
    cursor.execute("INSERT INTO problemas (aluno_id, lugar, descricao) VALUES (?, ?, ?)",
                   (aluno_id_int, lugar, descricao))
    conn.commit()

    entry_problema_aluno_id.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_lugar.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    text_descricao.delete("1.0", tk.END) # pyright: ignore[reportUndefinedVariable]

    messagebox.showinfo("Sucesso", "Problema relatado com sucesso.")
    def mostrar_jornal():
        listbox_jornal.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    cursor.execute("SELECT titulo, data FROM jornal ORDER BY data DESC")
    posts = cursor.fetchall()
    for p in posts:
        listbox_jornal.insert(tk.END, f"{p[1]} - {p[0]}") # pyright: ignore[reportUndefinedVariable]
        def adicionar_post_jornal():
            titulo = entry_titulo_jornal.get().strip() # pyright: ignore[reportUndefinedVariable]
    conteudo = text_conteudo_jornal.get("1.0", tk.END).strip() # pyright: ignore[reportUndefinedVariable]
    if not titulo or not conteudo: # pyright: ignore[reportUndefinedVariable]
        messagebox.showwarning("Atenção", "Preencha título e conteúdo.")
        return
    data_hoje = datetime.date.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO jornal (titulo, conteudo, data) VALUES (?, ?, ?)",
                   (titulo, conteudo, data_hoje)) # pyright: ignore[reportUndefinedVariable]
    conn.commit()
    entry_titulo_jornal.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    text_conteudo_jornal.delete("1.0", tk.END) # pyright: ignore[reportUndefinedVariable]
    mostrar_jornal()
    messagebox.showinfo("Sucesso", "Post adicionado ao jornal.")
    def mostrar_avisos():
        listbox_avisos.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    cursor.execute("SELECT texto, data FROM avisos ORDER BY data DESC")
    avisos = cursor.fetchall()
    for a in avisos:
        listbox_avisos.insert(tk.END, f"{a[1]} - {a[0]}") # pyright: ignore[reportUndefinedVariable]
        
def adicionar_aviso():
    texto = entry_texto_aviso.get().strip() # pyright: ignore[reportUndefinedVariable]
    if not texto:
        messagebox.showwarning("Atenção", "Digite o texto do aviso.")
        return
    data_hoje = datetime.date.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO avisos (texto, data) VALUES (?, ?)", (texto, data_hoje))
    conn.commit()
    entry_texto_aviso.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    mostrar_avisos() # pyright: ignore[reportUndefinedVariable]
    messagebox.showinfo("Sucesso", "Aviso adicionado.")
    def mostrar_calendario():
        listbox_calendario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    cursor.execute("SELECT evento, data, descricao FROM calendario ORDER BY data")
    eventos = cursor.fetchall()
    for e in eventos:
        desc = e[2] if e[2] else ""
        listbox_calendario.insert(tk.END, f"{e[1]} - {e[0]}: {desc}") # pyright: ignore[reportUndefinedVariable]
def adicionar_evento_calendario():
    evento = entry_evento_calendario.get().strip() # pyright: ignore[reportUndefinedVariable]
    data_evento = entry_data_calendario.get().strip() # pyright: ignore[reportUndefinedVariable]
    descricao = text_descricao_calendario.get("1.0", tk.END).strip() # pyright: ignore[reportUndefinedVariable]
    if not evento or not data_evento:
        messagebox.showwarning("Atenção", "Preencha evento e data.")
        return
    try:
        datetime.datetime.strptime(data_evento, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Erro", "Data deve estar no formato YYYY-MM-DD.")
        return
    cursor.execute("INSERT INTO calendario (evento, data, descricao) VALUES (?, ?, ?)",
                   (evento, data_evento, descricao))
    conn.commit()
    entry_evento_calendario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_data_calendario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    text_descricao_calendario.delete("1.0", tk.END) # pyright: ignore[reportUndefinedVariable]
    mostrar_calendario() # pyright: ignore[reportUndefinedVariable]
    messagebox.showinfo("Sucesso", "Evento adicionado ao calendário.")
    cursor.execute("INSERT INTO calendario (evento, data, descricao) VALUES (?, ?, ?)",
                   (evento, data_evento, descricao))
    conn.commit()
    entry_evento_calendario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_data_calendario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    text_descricao_calendario.delete("1.0", tk.END) # pyright: ignore[reportUndefinedVariable]
    mostrar_calendario() # pyright: ignore[reportUndefinedVariable]
    messagebox.showinfo("Sucesso", "Evento adicionado ao calendário.")
def mostrar_horarios():
    listbox_horarios.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    ordem_dias = {"Segunda":1, "Terça":2, "Quarta":3, "Quinta":4, "Sexta":5, "Sábado":6, "Domingo":7}
    cursor.execute("SELECT dia_semana, horario, materia, professor FROM horarios")
    horarios = cursor.fetchall()
    horarios.sort(key=lambda x: (ordem_dias.get(x[0], 99), x[1]))
    for h in horarios:
        prof = f" - Prof: {h[3]}" if h[3] else ""
        listbox_horarios.insert(tk.END, f"{h[0]} {h[1]}: {h[2]}{prof}") # pyright: ignore[reportUndefinedVariable]
def adicionar_horario():
    dia = combo_dia.get() # pyright: ignore[reportUndefinedVariable]
    horario = entry_horario.get().strip() # pyright: ignore[reportUndefinedVariable]
    materia = entry_materia.get().strip() # pyright: ignore[reportUndefinedVariable]
    professor = entry_professor.get().strip() # pyright: ignore[reportUndefinedVariable]

    if not dia or not horario or not materia:
        messagebox.showwarning("Atenção", "Preencha dia, horário e matéria.")
        return
    cursor.execute("INSERT INTO horarios (dia_semana, horario, materia, professor) VALUES (?, ?, ?, ?)",
                   (dia, horario, materia, professor))
    conn.commit()
    entry_horario.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_materia.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    entry_professor.delete(0, tk.END) # pyright: ignore[reportUndefinedVariable]
    mostrar_horarios()
    messagebox.showinfo("Sucesso", "Horário adicionado.")

    root = tk.Tk()
root.title("App Escola Completo") # pyright: ignore[reportUndefinedVariable]
root.geometry("750x650") # pyright: ignore[reportUndefinedVariable]
notebook = ttk.Notebook(root) # pyright: ignore[reportUndefinedVariable]
notebook.pack(expand=1, fill="both")
frame_cadastro = ttk.Frame(notebook)
notebook.add(frame_cadastro, text="Cadastro Alunos")

ttk.Label(frame_cadastro)
