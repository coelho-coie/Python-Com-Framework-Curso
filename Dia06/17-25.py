class Termostato:
    def __init__(self):
        self.temperatura = 20
        self.alerta = ""

    def ajustar(self, valor):
        if 15 <= valor <= 30:
            self.temperatura = valor
            self.alerta = "Temperatura Ideal"
        else:
            self.alerta = "Temperatura fora do limite permitido."

ar = Termostato()
ar.ajustar(25)
ar.ajustar(50)
