class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50

    def alimentar(self):
        self.fome -= 10

    def brincar(self):
        self.fome += 15

meu_pet = Pet("Rex")
meu_pet.alimentar()
print(f"Fome do {meu_pet.nome}: {meu_pet.fome}")