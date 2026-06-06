import os

pasta_principal = "projeto"
subpastas = ["dados", "imagens"]

# Cria a pasta principal
if not os.path.exists(pasta_principal):
    os.mkdir(pasta_principal)

# Cria as subpastas
for pasta in subpastas:
    # Junta os nomes para criar o caminho completo
    caminho_completo = os.path.join(pasta_principal, pasta)
    if not os.path.exists(caminho_completo):
        os.mkdir(caminho_completo)

print(f"Estrutura do projeto '{pasta_principal}' criada!")