import sqlite3
def buscar_livro_por_titulo(titulo):
    conexao = sqlite3.connect('Dia07/db/biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros WHERE titulo LIKE ?", (f'%{titulo}%',)) # LIKE busca por partes do texto
    resultados = cursor.fetchall()
    conexao.close()
    
    if resultados:
        print(f"Resultados para '{titulo}':")
        for livro in resultados:
            print(livro)
    else:
        print(f"Nenhum livro encontrado com o título '{titulo}'.")

# Exemplo de uso
buscar_livro_por_titulo("Senhor dos Anéis")