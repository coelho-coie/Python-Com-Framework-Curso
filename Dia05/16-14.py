def log_execucao(funcao_alvo):
    # O 'envelope' (ou wrapper) é a moldura que adiciona o novo comportamento
    def envelope():
        print("Comando enviado para a máquina...")
        funcao_alvo() # Aqui executamos a função original
    return envelope

@log_execucao # Aplicamos o decorador na função abaixo
def ligar_motor():
    print("O motor está em funcionamento!")

ligar_motor()