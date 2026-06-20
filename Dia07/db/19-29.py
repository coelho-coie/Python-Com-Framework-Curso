import sqlite3

def emprestar_livro(titulo):
    with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
        cursor = conexao.cursor()
        # Primeiro, verifica se o livro está disponível
        cursor.execute("SELECT status FROM livros WHERE titulo = ?", (titulo,))
        resultado = cursor.fetchone()
        
        if resultado and resultado[0] == 'disponível':
            cursor.execute("UPDATE livros SET status = 'emprestado' WHERE titulo = ?", (titulo,))
            conexao.commit()
            print(f"O livro '{titulo}' foi emprestado.")
        elif resultado:
            print(f"O livro '{titulo}' já está emprestado.")
        else:
            print(f"Livro '{titulo}' não encontrado.")

# Exemplo de uso
emprestar_livro("1984")