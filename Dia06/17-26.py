class Carro:
    def __init__(self, litros):
        self.gasolina = litros
    
    def derigir(self, km):
        consumo = km * 2
        if self.gasolina >= consumo:
            self.gasolina -= consumo
        else:
            print("Gasolina insuficiente.")

meu_carro = Carro(50)
meu_carro.dirigir(10)
print(f"Restam {meu_carro.gasolina} litros.")