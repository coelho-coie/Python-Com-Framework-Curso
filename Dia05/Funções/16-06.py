def verificar_par(numero: int) -> bool:
    status = (numero % 2 == 0)
    return status

print(f"O número 10 é par? {verificar_par(10)}")