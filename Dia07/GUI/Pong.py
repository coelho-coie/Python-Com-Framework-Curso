import tkinter as tk

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong clássico - Tkinter")
        self.root.resizable(False, False)

        # Configurações da tela
        self.WIDTH = 800
        self.HEIGHT = 500
        self.canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT, bg="black")
        self.canvas.pack()

        # Configurações do jogo
        self.PADDLE_WIDTH = 15
        self.PADDLE_HEIGHT = 90
        self.BALL_SIZE = 15
        self.PADDLE_SPEED = 50

        # Pontuação
        self.score_left = 0
        self.score_right = 0

        # Criar elementos
        self.setup_game()
        
        # Controles
        self.root.bind("<w>", lambda event: self.move_paddle(self.paddle_left, -self.PADDLE_SPEED))
        self.root.bind("<s>", lambda event: self.move_paddle(self.paddle_left, self.PADDLE_SPEED))
        self.root.bind("<Up>", lambda event: self.move_paddle(self.paddle_right, -self.PADDLE_SPEED))
        self.root.bind("<Down>", lambda event: self.move_paddle(self.paddle_right, self.PADDLE_SPEED))

        # Iniciar loop do jogo
        self.update_game()

    def setup_game(self):
        # Linha central
        self.canvas.create_line(self.WIDTH/2, 0, self.WIDTH/2, self.HEIGHT, fill="white", dash=(10, 10))

        # Raquetes
        self.paddle_left = self.canvas.create_rectangle(
            20, self.HEIGHT/2 - self.PADDLE_HEIGHT/2,
            20 + self.PADDLE_WIDTH, self.HEIGHT/2 + self.PADDLE_HEIGHT/2,
            fill="white"
        )
        self.paddle_right = self.canvas.create_rectangle(
            self.WIDTH - 20 - self.PADDLE_WIDTH, self.HEIGHT/2 - self.PADDLE_HEIGHT/2,
            self.WIDTH - 20, self.HEIGHT/2 + self.PADDLE_HEIGHT/2,
            fill="white"
        )

        # Bola
        self.ball = self.canvas.create_oval(
            self.WIDTH/2 - self.BALL_SIZE/2, self.HEIGHT/2 - self.BALL_SIZE/2,
            self.WIDTH/2 + self.BALL_SIZE/2, self.HEIGHT/2 + self.BALL_SIZE/2,
            fill="white"
        )

        # Velocidade inicial da bola (X, Y)
        self.ball_dx = 4
        self.ball_dy = 4

        # Texto de pontuação
        self.score_text = self.canvas.create_text(
            self.WIDTH/2, 30,
            text=f"{self.score_left}   {self.score_right}",
            fill="white", font=("Courier", 30, "bold")
        )

    def move_paddle(self, paddle, dy):
        pos = self.canvas.coords(paddle)
        # Impede a raquete de sair da tela
        if (pos[1] + dy >= 0) and (pos[3] + dy <= self.HEIGHT):
            self.canvas.move(paddle, 0, dy)

    def reset_ball(self):
        # Move a bola de volta para o centro
        self.canvas.coords(
            self.ball,
            self.WIDTH/2 - self.BALL_SIZE/2, self.HEIGHT/2 - self.BALL_SIZE/2,
            self.WIDTH/2 + self.BALL_SIZE/2, self.HEIGHT/2 + self.BALL_SIZE/2
        )
        # Inverte a direção horizontal para quem pontuou e reseta a vertical
        self.ball_dx = -self.ball_dx
        self.ball_dy = 4

    def update_game(self):
        # Mover bola
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)

        # Colisão com o teto ou chão
        if ball_pos[1] <= 0 or ball_pos[3] >= self.HEIGHT:
            self.ball_dy = -self.ball_dy

        # Posição das raquetes para checar colisão
        left_pos = self.canvas.coords(self.paddle_left)
        right_pos = self.canvas.coords(self.paddle_right)

        # Colisão com a raquete esquerda
        if (ball_pos[0] <= left_pos[2] and ball_pos[2] >= left_pos[0] and
            ball_pos[3] >= left_pos[1] and ball_pos[1] <= left_pos[3]):
            self.ball_dx = abs(self.ball_dx) + 0.5 # Aumenta a velocidade levemente para desafiar
            self.ball_dy = self.ball_dy + 0.5 if self.ball_dy > 0 else self.ball_dy - 0.5

        # Colisão com a raquete direita
        if (ball_pos[2] >= right_pos[0] and ball_pos[0] <= right_pos[2] and
            ball_pos[3] >= right_pos[1] and ball_pos[1] <= right_pos[3]):
            self.ball_dx = -abs(self.ball_dx) - 0.5
            self.ball_dy = self.ball_dy + 0.5 if self.ball_dy > 0 else self.ball_dy - 0.5

        # Ponto do jogador da Direita (bola saiu pela esquerda)
        if ball_pos[0] <= 0:
            self.score_right += 1
            self.canvas.itemconfig(self.score_text, text=f"{self.score_left}   {self.score_right}")
            self.reset_ball()

        # Ponto do jogador da Esquerda (bola saiu pela direita)
        if ball_pos[2] >= self.WIDTH:
            self.score_left += 1
            self.canvas.itemconfig(self.score_text, text=f"{self.score_left}   {self.score_right}")
            self.reset_ball()

        # Loop de atualização (~60 frames por segundo)
        self.root.after(16, self.update_game)

# Inicialização do script
if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()