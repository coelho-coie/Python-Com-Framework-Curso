# Pedimos o número de pessoas
pessoas_texto = input("Quantas pessoas estão na sala? ")

try:
    # Tentamos converter a entrada para um número
    numero_pessoas = int(pessoas_texto)
    
    # TENTAMOS fazer a divisão.
    # Se 'numero_pessoas' for 0, esta linha vai dar um erro (ZeroDivisionError).
    resultado = 100 / numero_pessoas
    
    # Se a divisão deu certo, mostramos o resultado.
    print(f"Cada pessoa recebe {resultado:.2f} partes.")

except:
    # Se a divisão no bloco 'try' falhou, o programa executa este bloco.
    print("Não é possível dividir por zero pessoas!")