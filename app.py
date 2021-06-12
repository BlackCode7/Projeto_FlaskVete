from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS, cross_origin
from werkzeug.utils import redirect
# Usado para fazer a documentação da API(restx)
from flask_restx import Api
import config
from controllers.LoginController import login_controller
from controllers.LoginController import api as ns_login

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/veterinariaDB'
db = SQLAlchemy(app)

api = Api(app, version='1.0', title='Api Clínica Veterinária',
          description='Aplicação para cadastro de pets de clínica veterinária.', doc='/docs')


# modo de acessar os dados do banco postgres e outros bancos
class VeterinariaLogin(db.Model):
    __tablename__ = "tabela_login"
    id = db.Column('id', db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    perfil = db.Column(db.String(100), nullable=False)

    def __init__(self, id, usuario, senha, perfil):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.perfil = perfil

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# rota de login da aplicação
@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    data = VeterinariaLogin.query.all()
    items = []
    for item in data:
        items.append(item.as_dict())
    return jsonify(items)


# Definição de documentação
def register_blueprint():
    app.register_blueprint(login_controller, url_prefix=config.API_BASE_URL)


# Definição de documentação
def add_namespace():
    api.add_namespace(ns_login, path=config.API_BASE_URL)


if __name__ == "__main__":
    #api.base_url(config.API_BASE_URL)#4
    register_blueprint()#3
    add_namespace()#2
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)#1


"""
####################################
@app.route('/login_post', methods=['POST'])
@cross_origin()
def login_post(self, methods):
    if self.methods == "POST":
        data = VeterinariaLogin.query.all()
        db.session.add(data)
        db.session.commit()
        db.session.save()
    else:
        if methods == 'GET':
            redirect('/login')
    return jsonify(self.methods)
####################################


class ApiPet(Resource):

    # Testando a rota get()
    def get(self, name, teste):
        #Modificar aqui por >>> return{"data":"Hello Pet"}
        #return{"Hello VeteBandeirantes"}
        return{"name": name, "teste": teste}


# Aqui o diconario pega os dados passados no url como name e teste
api.add_resource(ApiPet, "/hellopet/<string:name>/<int:teste>")

#Testando a rota post()
def post(self):
    return{"data":"testando Post"}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', method=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        pass
    pass

"""