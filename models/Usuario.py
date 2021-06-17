from sqlalchemy import Column, Integer, String, engine, inspect
from database.DataBase import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(200))

if not inspect(engine).has_table('usuario', schema=config.MYSQL_DATABASE)
    Usuario.__tablename__.create(engine)

