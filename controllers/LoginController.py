from flask import Blueprint, request, Response, config
from flask_restful.representations import json
from flask_restx import Namespace, Resource, fields
from dtos.ErroDTO import ErroDTO
# LoginController defini todas as rotas com a lib BluePrint() registra as rotas no main.py
# from swagger.LoginModel import login_fields
from dtos.UsuarioDTO import UsuarioLoginDTO
from services import JWTservice

login_controller = Blueprint('login_controller', __name__)
api = Namespace('Login', description='Realizar login na applicação')
login_fields = api.model('LoginDTO', {
    'login': fields.String,
    'senha': fields.String
})
user_fields = api.model('UsuárioDTO', {
    'name': fields.String,
    'email': fields.String,
    'token': fields.String
})


@api.route('/login', methods=['POST'])
class Login(Resource):
    """Tudo que for referente a rota /login o swagger ja implementa a documentação aqui"""
    @api.doc(response={200: 'Login realizado com sucesso!'})
    @api.doc(response={400: 'Parâmetros de entrada inválidos!'}, body=login_fields)
    @api.doc(response={500: 'Não foi possível efetuar o login, tente novamente!'})
    @api.response(200, 'Sucesso', user_fields)
    @api.expect(login_fields)
    def post(self):
        try:
            body = request.get_json()

            erros = []

            if not body:
                erros.append("O body da requisição não pode estar vazio!")

            if not "login" in body:
                erros.append("O campo 'login' é obrigatório. ")

            if not "senha" in body:
                erros.append("O campo 'senha' é obrigatório")

            if erros:
                return Response(
                    json.dumps(ErroDTO(400, erros).__dict__),
                    status=400,
                    imetype='application/json'
                    )

            if body["login"] == config.LOGIN_TESTE and body["senha"] == config.SENHA_TESTE:

                id_usuario = 1 # usuario mocado deve ser trocado
                token = JWTservice.gerar_token(id_usuario)
                return Response(
                    json.dumps(UsuarioLoginDTO("Admin", config.LOGIN_TESTES, token).__dict__),
                    status=200,
                    mimetype='application/json'
                    )

            return Response(
                json.dumps(ErroDTO("Usuario ou Senha incorretos! Tente novamente!", 401).__dict__),
                status=401,
                mimetype='application/json'
                )

        except Exception:
            return Response(
                json.dumps(ErroDTO("Não foi possível processar a requisição.", 500).__dict__),
                status=500,
                mimetype='application/json'
                )


