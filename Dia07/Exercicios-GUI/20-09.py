import tkinter as tk

def iniciar_desenho(event):
    # Guarda a posição inicial do mouse
    global ultimo_x, ultimo_y
    ultimo_x, ultimo_y = event.x, event.y

def desenhar(event):
    global ultimo_x, ultimo_y
    x, y = event.x, event.y
    # Cria uma linha do ponto anterior até o ponto atual
    canvas.create_line((ultimo_x, ultimo_y, x, y), fill="black", width=3)
    # Atualiza a posição para a próxima chamada
    ultimo_x, ultimo_y = x, y

def limpar_tela():
    canvas.delete("all")

# --- Interface ---
janela = tk.Tk()
janela.title("Exercício 3 - Avançado")

# Canvas onde o desenho acontece
canvas = tk.Canvas(janela, width=600, height=400, bg="white")
canvas.pack(pady=10)

# .bind() associa eventos do mouse a funções
canvas.bind("<Button-1>", iniciar_desenho) # <Button-1> é o clique esquerdo
canvas.bind("<B1-Motion>", desenhar)      # <B1-Motion> é arrastar com o botão esquerdo pressionado

# Botão para limpar
tk.Button(janela, text="Limpar Tela", command=limpar_tela).pack(pady=10)

janela.mainloop()