class UsuarioBaseDTO:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class UsuarioCreateDTO(UsuarioBaseDTO):
    def __init__(self, nome, usuario, senha):
        super().__init__(nome, usuario)
        self.senha = senha


# Conceito de herança
class UsuarioLoginDTO(UsuarioBaseDTO):
    def __init__(self, nome, email, token):
        super().__init__(nome, email)
        self.token = token