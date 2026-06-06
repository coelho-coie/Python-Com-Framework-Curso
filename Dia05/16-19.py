def calcular_icms(valor: float) -> float:
    res = valor * 0.18
    return res

def calcular_preco_venda(custo: float) -> float:    
    imposto = calcular_icms(custo)
    res = custo + imposto
    return res

print(f"Custo 100 -> Venda com ICMS: R$ {calcular_preco_venda(100.0)}")