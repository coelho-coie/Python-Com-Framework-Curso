def monitorar_pressao():
    p = 1.0
    while p <= 5.0:
        # Entrega a leitura e aguarda
        yield f"Pressão atual: {p:.1f} bar"
        p = p + 0.5
    yield "LIMITE ATINGIDO: Desligando válvulas!"

# O loop simula o tempo real de monitoramento
for status in monitorar_pressao():
    print(status)