import os

print("Procurando por pastas vazias...")

for item in os.listdir('.'):
    if os.path.isdir(item):
        # Se a lista de conteúdo da pasta está vazia, ela não tem nada dentro.
        if not os.listdir(item):
            os.rmdir(item) # rmdir = remove directory
            print(f" - A pasta vazia '{item}' foi removida.")
            
print("Verificação concluída.")