import PySimpleGUI as sg

contador = 0

layout = [
    [sg.Text('Você clicou:'), sg.Text(f'{contador}', key='-CONTADOR-', size=(5,1), font=('Helvetica', 24))],
    [sg.Button('Clique em Mim!')]
]

window = sg.Window('Contador', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Clique em Mim!':
        contador += 1
        window['-CONTADOR-'].update(f'{contador}')

window.close()