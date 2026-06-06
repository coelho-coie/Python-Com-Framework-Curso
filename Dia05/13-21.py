import os
import shutil

arquivo_original = input("Qual arquivo você quer copiar? ")
nome_da_copia = "copia_seguranca.txt"

if os.path.exists(arquivo_original):
    shutil.copy(arquivo_original, nome_da_copia)
    print(f"Backup de '{arquivo_original}' criado como '{nome_da_copia}'")
else:
    print(f"Erro: O arquivo '{arquivo_original}' não existe.")