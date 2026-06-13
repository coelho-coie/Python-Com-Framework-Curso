"""
Arquivo para criação de objetos times (esporte)
que podem ser de vários tipos, como futebol, vôlei,
basquete etc.
"""

class Clube:
    """
    Classe que herda dados de clubes de esportes de varios estilos
    """
    # Atributos - características do objeto
    def __init__(self):
        self.nome = "Flamengo"
        self.fundacao = "1911"
        self.cor_uniforme = "Vermelho"
        self.mascote = "Urubu"
        self.modalidade = "Natação"
        self.campeonatos = 6
        self.vitorias = 0
        self.derrotas = 0 

    # Métodos - ações do objeto
    def ganhar(self):
        self.vitorias += 1

    def jogar(self):
        pass

    def perder(self):
        self.perder += 1

    def trocar_uniforme(self):
        pass

# Time 1: Futebol
time1 = Clube(
    nome="Flamengo", 
    fundacao="1895", 
    cor_uniforme="Rubro-Negro", 
    mascote="Urubu", 
    modalidade="Futebol", 
    campeonatos=8
)

# Time 2: Basquete
time2 = Clube(
    nome="Los Angeles Lakers", 
    fundacao="1947", 
    cor_uniforme="Roxo e Ouro", 
    mascote="Não possui", 
    modalidade="Basquete", 
    campeonatos=17
)

# Time 3: Vôlei Nacional
time3 = Clube(
    nome="Sada Cruzeiro", 
    fundacao="2006", 
    cor_uniforme="Azul e Branco", 
    mascote="Raposa", 
    modalidade="Vôlei", 
    campeonatos=8
)

# Time 4: Futebol Americano
time4 = Clube(
    nome="Kansas City Chiefs", 
    fundacao="1960", 
    cor_uniforme="Vermelho e Branco", 
    mascote="K. C. Wolf", 
    modalidade="Futebol Americano", 
    campeonatos=4
)

time1.jogar()
time2.jogar()
time1.ganhar()
time2.perder()
