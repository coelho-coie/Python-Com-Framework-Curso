import sqlite3

conexao = sqlite3.connect('Dia07/db/biblioteca.db')
cursor = conexao.cursor()

try:
    # Adiciona a coluna 'status' com um valor padrão
    cursor.execute("ALTER TABLE livros ADD COLUMN status TEXT DEFAULT 'disponível'")
    print("Coluna 'status' adicionada com sucesso.")
except sqlite3.OperationalError as e:
    # Este erro acontece se a coluna já existir, o que é esperado após a primeira execução
    print(f"Não foi possível adicionar a coluna (provavelmente ela já existe): {e}")

conexao.commit()
conexao.close()