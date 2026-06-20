import tkinter as tk

def converter():
    try:
        metros = float(entry_metros.get())
        km = metros / 1000
        label_resultado.config(text=f"{metros} m equivalem a {km} km.")
    except ValueError:
        label_resultado.config(text="Entrada inválida.")

janela = tk.Tk()
janela.title("Exercício 1 - Intermediário")

tk.Label(janela, text="Valor em metros:").pack(pady=5)
entry_metros = tk.Entry(janela)
entry_metros.pack(pady=5)

tk.Button(janela, text="Converter", command=converter).pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

janela.mainloop()