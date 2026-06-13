# Nossa lista de frutas
frutas = ["Maçã", "Banana", "Laranja"]

# Mostramos as opções para o usuário
print("Escolha uma fruta pelo número:")
print("0: Maçã")
print("1: Banana")
print("2: Laranja")

try:
    # Pedimos a posição e tentamos converter para inteiro
    posicao_texto = input("Digite o número da sua escolha: ")
    posicao = int(posicao_texto)
    
    # TENTAMOS acessar a fruta na lista usando a posição digitada.
    # Se 'posicao' for 3, 4, etc., esta linha vai dar um erro (IndexError).
    fruta_escolhida = frutas[posicao]
    
    # Se deu certo, mostramos a fruta.
    print(f"Você escolheu: {fruta_escolhida}!")

except:
    # Se o acesso à lista no bloco 'try' falhou, o programa executa este bloco.
    print("Posição inválida! Escolha 0, 1 ou 2.")