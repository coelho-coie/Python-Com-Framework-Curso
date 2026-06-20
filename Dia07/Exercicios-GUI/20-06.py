import tkinter as tk

def mudar_cor(cor):
    # Apaga todas as luzes
    canvas.itemconfig(luz_vermelha, fill="grey")
    canvas.itemconfig(luz_amarela, fill="grey")
    canvas.itemconfig(luz_verde, fill="grey")
    
    # Acende a luz correta
    if cor == "vermelho":
        canvas.itemconfig(luz_vermelha, fill="red")
    elif cor == "amarelo":
        canvas.itemconfig(luz_amarela, fill="yellow")
    elif cor == "verde":
        canvas.itemconfig(luz_verde, fill="green")

janela = tk.Tk()
janela.title("Exercício 3 - Intermediário")

# Canvas para desenhar
canvas = tk.Canvas(janela, width=100, height=280, bg="black")
canvas.pack(pady=10)

# Cria os círculos (luzes) apagados
luz_vermelha = canvas.create_oval(10, 10, 90, 90, fill="grey")
luz_amarela = canvas.create_oval(10, 100, 90, 180, fill="grey")
luz_verde = canvas.create_oval(10, 190, 90, 270, fill="grey")

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Botões que chamam a função com argumentos diferentes (usando lambda)
tk.Button(frame_botoes, text="Vermelho", command=lambda: mudar_cor("vermelho")).pack(side=tk.LEFT)
tk.Button(frame_botoes, text="Amarelo", command=lambda: mudar_cor("amarelo")).pack(side=tk.LEFT)
tk.Button(frame_botoes, text="Verde", command=lambda: mudar_cor("verde")).pack(side=tk.LEFT)

janela.mainloop()