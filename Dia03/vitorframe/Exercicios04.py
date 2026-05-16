# Definição das variáveis
a = 75
b = 3
c = 5
d = 7

# Realiza as somas
soma1 = a + b
soma2 = c + d

# Compara os resultados das somas
resultado_comparacao = soma1 > soma2

print(f"A soma de {a}+{b} é {soma1}.")
print(f"A soma de {c}+{d} é {soma2}.")
print(f"A primeira soma é maior que a segunda? {resultado_comparacao}")

print("-"*10)

# Define o resultado correto
resultado_correto = 12 * 5

# Pede um palpite ao usuário e converte para inteiro
while True:
    try:
        palpite_usuario = int(input("Quanto é 12 * 5? Digite sua resposta: "))
        break
    except:
        continue

# Compara o palpite com o resultado correto
acertou = palpite_usuario == resultado_correto
if acertou:
    acertou = "Sim"
else:
    acertou = "Não"
print(f"O resultado correto é {resultado_correto}.")
print(f"Você acertou a resposta? {acertou}")

print("-"*10)

# Pede um número e o converte para inteiro

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except:
        continue

# Calcula o resto da divisão por 2 e compara com 0
e_par = (numero % 2) == 0

print(f"O número {numero} é par? {e_par}")

print("-"*10)

# Pede um número e o converte para float, para aceitar decimais
while True:
    try:
        numero = float(input("Digite um número: "))
        break
    except:
        continue

# Verifica as duas condições com o operador 'and'
esta_no_intervalo = numero > 10 and numero < 20

print(f"O número está entre 10 e 20? {esta_no_intervalo}")

print("-"*10)

# Pede o dia da semana e converte para minúsculas para evitar erros de digitação
semana = ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado","Domingo"]
print(semana)
dia_da_semana = input("Escolha algum dia do final de semana: ").lower()


# Verifica se o dia é um dos dois com o operador 'or'
e_fim_de_semana = dia_da_semana == "sábado" or dia_da_semana == "domingo"

print(f"É fim de semana? {e_fim_de_semana}")

print("-"*10)

# Pede a idade e a converte para inteiro
idade = int(input("Digite a idade: "))

# Monta a condição composta para verificar se a idade está no intervalo inclusivo
esta_na_faixa_permitida = idade >= 18 and idade <= 65

print(f"A participação no evento é permitida? {esta_na_faixa_permitida}")

print("-"*10)

# Pede as três notas e converte para float
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Encontra a menor nota
menor_nota = min(nota1, nota2, nota3)

# Verifica as duas condições para aprovação
foi_aprovado = media >= 7.0 and menor_nota > 3.0

print(f"A média do aluno foi: {media:.2f}")
print(f"A menor nota foi: {menor_nota}")
print(f"O aluno foi aprovado? {foi_aprovado}")

print("-"*10)

# Pede os dados da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))
estado = input("Digite a sigla do seu estado (UF): ").upper() # .upper() para garantir que seja maiúscula

# A primeira condição composta: (valor > 100 E estado é SP)
condicao_sp = valor_compra > 100.00 and estado == "SP"

# A segunda condição: valor > 250
condicao_outros_estados = valor_compra > 250.00

# O frete é grátis se a primeira OU a segunda condição for verdadeira
tem_frete_gratis = condicao_sp or condicao_outros_estados

print(f"O cliente tem direito a frete grátis? {tem_frete_gratis}")

print("-"*10)

# Pede um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o resto da divisão por 3 é zero
divisivel_por_3 = (numero % 3) == 0

# Verifica se o resto da divisão por 5 é zero
divisivel_por_5 = (numero % 5) == 0

# A condição final exige que AMBAS as condições acima sejam verdadeiras
e_divisivel_por_ambos = divisivel_por_3 and divisivel_por_5

print(f"O número {numero} é divisível por 3 e 5 ao mesmo tempo? {e_divisivel_por_ambos}")

print("-"*10)

# Simulação das variáveis de status
conta_ativa = True
e_convidado = False
servidor_manutencao = False

# A primeira parte da lógica: o usuário é válido se for ativo OU convidado
usuario_valido = conta_ativa or e_convidado

# A condição final: o usuário precisa ser válido E o servidor não pode estar em manutenção
pode_jogar = usuario_valido and (not servidor_manutencao)

print(f"O usuário pode jogar? {pode_jogar}")

print("-"*10)

# Coleta de dados
salario = float(input("Digite seu salário mensal: R$ "))
prestacao = float(input("Digite o valor da prestação desejada: R$ "))
anos_de_servico = int(input("Há quantos anos completos trabalha na empresa? "))

# Calcula o limite de 30% do salário
limite_prestacao = salario * 0.30

# Condições individuais
condicao_salario = salario > 3000
condicao_tempo_servico = anos_de_servico >= 2
condicao_prestacao = prestacao <= limite_prestacao

# Condição final: todas as três precisam ser verdadeiras
emprestimo_aprovado = condicao_salario and condicao_tempo_servico and condicao_prestacao

print(f"\nLimite da prestação (30%): R$ {limite_prestacao:.2f}")
print(f"Empréstimo Aprovado? {emprestimo_aprovado}")

print("-"*10)

# Pede os três lados
lado_a = float(input("Digite o comprimento do lado A: "))
lado_b = float(input("Digite o comprimento do lado B: "))
lado_c = float(input("Digite o comprimento do lado C: "))

# A regra do triângulo exige que todas as três condições sejam verdadeiras
condicao1 = (lado_a + lado_b) > lado_c
condicao2 = (lado_a + lado_c) > lado_b
condicao3 = (lado_b + lado_c) > lado_a

e_triangulo_valido = condicao1 and condicao2 and condicao3

print(f"Os lados fornecidos formam um triângulo válido? {e_triangulo_valido}")

print("-"*10)

# Pede o ano
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Condição 1: É divisível por 4 E não é divisível por 100
condicao1 = (ano % 4 == 0) and (ano % 100 != 0)

# Condição 2: É divisível por 400 (esta é a exceção da exceção)
condicao2 = (ano % 400 == 0)

# O ano é bissexto se a condição 1 OU a condição 2 for verdadeira
e_bissexto = condicao1 or condicao2

print(f"O ano {ano} é bissexto? {e_bissexto}")

print("-"*10)

# Coleta de dados
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
problema_cardiaco_str = input("Você possui algum problema cardíaco (sim/nao)? ").lower()

# Converte a resposta 'sim'/'nao' para um booleano
tem_problema_cardiaco = problema_cardiaco_str == "sim"

# Regra 1: Altura suficiente E sem problemas cardíacos
regra1 = altura > 1.50 and (not tem_problema_cardiaco)

# Regra 2: Super alto (assume a responsabilidade)
regra2 = altura > 1.80

# Pode entrar se a regra 1 OU a regra 2 for verdadeira
pode_entrar = regra1 or regra2

print(f"Pode entrar na montanha-russa? {pode_entrar}")

print("-"*10)

# Pede os dados da data
dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))
ano_dois_digitos = int(input("Digite o ano com dois dígitos (ex: 24 para 2024): "))

# Calcula o produto do dia pelo mês
produto_dia_mes = dia * mes

# Compara o produto com o ano
e_data_magica = produto_dia_mes == ano_dois_digitos

print(f"A data {dia}/{mes}/{ano_dois_digitos} é uma data mágica? {e_data_magica}")