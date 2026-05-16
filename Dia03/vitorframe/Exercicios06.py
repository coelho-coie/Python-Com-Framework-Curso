from datetime import datetime

print("Bem vindo, vc precisa ser maior de idade")
nasc = int(input("Digite seu ano de nacimento: "))
idade = datetime.now().year - nasc

if idade < 18:
    print("vc é menor de idade")
print()

print("-"*10)

temperatura_atual = 31

if temperatura_atual > 29:
    print("Clima típico de Sertãozinho! Cuidado com o calor.")
    
print("-"*10)

dia = "quarta"

if dia == "quarta":
    print("Dia de feira em Sertãozinho!")
    print("Não se esqueça de comprar pastel para o professor!")

print("-"*10)

idade = 25

if idade >= 18:
    print("Ingresso para o filme de terror liberado. \U0001F3AB")

print("-"*10)

palavra_chave = "Sertãozinho2025"

if palavra_chave == "Sertãozinho2025":
    print("Acesso ao sistema liberado. \U0001F513")

print("-"*10)

estoque_de_acucar = 35

if estoque_de_acucar < 50:
    print("Alerta: Estoque de açúcar baixo. Entrar em contato com a usina. \U000026A0")

print("-"*10)

tem_pulseira_vip = True

if tem_pulseira_vip:
    print("Bem-vindo(a) ao Camarote VIP! Aproveite o show! \U0001F942")

print("-"*10)

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo!")
    
print("-"*10)

nota = float(input("Digite a nota do aluno: "))

if nota >= 7.0:
    print("Aluno aprovado! \U0001F393")
else:
    print("Aluno reprovado. \U0001F4DA")

print("-"*10)

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}.")
else:
    print("Os dois números são iguais.")

print("-"*10)

numero = int(input("Digite um número inteiro: "))

# Se o resto da divisão por 2 for 0, o número é par
if (numero % 2) == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

print("-"*10)

altura = float(input("Digite sua altura em metros (ex: 1.75): "))

if altura >= 1.60:
    print("Entrada permitida no brinquedo! Divirta-se!")
else:
    print("Desculpe, sua altura está abaixo do mínimo exigido.")

print("-"*10)

peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc > 18.5 and imc < 25:
    print("Classificação: Peso normal.")
elif imc > 25 and imc < 30:
    print("Classificação: Sobrepeso.")
else: # Se não for nenhum dos anteriores, só pode ser >= 30
    print("Classificação: Obesidade.")

print("-"*10)

valor_saque = int(input("Digite o valor que deseja sacar: R$ "))

if valor_saque > 0 and (valor_saque % 10) == 0:
    print(f"Saque de R$ {valor_saque},00 realizado com sucesso!")
else:
    print("Erro: O valor do saque deve ser positivo e múltiplo de 10.")

print("-"*10)

valor_compra = float(input("Digite o valor total da compra: R$ "))
valor_final = valor_compra

if valor_compra > 500:
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 15%! (R$ {desconto:.2f})")
elif valor_compra >= 200 and valor_compra <= 500:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 10%! (R$ {desconto:.2f})")
else:
    print("Compras abaixo de R$ 200,00 não têm desconto.")

print(f"O valor final a pagar é: R$ {valor_final:.2f}")

print("-"*10)

letra = input("Digite uma única letra: ").lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"A letra '{letra}' é uma VOGAL.")
else:
    print(f"A letra '{letra}' é uma CONSOANTE.")

print("-"*10)

print("--- MENU DO BANCO ---")
print("1. Ver Saldo")
print("2. Fazer Depósito")
print("3. Realizar Saque")
print("---------------------")

opcao = input("Digite o número da opção desejada: ")

if opcao == '1':
    print("Executando a operação: VER SALDO...")
elif opcao == '2':
    print("Executando a operação: FAZER DEPÓSITO...")
elif opcao == '3':
    print("Executando a operação: REALIZAR SAQUE...")
else:
    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

print("-"*10)

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Primeira verificação: é um triângulo válido?
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo válido.")

    # Se for válido, entra no if aninhado para classificar
    if a == b and b == c:
        print("Classificação: Equilátero.")
    elif a == b or a == c or b == c:
        print("Classificação: Isósceles.")
    else:
        print("Classificação: Escaleno.")
else:
    print("Os lados fornecidos não podem formar um triângulo.")

print("-"*10)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}.")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}.")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}.")
elif operacao == '/':
    # Verificação aninhada para evitar o erro de divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é {resultado}.")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Operação inválida. Por favor, escolha +, -, * ou /.")

print("-"*10)

ano = int(input("Digite um ano para verificar se é bissexto: "))

# A regra complexa em uma única condição 'if'
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é bissexto.")

print("-"*10)

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data_valida = True # Começamos assumindo que a data é válida

if mes < 1 or mes > 12 or dia < 1 or dia > 31 or ano <= 0:
    data_valida = False
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    # Meses com 30 dias não podem ter dia 31
    data_valida = False
elif mes == 2 and dia > 28:
    # Fevereiro (simplificado) não pode ter dia maior que 28
    data_valida = False

if data_valida:
    print(f"A data {dia}/{mes}/{ano} é provavelmente válida.")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida.")

print("-"*10)

jogada_computador = "pedra"
jogada_usuario = input("Sua jogada (pedra, papel, tesoura): ").lower()

print(f"\nO computador escolheu: {jogada_computador}")
print(f"Você escolheu: {jogada_usuario}")

# Lógica do jogo
if jogada_usuario == jogada_computador:
    print("Resultado: Empate!")
elif (jogada_usuario == "pedra" and jogada_computador == "tesoura") or \
     (jogada_usuario == "tesoura" and jogada_computador == "papel") or \
     (jogada_usuario == "papel" and jogada_computador == "pedra"):
    print("Resultado: Você venceu! \U0001F3C6")
else:
    print("Resultado: O computador venceu! \U0001F916")

print("-"*10)