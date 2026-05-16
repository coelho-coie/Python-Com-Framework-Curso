from os import system as lt
lt("cls")

x = "Seu nome é\t\t"+ input("Qual teu nome? ")
x += "\nSeu número é\t\t" + input("Qual teu telefone? ")
x += "\nSeu cpf é\t\t" + input("Qual teu cpf? ")
x += "\nSua data de nacimento é\t" + input("Qual teu data de nacimento? ")

print(f"\n{x}")
