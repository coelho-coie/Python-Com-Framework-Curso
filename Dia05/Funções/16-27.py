import datetime

def log_horario(funcao_alvo):
    # Usamos *args e **kwargs para que o decorador aceite qualquer função
    def envelope(*args, **kwargs):
        agora = datetime.datetime.now()
        print(f"[SISTEMA]: Executando '{funcao_alvo.__name__}' em {agora}")
        res = funcao_alvo(*args, **kwargs)
        return res
    return envelope

@log_horario
def tarefa_do_operador():
    print("Atualizando banco de dados...")

tarefa_do_operador()