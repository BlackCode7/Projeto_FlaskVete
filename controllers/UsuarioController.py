# Para o controler das rotas do usuario
import json

from flask import Response, config
from flask_blueprint import Blueprint
from flask_restx import Namespace, Resource, fields
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO
from utils import Decorators

usuario_controller = Blueprint('usuario_controller', __name__)
api = Namespace('Usuario')

user_fields = api.model(
    'UsuarioBaseDTo', {
        'nome':fields.String,
        'email': fields.String,
    }
)

@api.route('/', methods=['GET'])
class usuarioController(Resource):
    @api.doc(responses={200: 'Login realizado com sucesso.'})
    @api.doc(responses={401: 'Token Inválido.'})
    @api.response(200, 'Success', user_fields)
    @Decorators.token_required
    def get(self, usuario_atual):
        try:
            return Response(
                json.dumps(UsuarioBaseDTO('Admin', config.LOGIN_TESTE).__dict__),
                status=200,
                mimetype='application/json'
                )

        except Exception:
            return Response(
                json.dumps(ErroDTO("Não foi possivel efetuar o login! Tente novamente", 500).__dict__),
                status=500,
                mimetype='application/json'
                )