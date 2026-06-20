import PySimpleGUI as sg
from datetime import datetime

layout = [
    [sg.Text('Digite seu ano de nascimento:')],
    [sg.Input(key='-ANO-', size=(10, 1))],
    [sg.Button('Verificar Idade')],
    [sg.Text(key='-SAIDA-')] # Texto de saída
]

window = sg.Window('Verificador de Idade', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Verificar Idade':
        try:
            ano_nascimento = int(values['-ANO-'])
            ano_atual = datetime.now().year
            idade = ano_atual - ano_nascimento
            if idade >= 18:
                # Podemos mudar a cor do texto com text_color
                window['-SAIDA-'].update(f'Você tem {idade} anos. Você é maior de idade.', text_color='green')
            else:
                window['-SAIDA-'].update(f'Você tem {idade} anos. Você é menor de idade.', text_color='red')
        except ValueError:
            window['-SAIDA-'].update('Por favor, digite um ano válido.', text_color='orange')

window.close()