class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        # Usamos 'self.nome' para buscar o dado que foi guardado no construtor.
        print(f"{self.nome} diz: Au Au!")

dog = Cachorro("Rex")
dog.latir()