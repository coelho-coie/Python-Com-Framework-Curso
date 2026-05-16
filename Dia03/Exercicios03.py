numero1 = 15
numero2 = 30
soma = numero1 + numero2
print(f"A soma de {numero1} e {numero2} é {soma}.")

base = 10
altura = 5
area = base * altura
print(f"A área do retângulo é: {area}")

dividendo = 27
divisor = 4
quociente = dividendo // divisor
resto = dividendo % divisor
print(f"{dividendo} dividido por {divisor} é {quociente} e sobram {resto}.")

base = int(input("Digite o número base: "))
expoente = int(input("Digite o expoente: "))
potencia = base ** expoente
print(f"{base} elevado a {expoente} é igual a {potencia}.")

numero = 50
dobro = numero * 2
metade = numero / 2
print(f"O dobro de {numero} é {dobro}.")
print(f"A metade de {numero} é {metade}.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

total_minutos = int(input("Digite a quantidade total de minutos: "))
horas = total_minutos // 60
minutos_restantes = total_minutos % 60
print(f"{total_minutos} minutos correspondem a {horas} horas e {minutos_restantes} minutos.")

preco_original = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = int(input("Digite o percentual de desconto (%): "))
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto
print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço final com desconto é: R$ {preco_final:.2f}")

numero = int(input("Digite um número inteiro para verificar: "))
# Se o resto for 0, é par. Se for 1, é ímpar.
resultado = numero % 2
print(f"O resto da divisão de {numero} por 2 é: {resultado}.")
print("(Se o resultado for 0, o número é PAR. Se for 1, é ÍMPAR.)")

distancia = float(input("Distância da viagem (KM): "))
consumo_kml = float(input("Consumo do carro (KM/L): "))
preco_gasolina = float(input("Preço do litro da gasolina (R$): "))
litros_necessarios = distancia / consumo_kml
custo_total = litros_necessarios * preco_gasolina
print(f"O custo total da viagem será de R$ {custo_total:.2f}")

total_segundos = int(input("Digite a quantidade total de segundos: "))
horas = total_segundos // 3600
segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60
print(f"{total_segundos} segundos é igual a {horas}h {minutos}m {segundos_finais}s.")

cateto_b = float(input("Digite o valor do primeiro cateto: "))
cateto_c = float(input("Digite o valor do segundo cateto: "))
# Elevar a 0.5 é o mesmo que tirar a raiz quadrada
hipotenusa = ((cateto_b ** 2) + (cateto_c ** 2)) ** 0.5
print(f"A hipotenusa é: {hipotenusa:.2f}")

largura_parede = float(input("Largura da parede (metros): "))
altura_parede = float(input("Altura da parede (metros): "))
RENDIMENTO_TINTA_M2_POR_LITRO = 2
area_parede = largura_parede * altura_parede
litros_necessarios = area_parede / RENDIMENTO_TINTA_M2_POR_LITRO
print(f"Sua parede tem {area_parede:.2f} m².")
print(f"Você precisará de {litros_necessarios:.2f} litros de tinta.")

valor_saque = int(input("Digite o valor do saque (inteiro): R$ "))
notas_50 = valor_saque // 50
resto = valor_saque % 50
notas_20 = resto // 20
resto = resto % 20
notas_10 = resto // 10
resto = resto % 10
notas_1 = resto // 1 # ou simplesmente 'resto'
print(f"Para sacar R$ {valor_saque}, você receberá:")
print(f"{notas_50} nota(s) de R$50")
print(f"{notas_20} nota(s) de R$20")
print(f"{notas_10} nota(s) de R$10")
print(f"{notas_1} nota(s) de R$1")

numero = int(input("Digite um número inteiro de 3 dígitos: "))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
numero_invertido = (unidade * 100) + (dezena * 10) + centena
print(f"O número {numero} invertido é {numero_invertido}.")