import tkinter as tk
from tkinter import ttk
import random
import string

def gerar_senha():
    try:
        comprimento = int(combo_comprimento.get())
    except ValueError:
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, "Comprimento inválido")
        return

    caracteres = ""
    if var_maiusculas.get() == 1:
        caracteres += string.ascii_uppercase
    if var_minusculas.get() == 1:
        caracteres += string.ascii_lowercase
    if var_numeros.get() == 1:
        caracteres += string.digits
    if var_simbolos.get() == 1:
        caracteres += string.punctuation
    
    if not caracteres:
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, "Selecione uma opção")
        return
        
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    
    entry_senha.delete(0, tk.END) # Limpa o campo
    entry_senha.insert(0, senha) # Insere a nova senha

# --- Configuração da Janela ---
janela = tk.Tk()
janela.title("Gerador de Senhas")

# --- Frame para as opções ---
frame_opcoes = tk.Frame(janela, padx=10, pady=10)
frame_opcoes.pack()

# --- Widgets ---
tk.Label(frame_opcoes, text="Comprimento:").grid(row=0, column=0, sticky='w')
combo_comprimento = ttk.Combobox(frame_opcoes, values=[i for i in range(8, 25)])
combo_comprimento.set(12)
combo_comprimento.grid(row=0, column=1, sticky='w')

# Checkbuttons usam variáveis especiais do Tkinter
var_maiusculas = tk.IntVar(value=1)
tk.Checkbutton(frame_opcoes, text="Letras Maiúsculas", variable=var_maiusculas).grid(row=1, column=0, columnspan=2, sticky='w')

var_minusculas = tk.IntVar(value=1)
tk.Checkbutton(frame_opcoes, text="Letras Minúsculas", variable=var_minusculas).grid(row=2, column=0, columnspan=2, sticky='w')

var_numeros = tk.IntVar(value=1)
tk.Checkbutton(frame_opcoes, text="Números", variable=var_numeros).grid(row=3, column=0, columnspan=2, sticky='w')

var_simbolos = tk.IntVar()
tk.Checkbutton(frame_opcoes, text="Símbolos", variable=var_simbolos).grid(row=4, column=0, columnspan=2, sticky='w')

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=5)

entry_senha = tk.Entry(janela, width=30, font=("Courier", 12))
entry_senha.pack(padx=10, pady=10)

# --- Inicia a Janela ---
janela.mainloop()