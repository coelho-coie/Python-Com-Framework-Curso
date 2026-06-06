nome_arquivo_original = "diario.txt"
palavra_antiga = input("Qual palavra você quer substituir? ")
palavra_nova = input(f"Por qual palavra você quer substituir '{palavra_antiga}'? ")
nome_arquivo_novo = "diario_modificado.txt"

with open(nome_arquivo_original, "r", encoding="utf-8") as f_origem:
    conteudo = f_origem.read()
    
# O método .replace() da string faz a substituição.
conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)
    
with open(nome_arquivo_novo, "w", encoding="utf-8") as f_destino:
    f_destino.write(conteudo_modificado)
        
print(f"Substituição concluída! O resultado foi salvo em '{nome_arquivo_novo}'.")