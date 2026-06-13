# Pedimos um valor ao usuário
entrada_usuario = input("Digite um número inteiro: ")

try:
    # TENTAMOS converter a entrada para um número inteiro.
    # Se o usuário digitou "abc" ou "5.2", esta linha vai dar um erro (ValueError).
    # Caso algum erro ocorra o "Try" para imediatamente e se desloca para o "Except"
    numero = int(entrada_usuario)
    
    # Se a linha acima funcionou, o código continua e mostra a mensagem de sucesso.
    print(f"Ótimo! O número {numero} é um inteiro válido.")

except:
    # Se a conversão no bloco 'try' falhou, o programa pula para cá.
    # Em vez de quebrar, ele executa o código que está aqui dentro.
    print("Erro: Por favor, digite um número inteiro válido.")