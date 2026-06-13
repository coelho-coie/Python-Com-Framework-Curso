class Garrafa:
    def __init__(self):
        self.conteudo_ml = 500

    def beber(self):
        self.conteudo_ml -= 100

    def encher(self):
        self.conteudo_ml = 500

g = Garrafa()
g.beber()
print(f"Volume: {g.conteudo_ml}ml")