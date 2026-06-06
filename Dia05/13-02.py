# Certifique-se de que o arquivo 'filme_favorito.txt' existe na pasta.
# Se ele não existir, este código dará um erro (FileNotFoundError).
with open("filme_favorito.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n--- Frase do seu filme favorito ---")
    print(conteudo)