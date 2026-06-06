def divisao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        res = "Valores dever ser int ou float"
    else:
        res = a/ b
    return res

print(f"Dividindo 10 por 2: {divisao(10, 2)}")
print(f"Dividindo 10 por 'A': {divisao(10, 'A')}")
print()