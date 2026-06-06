class Pokemon:
    def __init__(self, nome, tipo, ataque, defesa, agilidade):
       self.nome = nome
       self.tipo = tipo
       self.ataque = ataque
       self.defesa = defesa
       self.agilidade = agilidade

player1 = Pokemon("Pikachu", "Elétrico", 55, 50, 90)
player2 = Pokemon("Mewtwon", "Psiquico", 900, 900, 600)