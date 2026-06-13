# Um dicionário com dados mais realistas e interessantes
capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "Reino Unido": "Londres",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Itália": "Roma",
    "Japão": "Tóquio",
    "China": "Pequim",
    "Rússia": "Moscou",
    "Austrália": "Canberra"
}

# Pedimos a entrada do usuário
pais_digitado = input("Digite o nome de um país para saber sua capital: ")

try:
    # TENTAMOS acessar o dicionário usando a entrada do usuário como chave.
    # Se a chave (o país) não existir, esta linha vai gerar um erro (KeyError).
    capital = capitais[pais_digitado]
    
    # Se a linha acima funcionou, o código continua e mostra a capital.
    print(f"A capital de {pais_digitado} é {capital}.")

except KeyError:
    # Se o acesso no bloco 'try' falhou, o programa pula para este bloco.
    # Ele executa o código aqui dentro em vez de quebrar.
    print(f"Desculpe, o país '{pais_digitado}' não está em nossa lista.")