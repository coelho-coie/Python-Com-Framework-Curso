class Lampada:
    # Todo método dentro de uma classe precisa receber 'self' 
    # como primeiro parâmetro para identificar quem está agindo.
    def avisar(self):
        print("Cuidado, vidro quente!")

minha_lampada = Lampada()
minha_lampada.avisar() # Chamando a ação do objeto