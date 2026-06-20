import sqlite3
def adicionar_livro(titulo, autor, ano):
    conexao = sqlite3.connect('Dia07/db/biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", (titulo, autor, ano))
    conexao.commit()
    conexao.close()
    print(f"Livro '{titulo}' adicionado com sucesso.")

# Exemplo de uso
adicionar_livro("A Revolução dos Bichos", "George Orwell", 1945)