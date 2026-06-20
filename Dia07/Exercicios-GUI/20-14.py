import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário:', size=(8, 1)), sg.Input(key='-USER-')],
    [sg.Text('Senha:', size=(8, 1)), sg.Input(key='-PASS-', password_char='*')],
    [sg.Button('Entrar')]
]

window = sg.Window('Tela de Login', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Entrar':
        if values['-USER-'] == 'admin' and values['-PASS-'] == '1234':
            sg.popup('Login bem-sucedido!')
            break
        else:
            sg.popup_error('Usuário ou senha inválidos.')

window.close()