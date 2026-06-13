class Bicicleta:
    def __init__(self):
        self.velocidade = 0

    def pedalar(self):
        self.velocidade += 5

    def frear(self):
        self.velocidade -= 5
        if self.velocidade < 0:
            self.velocidade = 0

bike = Bicicleta()
bike.pedalar()
bike.frear()
print(f"Velocidade atual: {bike.velocidade} km/h")