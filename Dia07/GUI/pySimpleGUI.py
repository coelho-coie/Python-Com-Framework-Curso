import PySimpleGUI as sg

# Define um tema de cores para deixar a janela mais bonita
sg.theme('DarkBlue3')

# O layout descreve a aparência da janela, linha por linha
layout = [
    [sg.Text('Conversor de Temperatura')],
    # Uma linha com um Input para o número e um Combo para a opção
    [sg.Input(key='-INPUT-', size=(10, 1)), 
     sg.Combo(['Celsius para Fahrenheit', 'Fahrenheit para Celsius'], default_value='Celsius para Fahrenheit', key='-CONVERSAO-')],
    # Uma linha com os botões de ação
    [sg.Button('Converter'), sg.Button('Sair')],
    # Uma linha com um Text vazio que será usado para mostrar o resultado
    [sg.Text(size=(40,1), key='-OUTPUT-')]
]

# Cria a janela a partir do layout
window = sg.Window('Conversor', layout)

# Loop infinito para manter a janela aberta e receber eventos
while True:
    # window.read() pausa o programa e espera uma ação do usuário
    event, values = window.read()
    
    # Se o usuário fechar a janela (no 'X') ou clicar em 'Sair'
    if event == sg.WIN_CLOSED or event == 'Sair':
        break # Quebra o loop e encerra o programa
    
    # Se o evento for o clique no botão 'Converter'
    if event == 'Converter':
        try:
            # Pega o valor do campo de Input e converte para número
            temp_input = float(values['-INPUT-'])
            
            # Verifica qual opção do Combo foi escolhida e faz o cálculo
            if values['-CONVERSAO-'] == 'Celsius para Fahrenheit':
                resultado = temp_input * 9/5 + 32
                # Atualiza o texto do elemento '-OUTPUT-' com o resultado formatado
                window['-OUTPUT-'].update(f'{temp_input}°C é igual a {resultado:.2f}°F')
            else:
                resultado = (temp_input - 32) * 5/9
                window['-OUTPUT-'].update(f'{temp_input}°F é igual a {resultado:.2f}°C')
        except ValueError:
            # Se o usuário não digitar um número, mostra uma mensagem de erro
            window['-OUTPUT-'].update('Por favor, digite um número válido.')

# Fecha a janela de forma limpa
window.close()