import os
import shutil

pasta_origem = "Dia05/origem"
pasta_destino = "Dia05/destino"

# Garante que as pastas existem
os.makedirs(pasta_origem, exist_ok=True)
os.makedirs(pasta_destino, exist_ok=True)

arquivos_origem = os.listdir(pasta_origem)
arquivos_destino = os.listdir(pasta_destino)

for arquivo in arquivos_origem:
    if arquivo not in arquivos_destino:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        shutil.copy(caminho_origem, pasta_destino)
        print(f" - Copiando '{arquivo}' para '{pasta_destino}'")
    
print("Sincronização concluída.")