def validar_positivo(funcao_orig):
    # O envelope agora precisa aceitar o 'valor' que será passado à função
    def envelope(valor):
        if valor < 0:
            print("[ALERTA]: O sistema não aceita valores negativos!")
        else:
            # Se for positivo, a função original segue normalmente
            res = funcao_orig(valor)
            return res
    return envelope

@validar_positivo
def definir_pressao(p: float):
    print(f"Pressão ajustada para {p} bar.")

definir_pressao(10.5)
definir_pressao(-2.0) # Aciona o alerta do decorador