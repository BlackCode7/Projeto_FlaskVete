from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/veterinariaDB'
db = SQLAlchemy(app)
api = Api(app)
CORS(app)


class VeterinariaLogin(db.Model):
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


@app.route('/login')
@cross_origin()
def login():
    items = []
    for item in VeterinariaLogin.query.all():
        items.append(item.as_dict())
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True)


"""
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