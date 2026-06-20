import sqlite3
conexao = sqlite3.connect('Dia07/db/biblioteca.db')
cursor = conexao.cursor()
# A função COUNT(*) do SQL conta o número de linhas
cursor.execute("SELECT COUNT(*) FROM livros")
total_livros = cursor.fetchone()[0] # fetchone() retorna uma tupla, pegamos o primeiro item
print(f"A biblioteca tem um total de {total_livros} livros.")
conexao.close()