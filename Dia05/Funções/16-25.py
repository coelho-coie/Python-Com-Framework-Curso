def forcar_limite(n: int):
    try:
        # A função chama a si mesma infinitamente sem parar
        return forcar_limite(n + 1)
    except RecursionError:
        # O Python interrompe e caímos neste bloco de segurança
        res = "O sistema impediu um travamento por excesso de chamadas recursivas."
        return res

print(forcar_limite(1))