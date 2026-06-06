compras_carregadas = []

with open("compras.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # Usamos .strip() para remover o '\n' do final de cada linha.
        compras_carregadas.append(linha.strip())
    
print("Lista de compras carregada do arquivo:")
print(compras_carregadas)