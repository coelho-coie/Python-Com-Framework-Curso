try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido para a idade.")