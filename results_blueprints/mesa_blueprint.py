from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

mesa_blueprint = Blueprint("mesa_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/mesa"

@mesa_blueprint.route("/mesa/all", methods=["GET"])
def get_all_mesas() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@mesa_blueprint.route("/mesa/<string:id_>", methods=["GET"])
def get_mesa_by_id(id_ : str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@mesa_blueprint.route("/mesa/create", methods=["POST"])
def create_mesa() -> dict:
    mesa = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=mesa)
    return response.json()

@mesa_blueprint.route("/mesa/update/<string:id_>", methods=["PUT"])
def update_mesa(id_ : str) -> dict:
    mesa = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=mesa)
    return response.json()

@mesa_blueprint.route("/mesa/delete/<string:id_>", methods=["DELETE"])
def delete_mesa( id_ : str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
