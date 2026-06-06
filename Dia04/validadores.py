# Arquivo: validadores.py
def e_email_valido(email):
    # Verificação simples: checa se '@' e '.' existem na string
    if "@" in email and "." in email:
        return True
    else:
        return False