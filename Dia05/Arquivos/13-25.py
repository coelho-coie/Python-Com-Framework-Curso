import os

pasta_para_limpar = "lixeira"

# Crie a pasta 'lixeira' com alguns arquivos para testar.
if os.path.exists(pasta_para_limpar):
    print(f"Limpando a pasta '{pasta_para_limpar}'...")
    for nome_arquivo in os.listdir(pasta_para_limpar):
        caminho_arquivo = os.path.join(pasta_para_limpar, nome_arquivo)
        os.remove(caminho_arquivo)
        print(f" - Arquivo '{nome_arquivo}' removido.")
    print("Limpeza concluída.")
else:
    print(f"Erro: A pasta '{pasta_para_limpar}' não foi encontrada.")