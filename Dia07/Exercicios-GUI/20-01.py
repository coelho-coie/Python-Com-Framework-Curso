import tkinter as tk

def alterar_texto():
    label.config(text="Texto Alterado!")

janela = tk.Tk()
janela.title("Exercício 1")

label = tk.Label(janela, text="Texto Inicial", font=("Arial", 14))
label.pack(pady=20)

botao = tk.Button(janela, text="Clique para Mudar", command=alterar_texto)
botao.pack(pady=10)

janela.mainloop()