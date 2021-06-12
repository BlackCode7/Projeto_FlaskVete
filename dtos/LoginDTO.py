class LoginDTO:
    def __init__(self, id, senha, usuario):
        # OBS no video o dado representado é o login, mas aqui na minha aplicação
        # Eu estou usando o dado com o nome de usuario pq no banco esta assim!
        self.login = usuario
        self.senha = senha