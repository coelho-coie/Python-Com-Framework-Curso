nome_arquivo = input("Digite o nome do arquivo para contar as palavras: ")

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    # O método .split() quebra o texto em uma lista de palavras.
    lista_de_palavras = conteudo.split()
    numero_de_palavras = len(lista_de_palavras)
    
    print(f"O arquivo '{nome_arquivo}' contém {numero_de_palavras} palavras.")