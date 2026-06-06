# Arquivo: texto_utils.py
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

def inverter_string(texto):
    # Fatiamento de string com passo -1 é um atalho para inverter
    return texto[::-1]