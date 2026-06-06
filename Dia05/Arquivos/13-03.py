# Primeiro, criamos o arquivo com o cabeçalho usando 'w'.
with open("desejos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Minha lista de desejos:\n")

novo_desejo = input("Digite um desejo para adicionar à lista: ")

# Agora, usamos 'a' para adicionar ao final, sem apagar o que já estava lá.
with open("desejos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(novo_desejo + "\n")

print("Seu desejo foi adicionado à lista!")