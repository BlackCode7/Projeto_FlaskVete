import datetime

import jwt

# criar 2 metodos
from flask import config


def gerar_token(id_usuario):
    try:
        payload = {
            'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=3, minutes=3),
            'id_usuario': id_usuario
        }

        return jwt.encode(
            payload,
            config.SECRET_KEY,
            algorithm="HS256"
        )
    except Exception:
        raise Exception


def decodifar_token(token):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        return payload['id_usuario']

    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError

