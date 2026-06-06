def calcular_media(*notas: float) -> float:
    # '*notas' transforma todos os números recebidos em uma tupla interna
    soma_total = sum(notas)
    quantidade = len(notas)
    res = soma_total / quantidade
    return res

print(f"Média: {calcular_media(7, 8, 9.5, 10)}")