from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost'

engine = create_engine(
    #Passando a url
    SQLALCHEMY_DATABASE_URI
)

# Aqui eu mando o sqlAlchemy criar a base de dados se ele não existir
engine.execute(f'CREATE DATABASE IF NOT EXISTS {config.MYSQL_DATABASE}')
engine.execute(f'USE {config.MYSQL_DATABASE}')

# objeto de session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando um objeto pra usar em outras partes do código
Base = declarative_base()