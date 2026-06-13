class Lampada:
    def __init__(self, comodo):
        self.comodo = comodo
        self.acesa = True
    
    def apagar(self):
        self.acesa = False

class Casa:
    def __init__(self):
        self.dispositivos = []

    def adicionar_lampada(self, lamp):
        self.dispositivos.append(lamp)

    def desligar_tudo(self):
        for l in self.dispositivos:
            l.apagar()

sala = Lampada("Sala")
quarto = Lampada("Quarto")
minha_casa = Casa()
minha_casa.adicionar_lampada(sala)
minha_casa.adicionar_lampada(quarto)
minha_casa.desligar_tudo()