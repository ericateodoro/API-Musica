from flask import Flask, jsonify, request


app = Flask(__name__)

cancoes = [
    {"musica": "A banda", "Estilo": "Mpb"},
    {"musica": "Lego house", "Estilo": "Pop"},
    {"musica": "Sambista perfeiro", "Estilo": "Samba"},
    {"musica": "Pipa avoada", "Estilo": "Hip-hop"},
]
# GET-  http://localhost:5000/

@app.route("/cancoes/", methods=["GET"])
def consultar_cancoes():
    return jsonify(cancoes)




# Get com id - http://localhost:5000/cancoes/indice


@app.route("/cancoes/<int:indice>", methods=["GET"])
def obter_informacoes(indice):
    return jsonify(cancoes[indice])


# Inserir uma nova canção 

@app.route("/cancoes", methods=["POST"])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A cancao {cancao} foi adicionada com sucesso', 200)


# PUT Alterar uma canção


@app.route("/cancoes/<int:indice>", methods=["PUT"])
def alterar_cancao(indice):
    cancao_alterada = request.get_json()
    cancoes[indice].update(cancao_alterada)
    return jsonify(cancoes[indice], 200)

# DELETE -  Deletar uma canção


@app.route("/cancoes/<int:indice>", methods=["DELETE"])
def excluir_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify("Canção excluída com sucesso", 200)
    except:
        return jsonify("Não foi possível realizar a exclusão",404)


app.run(port=5000, host="localhost", debug=True)
