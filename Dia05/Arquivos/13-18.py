import os

# O '.' representa o diretório atual.
conteudo_diretorio = os.listdir('.')

print("--- Conteúdo do Diretório Atual ---")
for item in conteudo_diretorio:
    print(item)