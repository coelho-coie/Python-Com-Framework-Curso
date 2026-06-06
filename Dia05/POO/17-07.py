class Heroi:
    # O __init__ é o CONSTRUTOR. É aqui que fabricamos os atributos (dados).
    def __init__(self, nome, poder):
        self.nome = nome    # Salvando o dado no objeto
        self.poder = poder  # Salvando o dado no objeto
        print(f"Herói {self.nome} criado com o poder de {self.poder}!")

meu_heroi = Heroi("Flash", "Velocidade")