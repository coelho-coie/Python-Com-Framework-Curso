def saudar_cidade(cidade: str) -> str:
    """Saudação para entrar na cidade

    :param cidade: Qual a cidade
    :type cidade: str
    :return: Retorna a saudação
    :rtype: str
    """
    mensagem = f"Bem-vindo à cidade de {cidade}!"
    return mensagem

print(saudar_cidade("Sertãozinho"))