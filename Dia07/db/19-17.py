import sqlite3
conexao = sqlite3.connect('Dia07/db/biblioteca.db')
cursor = conexao.cursor()
livros_para_inserir = [
    ('Dom Quixote', 'Miguel de Cervantes', 1605),
    ('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954),
    ('1984', 'George Orwell', 1949)
]
cursor.executemany("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", livros_para_inserir)
conexao.commit()
print("Três livros inseridos.")
conexao.close()