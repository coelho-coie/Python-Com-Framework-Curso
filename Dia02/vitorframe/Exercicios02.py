
def Separador():
    print("\n" * 2)

# 1. Criação das variáveis com dados de exemplo
nome = "Ana Carolina"
idade = 29
cidade = "Sertãozinho"

# 2. Impressão de cada variável em uma linha distinta
print("--- Perfil do Usuário ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")

Separador()

# 1. Pede o nome do usuário e guarda na variável 'nome_usuario'
nome_usuario = input("Por favor, digite o seu nome: ")

# 2. Usa uma f-string para criar e imprimir a mensagem de boas-vindas
print(f"Olá, {nome_usuario}! Seja muito bem-vindo(a) ao curso de Python.")

Separador()

# Criação das variáveis de tipos diferentes
nome_produto = "Fone de Ouvido Bluetooth" # str
quantidade = 150                      # int
preco = 249.99                        # float
disponivel_em_estoque = True          # bool

# Impressão formatada de cada variável
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Preço unitário: R$ {preco}")
print(f"Disponível: {disponivel_em_estoque}")

Separador()

# 1. Pede o primeiro nome
primeiro_nome = input("Digite seu primeiro nome: ")

# 2. Pede o sobrenome
sobrenome = input("Digite seu sobrenome: ")

# 3. Junta as duas strings com um espaço no meio
nome_completo = primeiro_nome + " " + sobrenome

# 4. Imprime o resultado
print(f"Seu nome completo é: {nome_completo}")

Separador()

# 1. Pede a palavra
palavra = input("Digite uma palavra: ")

# 2. Pede o número de repetições e converte para inteiro
numero_de_vezes = int(input("Quantas vezes você quer repetir a palavra? "))

# 3. Usa o operador * para replicar a string
resultado = palavra * numero_de_vezes

# 4. Imprime o resultado final
print(resultado)

Separador()

# 1. Pede e converte os dois números
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# 2. Realiza os cálculos e guarda em variáveis
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 # Em Python, a divisão / sempre resulta em float

# 3. Imprime os resultados de forma organizada
print("\n--- Resultados ---")
print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} * {numero2} = {multiplicacao}")
print(f"{numero1} / {numero2} = {divisao}")

Separador()

# 1. Pede o peso e a altura, convertendo para float
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# 2. Calcula o IMC
imc = peso / (altura * altura)

# 3. Imprime o resultado formatado
# O :.2f dentro da f-string formata o número para ter apenas 2 casas decimais
print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

Separador()

# 1. Pede as informações do produto, convertendo os tipos
nome_produto = input("Digite o nome do produto: ")
qtd_estoque = int(input("Digite a quantidade em estoque: "))
preco_unitario = float(input("Digite o preço unitário (ex: 59.90): R$ "))

# 2. Imprime o resumo formatado
print("\n--- Resumo do Produto Cadastrado ---")
print(f"Nome: \t\t{nome_produto}")
print(f"Estoque: \t{qtd_estoque} unidades")
print(f"Preço: \t\tR$ {preco_unitario}")

Separador()

# 1. Coleta das informações
nome = input("Qual é o seu nome? ")
profissao = input("Qual é a sua profissão? ")
cidade = input("Em qual cidade você mora? ")

# 2. Monta e imprime a frase usando f-string
print("\n--- Apresentação ---")
print(f"Conheçam {nome}, um(a) excelente {profissao} que mora em {cidade}.")

Separador()

# 1. Define a constante PI
PI = 3.14159

# 2. Pede o raio ao usuário e converte para float
raio = float(input("Digite o raio do círculo: "))

# 3. Calcula a área
area = PI * (raio * raio)

# 4. Imprime o resultado formatado com 2 casas decimais
print(f"A área de um círculo com raio {raio} é {area:.2f}")

Separador()

# 1. Pede os valores da conta e da porcentagem
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = int(input("Digite a porcentagem da gorjeta (ex: 10, 15): "))

# 2. Calcula o valor da gorjeta
valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)

# 3. Calcula o valor total a ser pago
valor_total = valor_conta + valor_gorjeta

# 4. Imprime o resumo da conta
print("\n--- Resumo da Conta ---")
print(f"Valor da Conta: R$ {valor_conta:.2f}")
print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {valor_gorjeta:.2f}")
print(f"Valor Total a Pagar: R$ {valor_total:.2f}")

Separador()

# 1. Pede a idade em anos
idade_anos = int(input("Digite sua idade em anos: "))

# 2. Define constantes para os cálculos
DIAS_NO_ANO = 365
MESES_NO_ANO = 12
HORAS_NO_DIA = 24

# 3. Realiza os cálculos
idade_meses = idade_anos * MESES_NO_ANO
idade_dias = idade_anos * DIAS_NO_ANO
idade_horas = idade_dias * HORAS_NO_DIA

# 4. Imprime os resultados
print("\n--- Sua Idade em Diferentes Períodos ---")
print(f"Sua idade em meses é: {idade_meses} meses")
print(f"Sua idade em dias é: {idade_dias} dias")
print(f"Sua idade em horas é: {idade_horas} horas")

Separador()

# 1. Coleta de dados do produto
produto = input("Nome do produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unidade = float(input("Preço por unidade: R$ "))

# 2. Calcula o total
total = quantidade * preco_unidade

# 3. Imprime o recibo formatado
print("\n--- RECIBO ---")
print("=" * 30)
print(f"Produto: \t{produto}")
print(f"Quantidade: \t{quantidade}x")
print(f"Preço Unitário: R$ {preco_unidade:.2f}")
print("-" * 30)
print(f"TOTAL A PAGAR: \tR$ {total:.2f}")
print("=" * 30)

Separador()

# 1. Pede os dados ao usuário
primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
ano_nascimento = input("Digite seu ano de nascimento (ex: 1995): ") # Pega como string

# 2. Fatiamento de strings para pegar as partes desejadas
parte1 = primeiro_nome[0:3].lower()  # Pega os 3 primeiros caracteres e converte para minúsculo
parte2 = sobrenome[0:3].lower()     # Pega os 3 primeiros caracteres e converte para minúsculo
parte3 = ano_nascimento[2:4]        # Pega os 2 últimos caracteres

# 3. Junta tudo para formar o nome de usuário
username = parte1 + parte2 + parte3

# 4. Imprime a sugestão
print(f"\nSugestão de nome de usuário: {username}")

Separador()

# 1. Coleta dos dados da viagem
distancia = float(input("Qual a distância da viagem em KM? "))
velocidade_media = float(input("Qual a velocidade média esperada em KM/h? "))
consumo_carro = float(input("Qual o consumo do carro (KM por Litro)? "))

# 2. Calcula o tempo de viagem (Tempo = Distância / Velocidade)
tempo_viagem = distancia / velocidade_media

# 3. Calcula o combustível necessário (Litros = Distância / Consumo)
combustivel_necessario = distancia / consumo_carro

# 4. Imprime o relatório da viagem
print("\n--- Planejamento da Viagem ---")
print(f"Tempo estimado: {tempo_viagem:.2f} horas")
print(f"Combustível necessário: {combustivel_necessario:.2f} litros")