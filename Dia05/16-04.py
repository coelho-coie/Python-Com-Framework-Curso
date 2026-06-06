
# Obriga a variavel ser chamada lado
def calcular_area_quadrado(*, lado: float) -> float:
    res = lado * lado
    return res

print(f"Área: {calcular_area_quadrado(lado=4.0)}")
