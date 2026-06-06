# Crie um arquivo chamado 'poema.txt' com algumas linhas para testar.
nome_arquivo = "historia.txt" 
contador = 1

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    print(f"\n--- Conteúdo de '{nome_arquivo}' ---")
    for linha in arquivo:
        # .strip() remove a quebra de linha invisível do final.
        print(f"{contador}: {linha.strip()}")
        contador = contador + 1