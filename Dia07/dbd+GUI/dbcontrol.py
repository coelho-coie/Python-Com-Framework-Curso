import sqlite3
import PySimpleGUI as sg

# --- Funções de Banco de Dados ---

def adicionar_livro(titulo, autor, ano):
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            # Certifique-se de que sua tabela tenha a coluna status, ou que ela seja criada com DEFAULT 'Disponível'
            cursor.execute("""
                INSERT INTO livros (titulo, autor, ano_publicacao, status) 
                VALUES (?, ?, ?, 'Disponível')
            """, (titulo, autor, int(ano)))
            conexao.commit()
        return True
    except Exception as e:
        sg.popup_error(f"Erro ao adicionar livro: {e}")
        return False

def listar_todos():
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, ano_publicacao, status FROM livros ORDER BY titulo")
            return cursor.fetchall()
    except Exception as e:
        sg.popup_error(f"Erro ao listar livros: {e}")
        return []

def buscar_por_autor(autor):
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, titulo, autor, ano_publicacao, status FROM livros WHERE autor LIKE ?", (f'%{autor}%',))
            return cursor.fetchall()
    except Exception as e:
        sg.popup_error(f"Erro ao buscar autor: {e}")
        return []

def atualizar_status_livro(id_livro, novo_status):
    try:
        with sqlite3.connect('Dia07/db/biblioteca.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE livros SET status = ? WHERE id = ?", (novo_status, id_livro))
            conexao.commit()
        return True
    except Exception as e:
        sg.popup_error(f"Erro ao atualizar status: {e}")
        return False


# --- Interface Gráfica com Tabela ---

sg.theme('DarkBlue3')

# Cabeçalho atualizado com a coluna Status
cabecalho = ['ID', 'Título', 'Autor', 'Ano Publicado', 'Status']

# Variável global para rastrear os dados que estão atualmente exibidos na tabela
dados_exibidos = []

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
        max_col_width=25,
        auto_size_columns=False,
        display_row_numbers=False,
        justification='center', 
        num_rows=10,
        key='-TABELA-',
        row_height=35,
        expand_x=True,
        enable_click_events=True # Permite interações com as linhas
    )],

    # Botões de Ação para o livro selecionado
    [
        sg.Button("Retirar Livro (Empréstimo)", key='-RETIRAR-', button_color=('black', 'orange'), size=(22, 1)),
        sg.Button("Devolver Livro", key='-DEVOLVER-', button_color=('white', 'green'), size=(15, 1)),
        sg.Text('', size=(2, 1)), # Substituído o sg.Spacer por um texto vazio para fazer o espaçamento
        sg.Button("Sair", size=(10, 1), button_color=('white', 'firebrick'))
    ]
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
                
                dados_exibidos = listar_todos()
                janela['-TABELA-'].update(values=dados_exibidos)
        else:
            sg.popup("Por favor, preencha todos os campos.", title="Aviso")

    # Ação: Listar Todos os Livros
    if evento == '-LISTAR-':
        dados_exibidos = listar_todos()
        janela['-TABELA-'].update(values=dados_exibidos)
        if not dados_exibidos:
            sg.popup_informative("Nenhum livro cadastrado.")

    # Ação: Buscar por Autor
    if evento == '-BUSCAR-':
        termo_busca = valores['-BUSCA_AUTOR-'].strip()
        if termo_busca:
            dados_exibidos = buscar_por_autor(termo_busca)
            janela['-TABELA-'].update(values=dados_exibidos)
            if not dados_exibidos:
                sg.popup_informative(f"Nenhum livro encontrado para o autor '{termo_busca}'.")
        else:
            sg.popup("Digite o nome de um autor para buscar.", title="Aviso")

    # Ação: Retirar Livro (Empréstimo)
    if evento == '-RETIRAR-':
        linhas_selecionadas = valores['-TABELA-']
        if linhas_selecionadas:
            index_linha = linhas_selecionadas[0]
            livro_selecionado = dados_exibidos[index_linha]
            
            id_livro = livro_selecionado[0]
            status_atual = livro_selecionado[4] # Coluna 4 é o Status
            
            if status_atual == 'Emprestado':
                sg.popup("Este livro já está emprestado!", title="Aviso")
            else:
                if atualizar_status_livro(id_livro, 'Emprestado'):
                    sg.popup_quick_message("Livro retirado com sucesso!", background_color='orange', text_color='black')
                    # Atualiza a tabela mantendo o contexto atual (se era busca ou listagem total)
                    dados_exibidos = listar_todos() if evento == '-LISTAR-' or not valores['-BUSCA_AUTOR-'] else buscar_por_autor(valores['-BUSCA_AUTOR-'])
                    janela['-TABELA-'].update(values=dados_exibidos)
        else:
            sg.popup("Selecione um livro na tabela primeiro.", title="Aviso")

    # Ação: Devolver Livro
    if evento == '-DEVOLVER-':
        linhas_selecionadas = valores['-TABELA-']
        if linhas_selecionadas:
            index_linha = linhas_selecionadas[0]
            livro_selecionado = dados_exibidos[index_linha]
            
            id_livro = livro_selecionado[0]
            status_atual = livro_selecionado[4]
            
            if status_atual == 'Disponível':
                sg.popup("Este livro já está disponível na biblioteca.", title="Aviso")
            else:
                if atualizar_status_livro(id_livro, 'Disponível'):
                    sg.popup_quick_message("Livro devolvido com sucesso!", background_color='green', text_color='white')
                    dados_exibidos = listar_todos() if evento == '-LISTAR-' or not valores['-BUSCA_AUTOR-'] else buscar_por_autor(valores['-BUSCA_AUTOR-'])
                    janela['-TABELA-'].update(values=dados_exibidos)
        else:
            sg.popup("Selecione um livro na tabela primeiro.", title="Aviso")

janela.close()