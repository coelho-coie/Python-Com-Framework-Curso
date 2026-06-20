import sqlite3

def cadastrar_livro_interativo():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação: "))

    conexao = sqlite3.connect('Dia07/db/biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", (titulo, autor, ano))
    conexao.commit()
    conexao.close()
    print("\nLivro cadastrado com sucesso!")

cadastrar_livro_interativo()