from datetime import datetime

entrada_usuario = input("Digite sua nova entrada no diário:\n")

# Pega a data e hora atuais
agora = datetime.now()

# Formata a data e hora para um formato simples
timestamp = agora.strftime("%d/%m/%Y %H:%M") # Ex: 16/10/2025 14:30

linha_diario = f"[{timestamp}] - {entrada_usuario}\n"

with open("diario_datado.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(linha_diario)

print("Sua entrada foi registrada com data e hora!")