class Lampada:
    def __init__(self):
        self.ligada = False

    def clicar_interruptor(self):
        self.ligada = not self.ligada

    def verificar_estado(self):
        if self.ligada:
            print("A lâmpada está acesa.")
        else:
            print("A lâmpada está apagada.")

# Teste
minha_lampada = Lampada()
minha_lampada.clicar_interruptor()
minha_lampada.verificar_estado()