import os

contador = 0
for item in os.listdir('.'):
    # .isfile() verifica se o item é um arquivo (e não uma pasta)
    # .endswith() verifica se o texto termina com o que queremos
    if os.path.isfile(item) and item.endswith(".txt"):
        contador = contador + 1

print(f"Foram encontrados {contador} arquivos .txt no diretório.")