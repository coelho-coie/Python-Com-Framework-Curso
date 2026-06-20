import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# --- Variáveis Globais ---
caminhos_imagens = []
indice_imagem_atual = 0

# --- Funções ---
def escolher_pasta():
    global caminhos_imagens, indice_imagem_atual
    pasta = filedialog.askdirectory()
    if pasta:
        caminhos_imagens = [os.path.join(pasta, nome) for nome in os.listdir(pasta) 
                            if nome.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if caminhos_imagens:
            indice_imagem_atual = 0
            mostrar_imagem()

def mostrar_imagem():
    caminho = caminhos_imagens[indice_imagem_atual]
    img = Image.open(caminho)
    img.thumbnail((600, 400)) # Redimensiona para caber na tela
    photo = ImageTk.PhotoImage(img)
    label_imagem.config(image=photo)
    label_imagem.image = photo # Mantém uma referência

def proxima_imagem():
    global indice_imagem_atual
    if caminhos_imagens:
        indice_imagem_atual = (indice_imagem_atual + 1) % len(caminhos_imagens)
        mostrar_imagem()

def imagem_anterior():
    global indice_imagem_atual
    if caminhos_imagens:
        indice_imagem_atual = (indice_imagem_atual - 1) % len(caminhos_imagens)
        mostrar_imagem()

# --- Interface ---
janela = tk.Tk()
janela.title("Exercício 2 - Avançado")

# Botão para escolher pasta
tk.Button(janela, text="Escolher Pasta", command=escolher_pasta).pack(pady=10)

# Label para exibir a imagem
label_imagem = tk.Label(janela)
label_imagem.pack(padx=10, pady=10)

# Frame para os botões de navegação
frame_nav = tk.Frame(janela)
frame_nav.pack(pady=10)

tk.Button(frame_nav, text="<< Anterior", command=imagem_anterior).pack(side=tk.LEFT, padx=10)
tk.Button(frame_nav, text="Próximo >>", command=proxima_imagem).pack(side=tk.LEFT, padx=10)

janela.mainloop()