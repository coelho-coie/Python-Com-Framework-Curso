lista_de_compras = ["Maçã", "Arroz", "Feijão", "Chocolate", "Café"]

with open("compras.txt", "w", encoding="utf-8") as arquivo:
    for item in lista_de_compras:
        arquivo.write(item + "\n")

print("Lista de compras salva com sucesso em 'compras.txt'.")