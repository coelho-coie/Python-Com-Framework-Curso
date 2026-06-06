import os
import shutil
from datetime import datetime

arquivo_original = "dados.csv" # Crie este arquivo para teste
pasta_backup = "backups"

if not os.path.exists(pasta_backup):
    os.mkdir(pasta_backup)

if os.path.exists(arquivo_original):
    hoje = datetime.now().strftime("%Y-%m-%d") # Formato AAAA-MM-DD
    
    # Monta o nome final do backup: "dados_2025-10-16.csv"
    nome_backup = f"dados_{hoje}.csv"
    caminho_destino = os.path.join(pasta_backup, nome_backup)
    
    shutil.copy(arquivo_original, caminho_destino)
    print(f"Backup com data criado: '{caminho_destino}'")
else:
    print(f"Erro: Arquivo '{arquivo_original}' não encontrado.")