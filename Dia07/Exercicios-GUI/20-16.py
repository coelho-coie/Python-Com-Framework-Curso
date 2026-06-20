import PySimpleGUI as sg

layout = [
    [sg.Multiline(size=(60, 15), key='-TEXTO-')],
    [sg.Button('MAIÚSCULAS'), sg.Button('minúsculas')]
]

window = sg.Window('Editor de Texto', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    texto_atual = values['-TEXTO-']
    
    if event == 'MAIÚSCULAS':
        window['-TEXTO-'].update(texto_atual.upper())
    if event == 'minúsculas':
        window['-TEXTO-'].update(texto_atual.lower())

window.close()