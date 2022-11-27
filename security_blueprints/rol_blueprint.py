from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

rol_blueprint = Blueprint("rol_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/rol"

@rol_blueprint.route("/rol/all", methods=["GET"])
def get_all_rol() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@rol_blueprint.route("/rol/<int:id_>", methods=["GET"])
def get_rol_by_id(id_ : int) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@rol_blueprint.route("/rol/create", methods=["POST"])
def create_rol() -> dict:
    rol = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=rol)
    return response.json()

@rol_blueprint.route("/rol/update/<int:id_>", methods=["PUT"])
def update_rol(id_ : int) -> dict:
    rol = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.put(url, headers=HEADERS, json=rol)
    return response.json()

@rol_blueprint.route("/rol/delete/<int:id_>", methods=["DELETE"])
def delete_rol( id_ : int) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
