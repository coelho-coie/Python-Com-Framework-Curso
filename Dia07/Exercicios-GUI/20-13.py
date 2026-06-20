import PySimpleGUI as sg

layout = [
    [sg.Input(size=(10, 1), key='-NUM1-'), 
     sg.Combo(['+', '-', '*', '/'], default_value='+', key='-OP-'), 
     sg.Input(size=(10, 1), key='-NUM2-')],
    [sg.Button('Calcular')],
    [sg.Text('Resultado:', size=(30, 1), font=('Helvetica', 14), key='-RES-')]
]

window = sg.Window('Calculadora', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calcular':
        try:
            num1 = float(values['-NUM1-'])
            num2 = float(values['-NUM2-'])
            op = values['-OP-']
            resultado = 0
            if op == '+': resultado = num1 + num2
            if op == '-': resultado = num1 - num2
            if op == '*': resultado = num1 * num2
            if op == '/':
                if num2 == 0:
                    resultado = "Erro: Divisão por zero"
                else:
                    resultado = num1 / num2
            
            window['-RES-'].update(f'Resultado: {resultado}')
        except (ValueError, TypeError):
            window['-RES-'].update('Erro: Entrada inválida')

window.close()