def gerar_ids():
    # yield entrega o valor e 'pausa' a função até ser chamado de novo
    yield 1
    yield 2
    yield 3

# O loop 'for' pede o próximo valor para o gerador a cada volta
for codigo in gerar_ids():
    print(f"ID Gerado: {codigo}")