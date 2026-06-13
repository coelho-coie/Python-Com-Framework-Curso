try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")
    
    resultado = 0
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '/':
        if num2 == 0:
            resultado = "Erro: Divisão por zero"
        else:
            resultado = num1 / num2
    else:
        resultado = "Operação inválida"
        
    print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: Você deve digitar apenas números para o cálculo.")