from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

candidato_blueprint = Blueprint("candidato_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/candidato"

@candidato_blueprint.route("/candidato/all", methods=["GET"])
def get_all_candidatos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@candidato_blueprint.route("/candidato/<string:id_>", methods=["GET"])
def get_candidato_by_id(id_ : str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@candidato_blueprint.route("/candidato/create", methods=["POST"])
def create_candidato() -> dict:
    candidato = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=candidato)
    return response.json()

@candidato_blueprint.route("/candidato/update/<string:id_>", methods=["PATCH"])
def update_candidato(id_ : str) -> dict:
    candidato = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=candidato)
    return response.json()


@candidato_blueprint.route("/candidato/<string:id_c>/partido/<string:id_p>", methods=["PUT"])
def assign_party_to_candidate(id_c : str, id_p : str) -> dict:
    url = url_base + f'/{id_c}/partido/{id_p}'
    response = requests.put(url, headers=HEADERS)
    return response.json()

@candidato_blueprint.route("/candidato/delete/<string:id_>", methods=["DELETE"])
def delete_candidato( id_ : str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
