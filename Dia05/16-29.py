def limpar(t: str) -> str: return t.strip() # Remove espaços
def maiusculo(t: str) -> str: return t.upper() # Fica tudo maiúsculo
def finalizar(t: str) -> str: return t + " [OK]" # Adiciona sufixo

def processar_texto(bruto: str) -> str:
    # Cada linha utiliza o resultado da anterior (Pipeline)
    t1 = limpar(bruto)
    t2 = maiusculo(t1)
    res = finalizar(t2)
    return res

print(processar_texto("    sistema de segurança    "))