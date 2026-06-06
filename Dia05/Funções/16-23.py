def filtrar_erros(total_linhas: int):
    for i in range(total_linhas):
        # Simulamos que apenas algumas linhas são erros reais
        if i % 100 == 0:
            yield f"Registro {i}: Falha detectada!"

# O generator processa as linhas uma por uma, sem ocupar memória RAM extra
for log in filtrar_erros(1000):
    print(f"[LOG]: {log}")