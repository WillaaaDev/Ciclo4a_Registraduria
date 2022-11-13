from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
miControladorMesa=ControladorMesa()
from Controladores.ControladorPartidoPolitico import ControladorPartidoPolitico
miControladorPartidoPolitico=ControladorPartidoPolitico()
from Controladores.ControladorCandidatos import ControladorCandidatos
miControladorCandidatos=ControladorCandidatos()



@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="listos ..."
    return jsonify(json)

@app.route("/mesa",methods=['GET'])
def getMesa1():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


@app.route("/PartidoPolitico",methods=['GET'])
def getPartidoPolitico1():
    json=miControladorPartidoPolitico.index()
    return jsonify(json)
@app.route("/PartidoPolitico",methods=['POST'])
def crearPartidoPolitico():
    data = request.get_json()
    json=miControladorPartidoPolitico.create(data)
    return jsonify(json)
@app.route("/PartidoPolitico/<string:id>",methods=['GET'])
def getPartidoPolitico(id):
    json=miControladorPartidoPolitico.show(id)
    return jsonify(json)
@app.route("/PartidoPolitico/<string:id>",methods=['PUT'])
def modificarPartidoPolitico(id):
    data = request.get_json()
    json=miControladorPartidoPolitico.update(id,data)
    return jsonify(json)

@app.route("/PartidoPolitico/<string:id>",methods=['DELETE'])
def eliminarPartidoPolitico(id):
    json=miControladorPartidoPolitico.delete(id)
    return jsonify(json)


@app.route("/Candidatos",methods=['GET'])
def getCandidatos1():
    json=miControladorCandidatos.index()
    return jsonify(json)
@app.route("/Candidatos",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidatos.create(data)
    return jsonify(json)
@app.route("/Candidatos/<string:id>",methods=['GET'])
def getCandidatos(id):
    json=miControladorCandidatos.show(id)
    return jsonify(json)
@app.route("/Candidatos/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=miControladorCandidatos.update(id,data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=miControladorCandidatos.delete(id)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

