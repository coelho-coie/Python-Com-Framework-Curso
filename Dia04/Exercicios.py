# Perdido com as mudanças de computadores


# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install colorama
# Para verificar se a instalação deu certo, digite: pip list
import colorama
from colorama import Fore

colorama.init(autoreset=True)

print(Fore.GREEN + "Aprovado!")
print(Fore.RED + "Reprovado!")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install requests
# Para verificar se a instalação deu certo, digite: pip list
import requests

cep = input("Digite o CEP para consulta: ")
url = "https://viacep.com.br/ws/" + cep + "/json/"

resposta = requests.get(url)
dados = resposta.json()

print(f"\nLogradouro: {dados['logradouro']}")
print(f"Cidade: {dados['localidade']}")

# OBS: o retorno da pesquisa traz várioas chaves em um JSON:
#  {
#       "cep": "01001-000",
#       "logradouro": "Praça da Sé",
#       "complemento": "lado ímpar",
#       "unidade": "",
#       "bairro": "Sé",
#       "localidade": "São Paulo",
#       "uf": "SP",
#       "estado": "São Paulo",
#       "regiao": "Sudeste",
#       "ibge": "3550308",
#       "gia": "1004",
#       "ddd": "11",
#       "siafi": "7107"
#     }

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install Pillow
# Para verificar se a instalação deu certo, digite: pip list
from PIL import Image

# IMPORTANTE: Você precisa ter uma imagem "foto.jpg" na mesma pasta do script.
img_colorida = Image.open("foto.jpg")

img_pb = img_colorida.convert('L')

img_pb.save("foto_pb.jpg")
print("Imagem convertida para preto e branco com sucesso!")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install numpy
# Para verificar se a instalação deu certo, digite: pip list
import numpy as np

notas = np.array([6.5, 8.0, 5.5, 9.0])

notas_com_bonus = notas + 0.5

print(f"Notas originais: {notas}")
print(f"Notas com bônus: {notas_com_bonus}")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pandas
# Para verificar se a instalação deu certo, digite: pip list
import pandas as pd

dados = {
    'Produto': ['Café', 'Açúcar', 'Leite'],
    'Preço': [15.90, 4.50, 5.20]
}

tabela_produtos = pd.DataFrame(dados)

print(tabela_produtos)

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pytube
# Para verificar se a instalação deu certo, digite: pip list
from pytube import YouTube

url_video = input("Cole a URL do vídeo do YouTube que deseja baixar: ")

yt = YouTube(url_video)
stream = yt.streams.get_highest_resolution()

print(f"Baixando o vídeo: '{yt.title}'...")
stream.download()
print("Download concluído com sucesso!")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install SpeechRecognition PyAudio
# Para verificar se a instalação deu certo, digite: pip list
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Ajustando para o ruído ambiente...")
    r.adjust_for_ambient_noise(source)
    print("Pode falar! Estou ouvindo...")

    audio = r.listen(source)

    texto = r.recognize_google(audio, language='pt-BR')
    print(f"Você disse: {texto}")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install matplotlib
# Para verificar se a instalação deu certo, digite: pip list
import matplotlib.pyplot as plt

votos = [50, 25, 15, 10]
sabores = ['Chocolate', 'Morango', 'Baunilha', 'Creme']

plt.pie(votos, labels=sabores, autopct='%1.1f%%')
plt.title('Preferência de Sabores de Sorvete')
plt.show()

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pandas
# Para verificar se a instalação deu certo, digite: pip list
import pandas as pd

dados = {
    'Aluno': ['Ana', 'Beto', 'Carla', 'Daniel'],
    'Nota': [9.5, 6.0, 8.0, 5.5]
}
df = pd.DataFrame(dados)

aprovados = df[df['Nota'] >= 7]

print("--- Alunos Aprovados ---")
print(aprovados)

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install pygame
# Para verificar se a instalação deu certo, digite: pip list
import pygame

pygame.init()

LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Minha Janela Pygame")

AZUL = (0, 0, 255)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    TELA.fill(AZUL)
    pygame.display.flip()

pygame.quit()

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install face_recognition
# Para verificar se a instalação deu certo, digite: pip list
import face_recognition

# IMPORTANTE: Você precisa ter uma imagem "grupo.jpg" na mesma pasta.
imagem = face_recognition.load_image_file("grupo.jpg")
locais_dos_rostos = face_recognition.face_locations(imagem)

num_rostos = len(locais_dos_rostos)

print(f"Foram encontrados {num_rostos} rostos na imagem.")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install requests
# Para verificar se a instalação deu certo, digite: pip list
import requests

valor_usd = float(input("Digite o valor em Dólares (USD) para converter: "))

url = "https://api.exchangerate-api.com/v4/latest/USD"
resposta = requests.get(url)
dados = resposta.json()

taxa_brl = dados['rates']['BRL']
taxa_eur = dados['rates']['EUR']

valor_brl = valor_usd * taxa_brl
valor_eur = valor_usd * taxa_eur

print(f"\nUS$ {valor_usd:.2f} equivale a R$ {valor_brl:.2f}")
print(f"US$ {valor_usd:.2f} equivale a € {valor_eur:.2f}")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install requests beautifulsoup4
# Para verificar se a instalação deu certo, digite: pip list
import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"

resposta = requests.get(url)
soup = BeautifulSoup(resposta.content, 'html.parser')

# A classe pode mudar, inspecione o site para encontrar a correta
manchetes = soup.find_all('a', class_='feed-post-link')

print("--- 5 Primeiras Manchetes do G1 ---")
for i, manchete in enumerate(manchetes[:5]):
    print(f"{i+1}: {manchete.get_text().strip()}")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install qrcode[pil]
# Para verificar se a instalação deu certo, digite: pip list
import qrcode

link = input("Digite o link ou texto para gerar o QR Code: ")

img = qrcode.make(link)
img.save("meu_qrcode.png")

print("QR Code salvo como 'meu_qrcode.png' com sucesso!")

# Para usar esta biblioteca, primeiro instale-a no seu terminal:
# pip install textblob
# Para verificar se a instalação deu certo, digite: pip list
# Após a instalação, execute este comando para baixar os dados necessários:
# python -m textblob.download_corpora
from textblob import TextBlob

frase = input("Digite uma frase em inglês para análise: ")

blob = TextBlob(frase)
polaridade = blob.sentiment.polarity

print(f"\nPolaridade do sentimento: {polaridade:.2f}")

if polaridade > 0.1:
    print("Sentimento: Positivo")
elif polaridade < -0.1:
    print("Sentimento: Negativo")
else:
    print("Sentimento: Neutro")


numeros = [15, 8, 23, 42, 4, 16]

maior = max(numeros)
menor = min(numeros)

print(f"Dada a lista {numeros}:")
print(f"O maior número é {maior}.")
print(f"O menor número é {menor}.")

# Definindo a função
def saudacao():
    print("Olá, mundo!")
    print("Seja bem-vindo(a) ao Python!")

# Chamando a função
print("Primeira saudação:")
saudacao()

print("\nSegunda saudação:")
saudacao()

def mostrar_tabuada_do_7():
    print("--- Tabuada do 7 ---")
    for i in range(1, 11):
        print(f"7 x {i} = {7 * i}")

# Chama a função para executar a tarefa
mostrar_tabuada_do_7()

import random

def rolar_dado():
    # Sorteia um número inteiro entre 1 e 6 (inclusive)
    resultado = random.randint(1, 6)
    print(f"O dado rolou e o resultado foi: {resultado}")

# Rola o dado 3 vezes
rolar_dado()
rolar_dado()
rolar_dado()

import math

def calcular_potencia():
    # math.pow(base, expoente)
    resultado = math.pow(2, 10)
    print(f"2 elevado a 10 é igual a {resultado}.")

calcular_potencia()

def dobro(numero):
    return numero * 2

# Testando a função
resultado = dobro(15)
print(f"O dobro de 15 é {resultado}.")

def apresentacao(nome, idade):
    print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# Testando a função
apresentacao("Júlia", 22)
apresentacao("Marcos", 35)

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

# Testando a função
media_final = calcular_media(8.0, 9.5)
print(f"A média é: {media_final}")

def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
        
# Testando a função
print(f"O número 10 é par? {e_par(10)}")
print(f"O número 7 é par? {e_par(7)}")

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

# Testando a função
resultado = maior_numero(100, 50)
print(f"O maior número entre 100 e 50 é {resultado}.")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Coletando dados do usuário e chamando a função
peso_usuario = float(input("Digite seu peso (kg): "))
altura_usuario = float(input("Digite sua altura (m): "))

imc_resultado = calcular_imc(peso_usuario, altura_usuario)
print(f"Seu IMC é: {imc_resultado:.2f}")

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

# Testando a função
frase = "Python é uma linguagem fantástica"
total_vogais = contar_vogais(frase)
print(f"A frase '{frase}' tem {total_vogais} vogais.")

def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    novo_preco = preco - desconto
    return novo_preco

# Testando a função
preco_produto = 250.00
preco_com_desconto = aplicar_desconto(preco_produto, 15) # 15% de desconto
print(f"O preço original era R$ {preco_produto:.2f}.")
print(f"Com 15% de desconto, o preço final é R$ {preco_com_desconto:.2f}.")

def inverter_string(texto):
    texto_invertido = ""
    for letra in texto:
        texto_invertido = letra + texto_invertido
    return texto_invertido

# Testando a função
original = "programar"
invertida = inverter_string(original)
print(f"A palavra '{original}' invertida é '{invertida}'.")

def encontrar_maior(lista_numeros):
    # Começamos assumindo que o primeiro número é o maior
    maior = lista_numeros[0]
    # Percorremos o resto da lista para comparar
    for numero in lista_numeros:
        if numero > maior:
            maior = numero
    return maior

# Testando a função
numeros = [5, 29, 12, 99, 3, 50]
maior_valor = encontrar_maior(numeros)
print(f"Na lista {numeros}, o maior valor é {maior_valor}.")

def e_palindromo(texto):
    # Remove espaços e converte para minúsculas para uma comparação justa
    texto_tratado = texto.replace(" ", "").lower()
    
    # Inverte o texto tratado
    texto_invertido = ""
    for letra in texto_tratado:
        texto_invertido = letra + texto_invertido
        
    # Retorna o resultado da comparação
    return texto_tratado == texto_invertido

# Testando a função
print(f"'arara' é um palíndromo? {e_palindromo('arara')}")
print(f"'python' é um palíndromo? {e_palindromo('python')}")
print(f"'Anotaram a data da maratona' é um palíndromo? {e_palindromo('Anotaram a data da maratona')}")

def fatorial(numero):
    if numero < 0:
        return "Não existe fatorial de número negativo"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado = resultado * i
        return resultado

# Testando a função
print(f"O fatorial de 5 é {fatorial(5)}.")
print(f"O fatorial de 0 é {fatorial(0)}.")

def e_primo(numero):
    # Números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    # Verificamos divisores de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False # Se encontrar um divisor, não é primo
    return True # Se o loop terminar sem encontrar divisores, é primo

# Testando a função
print(f"O número 17 é primo? {e_primo(17)}")
print(f"O número 15 é primo? {e_primo(15)}")

def filtrar_pares(lista_original):
    lista_de_pares = []
    for numero in lista_original:
        if numero % 2 == 0:
            lista_de_pares.append(numero)
    return lista_de_pares

# Testando a função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)
print(f"A lista original é {numeros}.")
print(f"A lista apenas com números pares é {pares}.")

def validar_senha(senha):
    tem_pelo_menos_8_chars = len(senha) >= 8
    tem_maiuscula = False
    tem_numero = False

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        if char.isdigit():
            tem_numero = True
            
    # A senha é válida se todas as condições forem verdadeiras
    if tem_pelo_menos_8_chars and tem_maiuscula and tem_numero:
        return True
    else:
        return False

# Testando a função
print(f"'Senha123' é uma senha válida? {validar_senha('Senha123')}")
print(f"'senhafraca' é uma senha válida? {validar_senha('senhafraca')}")
print(f"'SENHA' é uma senha válida? {validar_senha('SENHA')}")

# Arquivo: programa_principal.py
import saudacoes

print("--- Testando meu módulo de saudações ---")
saudacoes.bom_dia()
saudacoes.boa_noite()

# Arquivo: programa_principal.py
import matematica_simples

resultado_multi = matematica_simples.multiplicar(10, 5)
resultado_div = matematica_simples.dividir(100, 4)

print(f"Resultado da multiplicação: {resultado_multi}")
print(f"Resultado da divisão: {resultado_div}")

# Arquivo: programa_principal.py
from list_utils import encontrar_maior

meus_numeros = [10, 88, 43, 2, 99, 54]
maior_numero = encontrar_maior(meus_numeros)
print(f"O maior número na lista {meus_numeros} é {maior_numero}.")

# Arquivo: programa_principal.py
import saudacoes as sd # 'sd' agora é o apelido de 'saudacoes'

print("Testando o módulo com apelido:")
sd.bom_dia()
sd.boa_noite()

# Arquivo: programa_principal.py
import texto_utils

frase = input("Digite uma frase: ")
vogais = texto_utils.contar_vogais(frase)
invertida = texto_utils.inverter_string(frase)

print(f"\nA sua frase tem {vogais} vogais.")
print(f"A sua frase invertida é: {invertida}")

# Arquivo: programa_principal.py
import geometria

area_c = geometria.area_circulo(5)
area_r = geometria.area_retangulo(10, 8)

print(f"A área de um círculo de raio 5 é {area_c:.2f}.")
print(f"A área de um retângulo 10x8 é {area_r}.")

# Arquivo: programa_principal.py
from validadores import e_email_valido

email_digitado = input("Digite seu email: ")
if e_email_valido(email_digitado):
    print("O formato do email parece válido.")
else:
    print("O formato do email é inválido.")

    # Arquivo: programa_principal.py
import geometria
import texto_utils

print("--- Testando Múltiplas Importações ---")

# Usando uma função do módulo de geometria
raio_circulo = 10
area = geometria.area_circulo(raio_circulo)
print(f"A área de um círculo de raio {raio_circulo} é {area:.2f}.")

# Usando uma função do módulo de texto
frase = "Módulos são úteis"
frase_invertida = texto_utils.inverter_string(frase)
print(f"A frase '{frase}' invertida é '{frase_invertida}'.")

# Arquivo: programa_principal.py
import operacoes

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")

if op == '+':
    resultado = operacoes.somar(num1, num2)
elif op == '-':
    resultado = operacoes.subtrair(num1, num2)
elif op == '*':
    resultado = operacoes.multiplicar(num1, num2)
elif op == '/':
    resultado = operacoes.dividir(num1, num2)
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")