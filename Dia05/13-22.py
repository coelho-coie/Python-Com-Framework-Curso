import os
import shutil

pasta_destino = "temporarios"
arquivo_a_mover = "relatorio_temp.txt"

# Crie a pasta e o arquivo antes de executar o script.
if os.path.exists(arquivo_a_mover):
    shutil.move(arquivo_a_mover, pasta_destino)
    print(f"Arquivo '{arquivo_a_mover}' movido para a pasta '{pasta_destino}'.")
else:
    print(f"Erro: Crie o arquivo '{arquivo_a_mover}' para poder movê-lo.")