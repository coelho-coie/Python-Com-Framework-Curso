# Uso do split
texto = "Python é poderoso"
partes = texto.split()

print(partes)

print("-"*10)

# Uso do map
valores = ["10", "20", "30"]

numeros = map(int, valores)

print(list(numeros))

print("-"*10)

# Uso do join
palavras = partes.copy()

frase = " ".join(palavras)

print(frase)

print("-"*10)

# Lê a entrada do usuário e divide a string em uma lista de nomes usando os espaços como separador
nomes = input().split()

# Junta os elementos da lista 'nomes' em uma única string, separando-os por vírgula e espaço
resultado = ", ".join(nomes)

# Exibe o resultado final na tela
print(resultado)

print("-"*10)

# Lê a entrada, divide pelos espaços e converte cada parte para inteiro (int)
a, b = map(int, input().split())

# Calcula a soma das variáveis 'a' e 'b' e exibe o resultado
print(a + b)

print("-"*10)

# Lê o texto digitado pelo usuário
texto = input()

# Divide a string onde houver hifens ("-") e armazena o resultado em uma lista
lista = texto.split("-")

# Exibe a lista gerada
print(lista)

print("-"*10)

# Lê a entrada, separa os valores, converte para float e transforma tudo em uma lista
numeros = list(map(float, input().split()))

# Exibe a lista de números decimais
print(numeros)

print("-"*10)

# Define a lista inicial com os números de telefone em formato de texto
telefones = ["9999-1111", "8888-2222", "7777-3333"]

# Une os elementos da lista em uma única string, colocando " | " entre eles
texto = " | ".join(telefones)

# Exibe a string resultante
print(texto)

print("-"*10)

# Lê a data, divide a string na barra ("/") e atribui às variáveis dia, mes e ano
dia, mes, ano = input().split("/")

# Exibe as variáveis de forma clara usando uma f-string formatada
print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}")

print("-"*10)

valor_saque = int(input("Digite o valor que deseja sacar: R$ "))

if valor_saque > 0 and (valor_saque % 10) == 0:
    print(f"Saque de R$ {valor_saque},00 realizado com sucesso!")
else:
    print("Erro: O valor do saque deve ser positivo e múltiplo de 10.")

print("-"*10)

# Lê os números, separa por espaço, converte para inteiro e armazena em uma lista
numeros = list(map(int, input().split()))

# Calcula a média somando todos os itens da lista e dividindo pela quantidade de itens
media = sum(numeros) / len(numeros)

# Exibe o valor da média calculada
print(media)

print("-"*10)

# Lê os dados do produto digitados, separados por vírgula
dados = input().split(",")

# Atribui o primeiro elemento ao nome (já é string, não precisa converter)
nome = dados[0]
# Converte o segundo elemento para número inteiro (quantidade)
quantidade = int(dados[1])
# Converte o terceiro elemento para número decimal (preço)
preco = float(dados[2])

# Calcula o valor total multiplicando a quantidade pelo preço unitário
total = quantidade * preco

# Exibe o valor total
print(total)

print("-"*10)

# Lê as coordenadas, separa por espaço e converte as três para inteiro
x, y, z = map(int, input().split())

# Multiplica cada coordenada por 2 e converte o resultado de volta para string
novas_coordenadas = [str(x * 2), str(y * 2), str(z * 2)]

# Une as novas coordenadas usando o traço ("-") como separador
resultado = "-".join(novas_coordenadas)

# Exibe o texto final
print(resultado)

print("-"*10)

# Lê a frase inteira e a divide em uma lista de palavras independentes
palavras = input().split()

# Cria uma nova lista aplicando o método capitalize() (primeira letra maiúscula) em cada palavra
palavras_formatadas = [palavra.capitalize() for palavra in palavras]

# Junta as palavras modificadas em um único texto, separando-as por espaço novamente
resultado = " ".join(palavras_formatadas)

# Exibe o resultado final
print(resultado)

print("-"*10)

# Lê a entrada, divide no ponto e vírgula e converte tudo para float em uma lista
temperaturas = list(map(float, input().split(";")))

# Filtra apenas as temperaturas maiores ou iguais a zero, transformando-as em string
validas = [str(temp) for temp in temperaturas if temp >= 0]

# Une as temperaturas válidas com a seta (" -> ") como separador
resultado = " -> ".join(validas)

# Exibe o resultado da filtragem
print(resultado)

print("-"*10)

# Lê os blocos binários e separa por espaços em uma lista de textos
binarios = input().split()

# Usa o map com uma função anônima (lambda) para converter cada binário (base 2) para inteiro comum
decimais = map(lambda x: int(x, 2), binarios)

# Converte os números inteiros de volta para string dentro de outro map, e junta com vírgula e espaço
resultado = ", ".join(map(str, decimais))

# Exibe o resultado das conversões
print(resultado)

print("-"*10)

# Lê a frase completa e separa em palavras
palavras = input().split()

# Filtra palavras com mais de 4 letras e aplica o método upper() para deixá-las maiúsculas
filtradas = [p.upper() for p in palavras if len(p) > 4]

# Junta as palavras que restaram colocando " | " entre elas
resultado = " | ".join(filtradas)

# Exibe o resultado final
print(resultado)

print("-"*10)

# Separa a entrada principal em linhas isoladas, quebrando no ponto e vírgula
linhas = input().split(";")

# Cria uma lista vazia principal onde vamos guardar os números
matriz_plana = []

# Laço de repetição para percorrer cada linha gerada
for linha in linhas:
    # Divide cada linha pelas vírgulas, converte para inteiro e adiciona os itens na lista principal
    matriz_plana.extend(map(int, linha.split(",")))

# Exibe a lista unificada com todos os números
print(matriz_plana)

print("-"*10)

# Lê os e-mails digitados e os separa por vírgula
emails_brutos = input().split(",")

# Cria um conjunto (Set) aplicando strip() em cada e-mail para remover espaços e descartar duplicatas automaticamente
emails_limpos = {email.strip() for email in emails_brutos}

# Pega esse conjunto livre de duplicatas, transforma em lista e a ordena em ordem alfabética
emails_ordenados = sorted(list(emails_limpos))

# Junta os e-mails formatados e ordenados usando ponto e vírgula
resultado = ";".join(emails_ordenados)

# Exibe o texto perfeitamente limpo
print(resultado)

print("-"*10)