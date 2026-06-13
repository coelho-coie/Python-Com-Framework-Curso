class Usuario:
    def __init__(self, user, senha):
        self.username = user
        self.senha = senha

    def alterar_senha(self, antiga, nova):
        if antiga == self.senha:
            self.senha = nova
            print("Senha alterada!")
        else:
            print("Senha antiga incorreta.")

perfil = Usuario("admin", "1234")
perfil.alterar_senha("1234", "abcd")