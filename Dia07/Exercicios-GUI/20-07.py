import tkinter as tk
from tkinter import filedialog

def abrir_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            area_texto.delete("1.0", tk.END)
            area_texto.insert("1.0", f.read())

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(area_texto.get("1.0", tk.END))

janela = tk.Tk()
janela.title("Exercício 1 - Avançado")

# Área de Texto
area_texto = tk.Text(janela, wrap="word") # wrap="word" quebra a linha por palavra
area_texto.pack(expand=True, fill="both")

# Menu
menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

janela.mainloop()