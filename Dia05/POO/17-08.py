class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        # Podemos realizar cálculos dentro do construtor para gerar novos atributos.
        self.area = base * altura 

ret = Retangulo(10, 5)
print(f"A área calculada no nascimento do objeto foi: {ret.area}")