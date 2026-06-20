import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "aluno" and senha == "python":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

janela = tk.Tk()
janela.title("Exercício 2 - Intermediário")

tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=5, pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.grid(row=1, column=1, padx=5, pady=5)

tk.Button(janela, text="Entrar", command=verificar_login).grid(row=2, column=1, pady=10)

janela.mainloop()