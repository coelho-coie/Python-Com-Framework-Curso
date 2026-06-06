def fatorial(n: int) -> int:
    if n <= 1:
        res = 1
    else:
        res = n * fatorial(n - 1)
    return res

print(f"O fatorial de 5 é: {fatorial(5)}")