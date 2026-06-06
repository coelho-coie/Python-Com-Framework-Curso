def aplicar_cupons(preco: float, **cupons) -> float:
    # Começamos com o preço original e vamos abatendo os descontos
    valor_atualizado = preco
    for nome, porcentagem in cupons.items():
        print(f"Aplicando desconto: {nome} (-{porcentagem}%)")
        abatimento = valor_atualizado * (porcentagem / 100)
        valor_atualizado = valor_atualizado - abatimento
    return valor_atualizado

final = aplicar_cupons(1000.0, Natal=10, Fidelidade=5, PrimeiraCompra=2)
print(f"Valor Final: R$ {final:.2f}")