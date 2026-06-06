import os
import shutil

# Cria as pastas de destino, se não existirem
if not os.path.exists("Imagens"):
    os.mkdir("Imagens")
if not os.path.exists("Documentos"):
    os.mkdir("Documentos")

# Organiza os arquivos
for arquivo in os.listdir('.'):
    if os.path.isfile(arquivo):
        if arquivo.endswith(".jpg") or arquivo.endswith(".png"):
            shutil.move(arquivo, "Imagens")
            print(f"Movendo '{arquivo}' para 'Imagens'")
        elif arquivo.endswith(".txt") or arquivo.endswith(".pdf"):
            shutil.move(arquivo, "Documentos")
            print(f"Movendo '{arquivo}' para 'Documentos'")

print("\nOrganização concluída!")