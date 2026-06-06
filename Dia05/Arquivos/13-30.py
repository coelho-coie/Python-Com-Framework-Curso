import os
import shutil
import time

pasta_logs = "Dia05/logs"
pasta_arquivo = os.path.join(pasta_logs, "logs_antigos")
DIAS_LIMITE = 7
SEGUNDOS_LIMITE = DIAS_LIMITE * 24 * 60 * 60

os.makedirs(pasta_arquivo, exist_ok=True)

agora = time.time()

print(f"Arquivando logs mais antigos que {DIAS_LIMITE} dias...")

for nome_arquivo in os.listdir(pasta_logs):
    caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)
    
    if os.path.isfile(caminho_arquivo):
        tempo_modificacao = os.path.getmtime(caminho_arquivo)
        
        if (agora - tempo_modificacao) > SEGUNDOS_LIMITE:
            shutil.move(caminho_arquivo, pasta_arquivo)
            print(f" - Arquivando log antigo: '{nome_arquivo}'")

print("Processo de arquivamento concluído.")