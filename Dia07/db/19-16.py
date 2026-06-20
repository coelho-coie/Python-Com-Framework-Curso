import sqlite3
conexao = sqlite3.connect('Dia07/db/biblioteca.db')
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER
);
""")
print("Tabela 'livros' criada.")
conexao.close()