def buscar_pares(limite: int):
    for n in range(limite + 1):
        # Se for par, entregamos (yield) e pausamos a função
        if n % 2 == 0:
            yield n

for par in buscar_pares(10):
    print(f"Número par: {par}")