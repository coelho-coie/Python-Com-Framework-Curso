def cadastrar_maquina(nome: str, **especificacoes):
    print(f"Cadastrando Máquina: {nome}")
    # '**especificacoes' vira um dicionário com chave e valor
    for item, valor in especificacoes.items():
        print(f"--- Detalhe Técnico: {item} -> {valor}")

cadastrar_maquina("Torno CNC", voltagem="220V", motor="10CV", sensor="Laser")