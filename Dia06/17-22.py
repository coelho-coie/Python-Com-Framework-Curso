class Passometro:
    def __init__(self):
        self.passos = 0

    def andar(self):
        self.passos += 1

    def resetar(self):
        self.passos = 0

meu_treino = Passometro()
meu_treino.andar()
meu_treino.andar()
print(f"Passos dados: {meu_treino.passos}")