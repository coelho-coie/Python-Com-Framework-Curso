import sqlite3
conexao = sqlite3.connect('Dia07/db/biblioteca.db')
cursor = conexao.cursor()
# Adicionando um livro novo para o teste funcionar
cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 2001))
conexao.commit()

print("--- Livros publicados a partir de 2000 ---")
cursor.execute("SELECT * FROM livros WHERE ano_publicacao >= 2000")
livros_recentes = cursor.fetchall()
for livro in livros_recentes:
    print(livro)
conexao.close()