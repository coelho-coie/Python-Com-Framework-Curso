import sqlite3

def menu():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Listar Todos os Livros")
        print("3. Buscar por Autor")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Reutiliza a função do exercício anterior
            titulo = input("Título: "); autor = input("Autor: "); ano = int(input("Ano: "))
            adicionar_livro(titulo, autor, ano)
        elif opcao == '2':
            listar_todos()
        elif opcao == '3':
            autor = input("Digite o nome do autor para buscar: ")
            buscar_por_autor(autor)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def adicionar_livro(titulo, autor, ano):
    # ... (código da função do exercício intermediário 1)
    with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", (titulo, autor, ano))
        conexao.commit()
    print("Livro adicionado.")

def listar_todos():
    with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros ORDER BY titulo")
        for livro in cursor.fetchall():
            print(livro)

def buscar_por_autor(autor):
    with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", (f'%{autor}%',))
        for livro in cursor.fetchall():
            print(livro)

# Inicia o menu
menu()