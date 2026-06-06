def fibonacci(n: int) -> int:
    # CASO DE PARADA: Os termos 0 e 1 retornam eles mesmos
    if n <= 1:
        res = n
    else:
        # A sequência é a soma dos dois termos anteriores (n-1 + n-2)
        res = fibonacci(n - 1) + fibonacci(n - 2)
    return res

print(f"O 7º termo da sequência de Fibonacci é: {fibonacci(7)}")