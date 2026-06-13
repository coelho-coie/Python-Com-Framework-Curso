class Elevador:
    def __init__(self, total):
        self.andar_atual = 0
        self.total_andares = total

    def ir_para(self, destino):
        if 0 <= destino <= self.total_andares:
            self.andar_atual = destino
        else:
            print("Andar inexistente.")

predio = Elevador(10)
predio.ir_para(5)
print(f"O elevador está no {predio.andar_atual}º andar.")