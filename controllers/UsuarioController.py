# Para o controler das rotas do usuario
import json
from flask import Response, config, request
from flask_blueprint import Blueprint
from flask_restx import Namespace, Resource, fields
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO, UsuarioCreateDTO
from services.UsuarioService import UsuarioService
from services.UsuarioService import UsuarioService
from utils import Decorators
from utils.Criptografia import criptografar_senha

usuario_controller = Blueprint('usuario_controller', __name__)
api = Namespace('Usuario')

user_fields = api.model(
    'UsuarioBaseDTo', {
        'nome': fields.String,
        'email': fields.String,
    }
)


@api.route('/', methods=['GET'])
class usuarioController(Resource):
    @api.doc(responses={200: 'Login realizado com sucesso.'})
    @api.doc(responses={401: 'Token Inválido.'})
    @api.response(200, 'Success', user_fields)
    @Decorators.token_required
    def get(usuario):
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

    def post(self):
        try:
            # criações no servidor
            body = request.get_json()

            erros = []

            if not body:
                return Response(
                    json.dumps(ErroDTO(400, 'Body da requisição esta vazio').__dict__),
                    status=400,
                    mimetype='application/json'
                )

            if not "nome" in body:
                erros.append("Campo 'nome' é obrigatório")

            if not "senha" in body:
                erros.append("Campo 'senha' é obrigatório")

            if not "email" in body:
                erros.append("Campo 'email' é obrigatório")

            if erros:
                return Response(
                    json.dumps(ErroDTO(400, erros).__dict__),
                    status=400,
                    imetype='application/json'
                )

            usuario_criado = UsuarioService().criar_usuario(body["nome"],
                                           body["email"],
                                           criptografar_senha(body["senha"]))

            # Validadno usuario criado
            if not usuario_criado:
                return Response(
                    json.dumps(ErroDTO(400, 'E-mail já cadastrado no sistema.').__dict__),
                    status=400,
                    mimetype='application/json'
                )

            return Response(
                json.dumps(UsuarioCreateDTO(usuario_criado.id,
                                            usuario_criado.nome,
                                            usuario_criado.email,
                                            usuario_criado.senha).__dict__),
                                            status=201,
                                            mimetype='application/json'
            )

        except Exception:

            return Response(
                json.dumps(ErroDTO("Não foi possivel efetuar o login! Tente novamente", 500).__dict__),
                status=500,
                mimetype='application/json'
            )