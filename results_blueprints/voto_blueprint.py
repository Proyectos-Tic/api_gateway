from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

voto_blueprint = Blueprint("voto_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/voto"

@voto_blueprint.route("/voto/all", methods=["GET"])
def get_all_votos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@voto_blueprint.route("/voto/<string:id_>", methods=["GET"])
def get_voto_by_id(id_ : str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@voto_blueprint.route("/voto/create/mesa/<string:idMesa>/candidato/<string:idCandidato>", methods=["POST"])
def create_voto(idMesa:str, idCandidato: str) -> dict:
    voto = {}
    url = url_base + f'/create/mesa/{idMesa}/candidato/{idCandidato}'
    response = requests.post(url, headers=HEADERS, json=voto)
    return response.json()

@voto_blueprint.route("/voto/update/<string:id_>", methods=["PUT"])
def update_voto(id_ : str) -> dict:
    voto = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=voto)
    return response.json()

@voto_blueprint.route("/voto/delete/<string:id_>", methods=["DELETE"])
def delete_voto( id_ : str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
