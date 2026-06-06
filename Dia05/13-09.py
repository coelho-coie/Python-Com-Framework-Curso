# O int() converte o texto digitado pelo usuário em um número.
numero_texto = input("Digite um número para gerar a tabuada: ")
numero = int(numero_texto)
    
with open("tabuada.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"--- Tabuada do {numero} ---\n")
    for i in range(1, 11):
        resultado = numero * i
        arquivo.write(f"{numero} x {i} = {resultado}\n")
            
print(f"Tabuada do {numero} salva em 'tabuada.txt'.")