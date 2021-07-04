import uuid
from flask import Flask, jsonify, request,Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import mysql.connector
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# Connection credentials

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://renanmeneses:cmVuYW5tZW5l@jobs.visie.com.br/renanmeneses'

db = SQLAlchemy(app)

class Pessoas(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    rg = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date())
    data_admissao = db.Column(db.Date())
    
    def __init__(self, id_pessoa, nome, rg, cpf, data_nascimento, data_admissao ):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
    def to_json(self):
        return{
        "id_pessoa" : self.id_pessoa,
        "nome" : self.nome,
        "rg" : self.rg,
        "cpf" : self.cpf,
        "data_nascimento" : self.data_nascimento,
        "data_admissao" : self.data_admissao
        }
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_pessoa(pessoa_id):
    for pessoa in Pessoas:
        if pessoa['id'] == pessoa_id:
            Pessoas.remove(pessoa)
            return True
    return False


@app.route('/pessoas', methods=['GET', 'POST'])
def all_Pessoas():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        pessoa = Pessoas(
        id_pessoa= uuid.uuid4().hex,
        nome= post_data.get('nome'),
        rg= post_data.get('rg'),
        cpf= post_data.get('cpf'),
        data_nascimento= post_data.get('data_nascimento'),
        data_admissao= post_data.get('data_admissao'))
        db.session.add(pessoa)
        db.session.commit()
        response_object['message'] = 'pessoa added!'

        # Pessoas.append({
        #     'id_pessoa': uuid.uuid4().hex,
        #     'nome': post_data.get('nome'),
        #     'rg': post_data.get('rg'),
        #     'cpf': post_data.get('cpf'),
        #     'data_nascimento': post_data.get('data_nascimento'),
        #     'data_admissao': post_data.get('data_admissao')

        # })
        print(post_data)

    else:
        pessoas = Pessoas.query.all()
        pessoas_json = [pessoa.to_json() for pessoa in pessoas]
        response_object['pessoas'] = pessoas_json
        # response_object['pessoas'] = Pessoa

    return jsonify(response_object)


@app.route('/pessoas/<pessoa_id>', methods=['PUT', 'DELETE'])
def single_pessoa(pessoa_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        # remove_pessoa(pessoa_id)
        print(pessoa_id)
        # Pessoas.append({
        #     'id': uuid.uuid4().hex,
        #     'nome': post_data.get('nome'),
        #     'rg': post_data.get('rg'),
        #     'cpf': post_data.get('cpf'),
        #     'data_nascimento': post_data.get('data_nascimento'),
        #     'data_admissao': post_data.get('data_admissao')
        # })
        response_object['message'] = 'pessoa updated!'
    if request.method == 'DELETE':
        # remove_pessoa(pessoa_id)
        pessoa = Pessoas.query.filter_by(id_pessoa = pessoa_id).first()
        db.session.delete(pessoa)
        db.session.commit()
        response_object['message'] = 'pessoa removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True)
