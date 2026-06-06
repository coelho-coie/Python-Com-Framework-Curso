palavra_chave = input("Digite a palavra-chave para filtrar o log: ")
linhas_filtradas = []

# Primeiro, lemos o arquivo original e guardamos as linhas que nos interessam.
with open("log.txt", "r", encoding="utf-8") as arquivo_leitura:
    for linha in arquivo_leitura:
        if palavra_chave in linha:
            linhas_filtradas.append(linha)

# Agora, criamos o novo arquivo e escrevemos as linhas que guardamos.
with open("log_filtrado.txt", "w", encoding="utf-8") as arquivo_escrita:
    for linha in linhas_filtradas:
        arquivo_escrita.write(linha)

print("Filtro concluído! Verifique o arquivo 'log_filtrado.txt'.")