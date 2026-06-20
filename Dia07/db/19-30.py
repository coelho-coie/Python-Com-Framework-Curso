import sqlite3

def listar_disponiveis():
    with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT titulo, autor FROM livros WHERE status = 'disponível'")
        print("\n--- Livros Disponíveis para Empréstimo ---")
        for livro in cursor.fetchall():
            print(f"'{livro[0]}' por {livro[1]}")

# Exemplo de uso
listar_disponiveis()