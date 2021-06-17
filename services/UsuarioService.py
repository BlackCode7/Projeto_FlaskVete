from database.DataBase import SessionLocal
from utils.Criptografia import verificar_senha

db = sessionLocal()

class UsuarioService:
    def __init__(self):
        pass


    def login(self, email, senha):
        usuario = db.query(Usuario).filter(Usuario.email == email).first()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha)
