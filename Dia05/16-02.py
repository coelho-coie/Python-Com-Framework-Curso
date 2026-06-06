def registrar_colaborador(nome: str, setor: str):
    """Realiza registro do coloborador da empresa junto com setor

    :param nome: Nome do colaborador
    :type nome: str
    :param setor: Setor que o colaborador trabalha
    :type setor: str
    """
    print(f"Colaborador {nome} alocado no setor {setor}.")

registrar_colaborador(nome="Carlos Silva", setor="Automação")
