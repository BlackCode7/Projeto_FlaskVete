from sqlalchemy import Column, Integer, String, engine, inspect
import config
from database.DataBase import Base


class Usuario(Base):
    __tablename__ = 'tb_usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(100))

# Validação pra ver se a tabela existe no banco
if not inspect(engine).has_table('tb_usuario', schema=config.MYSQL_DATABASE):
    Usuario.__table__.create(engine)

