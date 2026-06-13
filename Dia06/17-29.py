class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.forca = 10
        self.xp = 0

    def ganhar_xp(self, pontos):
        self.xp += pontos
        if self.xp >= 100:
            self.forca += 5
            self.xp = 0
            print(f"{self.nome} subiu de força!")

heroi = Guerreiro("Toledo")
heroi.ganhar_xp(120)
print(f"Força atual: {heroi.forca}")