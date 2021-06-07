
from flask_sqlalchemy import SQLAlchemy

import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/veterinariaDB'
db = SQLAlchemy(app)


class VeterinariaDB(db.Model):
    __tablename__ = "tabela_login"
    idlogin = db.Column('idlogin', db.Integer, primary_key=True)
    usuariologin = db.Column(db.String(100), nullable=False)
    senhalogin = db.Column(db.String(100), nullable=False)
    perfilusuario = db.Column(db.String(100), nullable=False)

    def __init__(self, idlogin, usuariologin, senhalogin, perfilusuario):
        self.idlogin = idlogin
        self.usuariologin = usuariologin
        self.senhalogin = senhalogin
        self.perfilusuario = perfilusuario

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
