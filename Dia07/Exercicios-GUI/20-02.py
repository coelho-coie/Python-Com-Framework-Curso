import tkinter as tk

def dar_boas_vindas():
    nome = entry_nome.get()
    label_resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Exercício 2")

tk.Label(janela, text="Qual é o seu nome?").pack(pady=5)
entry_nome = tk.Entry(janela)
entry_nome.pack(pady=5)

tk.Button(janela, text="OK", command=dar_boas_vindas).pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

janela.mainloop()