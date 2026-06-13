class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def fechar_conta(self):
        total = 0
        for p in self.itens:
            total += p.preco
        return total

p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 150)
meu_carrinho = Carrinho()
meu_carrinho.adicionar(p1)
meu_carrinho.adicionar(p2)
print(f"Total: R${meu_carrinho.fechar_conta()}")