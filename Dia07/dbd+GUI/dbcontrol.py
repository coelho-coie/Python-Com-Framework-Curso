import sqlite3
import PySimpleGUI as sg

# --- Funções de Banco de Dados ---

def adicionar_livro(titulo, autor, ano):
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)", (titulo, autor, int(ano)))
            conexao.commit()
        return True
    except Exception as e:
        sg.popup_error(f"Erro ao adicionar livro: {e}")
        return False

def listar_todos():
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, ano_publicacao FROM livros ORDER BY titulo")
            return cursor.fetchall()
    except Exception as e:
        sg.popup_error(f"Erro ao listar livros: {e}")
        return []

def buscar_por_autor(autor):
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, ano_publicacao FROM livros WHERE autor LIKE ?", (f'%{autor}%',))
            return cursor.fetchall()
    except Exception as e:
        sg.popup_error(f"Erro ao buscar autor: {e}")
        return []


# --- Interface Gráfica com Tabela ---

sg.theme('DarkBlue3')

# Definição dos cabeçalhos da tabela
cabecalho = ['ID', 'Título', 'Autor', 'Ano de Publicação']

layout = [
    [sg.Text("--- Sistema de Biblioteca ---", font=("Helvetica", 16), justification='center', expand_x=True)],
    
    # Seção para Adicionar Livro
    [sg.Frame("Adicionar Novo Livro", [
        [sg.Text("Título:", size=(6, 1)), sg.Input(key='-TITULO-', size=(45, 1))],
        [sg.Text("Autor:", size=(6, 1)), sg.Input(key='-AUTOR-', size=(45, 1))],
        [sg.Text("Ano:", size=(6, 1)), sg.Input(key='-ANO-', size=(10, 1)), sg.Button("Salvar Livro", key='-SALVAR-')]
    ])],
    
    # Seção para Buscar por Autor
    [sg.Frame("Filtros e Busca", [
        [sg.Text("Autor:"), sg.Input(key='-BUSCA_AUTOR-', size=(25, 1)), sg.Button("Buscar", key='-BUSCAR-'), sg.Button("Listar Todos", key='-LISTAR-')]
    ])],
    
    [sg.Text("Livros Encontrados:")],
    
    # Elemento de Tabela do PySimpleGUI
    [sg.Table(
        values=[], 
        headings=cabecalho, 
        max_col_width=35,
        auto_size_columns=True,
        display_row_numbers=False,
        justification='left', 
        num_rows=10,
        key='-TABELA-',
        row_height=25,
        expand_x=True
    )],
    
    [sg.Button("Sair", size=(10, 1), button_color=('white', 'firebrick'))]
]

janela = sg.Window("Gerenciador de Biblioteca com Tabela", layout, finalize=True, resizable=True)

# Loop principal
while True:
    evento, valores = janela.read()
    
    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break
        
    # Ação: Salvar Livro
    if evento == '-SALVAR-':
        titulo = valores['-TITULO-'].strip()
        autor = valores['-AUTOR-'].strip()
        ano = valores['-ANO-'].strip()
        
        if titulo and autor and ano:
            if adicionar_livro(titulo, autor, ano):
                sg.popup_quick_message("Livro adicionado com sucesso!", background_color='green', text_color='white')
                janela['-TITULO-'].update('')
                janela['-AUTOR-'].update('')
                janela['-ANO-'].update('')
                # Atualiza a tabela automaticamente após salvar
                janela['-TABELA-'].update(values=listar_todos())
        else:
            sg.popup("Por favor, preencha todos os campos.", title="Aviso")

    # Ação: Listar Todos os Livros
    if evento == '-LISTAR-':
        dados_livros = listar_todos()
        # Atualiza o componente tabela diretamente com a lista de tuplas do banco
        janela['-TABELA-'].update(values=dados_livros)
        if not dados_livros:
            sg.popup_informative("Nenhum livro cadastrado.")

    # Ação: Buscar por Autor
    if evento == '-BUSCAR-':
        termo_busca = valores['-BUSCA_AUTOR-'].strip()
        if termo_busca:
            dados_filtrados = buscar_por_autor(termo_busca)
            janela['-TABELA-'].update(values=dados_filtrados)
            if not dados_filtrados:
                sg.popup_informative(f"Nenhum livro encontrado para o autor '{termo_busca}'.")
        else:
            sg.popup("Digite o nome de um autor para buscar.", title="Aviso")

janela.close()