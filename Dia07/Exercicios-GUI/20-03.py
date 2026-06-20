import tkinter as tk

contador = 0

def incrementar():
    global contador
    contador += 1
    label_contador.config(text=str(contador))

janela = tk.Tk()
janela.title("Exercício 3")

label_contador = tk.Label(janela, text=str(contador), font=("Helvetica", 24))
label_contador.pack(pady=20)

botao = tk.Button(janela, text="Clique em Mim!", command=incrementar)
botao.pack(pady=10)

janela.mainloop()