import sqlite3
def atualizar_ano(titulo, novo_ano):
    conexao = sqlite3.connect('Dia07/db/biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE livros SET ano_publicacao = ? WHERE titulo = ?", (novo_ano, titulo))
    conexao.commit()
    # .rowcount diz quantas linhas foram afetadas pela última operação
    if cursor.rowcount > 0:
        print(f"Ano do livro '{titulo}' atualizado para {novo_ano}.")
    else:
        print(f"Livro '{titulo}' não encontrado.")
    conexao.close()

# Exemplo de uso
atualizar_ano("1984", 1950) # Vamos "errar" o ano para testar