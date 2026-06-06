# O '*' força a chamada nomeada para evitar confusão entre os textos
def conectar_banco(*, servidor: str, usuario: str, senha: str):
    res = f"Banco em '{servidor}' acessado pelo usuário '{usuario}'."
    return res

print(conectar_banco(servidor="192.168.1.10", usuario="root", senha="123"))