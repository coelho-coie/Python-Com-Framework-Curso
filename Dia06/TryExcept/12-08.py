while True:
    entrada = input("Digite um número ou 'sair' para terminar: ")
    
    if entrada.lower() == 'sair':
        print("Encerrando o programa...")
        break
        
    try:
        numero = float(entrada)
        print(f"O dobro de {numero} é {numero * 2}.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")