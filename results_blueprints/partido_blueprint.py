from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

partido_blueprint = Blueprint("partido_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/partido"

@partido_blueprint.route("/partido/all", methods=["GET"])
def get_all_partidos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@partido_blueprint.route("/partido/<string:id_>", methods=["GET"])
def get_partido_by_id(id_ : str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@partido_blueprint.route("/partido/create", methods=["POST"])
def create_partido() -> dict:
    partido = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=partido)
    return response.json()

@partido_blueprint.route("/partido/update/<string:id_>", methods=["PATCH"])
def update_partido(id_ : str) -> dict:
    partido = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=partido)
    return response.json()

@partido_blueprint.route("/partido/delete/<string:id_>", methods=["DELETE"])
def delete_partido( id_ : str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
