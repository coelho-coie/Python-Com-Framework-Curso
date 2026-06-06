temperaturas = [65.0, 80.5, 74.2, 90.0, 30.5, 115.0]

# filter() aplica a lambda em cada item da lista e mantém apenas os True
alerta = list(filter(lambda t: t > 75.0, temperaturas))

print(f"Temperaturas em zona de risco: {alerta}")