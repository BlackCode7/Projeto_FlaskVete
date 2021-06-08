from flask import Blueprint, request, Response
from flask_restful.representations import json
from flask_restx import Namespace, Resource, fields

from dtos.UsuarioDTO import ErroDTO

login_controller = Blueprint('login_controller', __name__)
api = Namespace('Login', description='Realizar login na Aplicação')
# trazendo os dados do banco para fazer o filtro
login_fields = api.model('LoginDTO', {
    'login': fields.String,
    'senha': fields.String
})


@api.route('/login', methods=['POST'])
class Login(Resource):
    """Tudo que for referente a rota /login o swagger ja implementa a documentação aqui"""
    @api.doc(response={200: 'Login realizado com sucesso!'})
    @api.doc(response={400: 'Parâmetros de entrada inválidos!'})
    @api.doc(response={500: 'Não foi possível efetuar o login, tente novamente!'})
    @api.expect(login_fields)
    def post(self):
        try:
            body = request.get_json()
            if not body or "login" not in body or "senha" not in body:
                return Response(json.dumps(ErroDTO("Parâmetros de entrada inválidos", 400).__dict__), status=400, mimetype='application/json')

            return Response("login autenticado com sucesso",status=200, mimetype='application/json')

        except Exception as e:
            return Response(json.dumps(ErroDTO("Não foi possível efetuar o login, tente novamente", 500).__dict__), status=500, mimetype='application/json')