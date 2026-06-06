nome = input("Nome do contato: ")
telefone = input("Telefone do contato: ")

# Montamos a linha no formato CSV (Valores Separados por Vírgula)
linha_csv = f"{nome},{telefone}\n"

# Usamos 'a' para adicionar o novo contato sem apagar os existentes.
with open("contatos.csv", "a", encoding="utf-8") as arquivo:
    arquivo.write(linha_csv)

print("Contato adicionado com sucesso!")