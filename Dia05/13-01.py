frase_filme = input("Digite uma frase do seu filme favorito: ")

# O modo 'w' cria o arquivo se ele não existir, ou apaga o conteúdo se já existir.
with open("filme_favorito.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase_filme)

print("Frase salva com sucesso em 'filme_favorito.txt'!")