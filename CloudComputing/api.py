#importando o modulo flask para criar uma aplicação web
import flask
from flask import request, jsonify

hoteis = [
    {"id":0,
    "nome":"Disney's All Star Sports",
    "categoria": "value"
    },{
    "id":1,
    "nome":"Disney's all-star music",
    "categoria":"value"
    },{
    "id":2,"nome":"Disney's all-star Movies",
    "categoria":"value"
    }
    ]


#criando a aplicação(um objeto do tipo flask) e setando como debug para que se acontecerem erros, eles apareçam no navegador
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#indicando uma rota(um caminho na url da nossa api) e qual metodo deve ser disparado quando ela for acessad
@app.route("/", methods=["GET"])
def home():
    #esse metodo retorna um html
    return "<h1>Oi digo sou desenvolvedor</h1><p>texto maneiro</p>"

@app.route("/api/v1/hoteis", methods=["GET"])
def api():
    #verificamos se o argumento id foi passado na hora do request
    if 'id' in request.args:
        #caso tenha sido, armazenamos em uma variavel
        id = int(request.args['id'])
    elif 'nome' in request.args:
        #no caso de armazenar um nome
        nome = int(request.args['nome'])
    else:
        #caso nao tenha sido passado id, retornamos um erro
        return "Erro: nenhum id foi informado. Por favor, especifique esse dado!"
    #criando os resultados, ainda em branco
    resultados = []
    #para cada hotel, vamos verificar o id e caso seja igual, anexamos o resultado
    for hotel in hoteis:
        if hotel['id'] == id:
            resultados.append(hotel)

        return jsonify(resultados)


#def api_all():
#  return jsonify(hoteis)

app.run()
