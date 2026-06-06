def soma_recursiva(lista: list) -> float:
    # CASO DE PARADA: Se a lista estiver vazia, a soma é 0
    if not lista:
        res = 0
    else:
        res = lista[0] + soma_recursiva(lista[1:])
    return res

print(f"Soma total: {soma_recursiva([5, 10, 15])}")