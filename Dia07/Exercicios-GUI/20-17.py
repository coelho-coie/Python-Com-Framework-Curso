import PySimpleGUI as sg
import os

layout = [
    [sg.Text('Digite a extensão (ex: .txt, .py):'), sg.Input('.py', key='-EXT-', size=(10,1))],
    [sg.Button('Procurar Pasta')],
    [sg.Listbox(values=[], size=(60, 15), key='-LISTA-')]
]

window = sg.Window('Buscador de Arquivos', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Procurar Pasta':
        # Abre a janela do sistema para escolher uma pasta
        pasta = sg.popup_get_folder('Selecione uma pasta')
        if pasta: # Se o usuário selecionou uma pasta
            extensao = values['-EXT-']
            arquivos_encontrados = []
            try:
                # os.listdir() lista tudo que está dentro de uma pasta
                for nome_arquivo in os.listdir(pasta):
                    if nome_arquivo.endswith(extensao):
                        arquivos_encontrados.append(nome_arquivo)
                
                window['-LISTA-'].update(values=arquivos_encontrados)
            except Exception as e:
                sg.popup_error(f'Ocorreu um erro: {e}')

window.close()