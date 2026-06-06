
def converter_celsius(celsius: float) -> float:
    """Converte o valores de celsius em fahrenheit

    Args:
        celsius (float): Recebe o valor em celsius

    Returns:
        float: Retorna o valor em fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

res = converter_celsius(25.0)
print(f"Resultado: {res}°F")
