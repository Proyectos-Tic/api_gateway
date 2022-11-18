from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

rol_blueprints = Blueprint('rol_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/rol"


@rol_blueprints.route("/rol", methods=['GET'])
def get_all_rols() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@rol_blueprints.route("/rol/<string:id_>", methods=['GET'])
def rol_by_id(id_: str) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@rol_blueprints.route("/rol/insert", methods=['POST'])
def insert_rol() -> dict:
    rol = request.get_json()
    url = url_base + "/rol/insert"
    response = requests.post(url, headers=HEADERS, json=rol)
    return response.json()


@rol_blueprints.route("/rol/update/<string:id_>", methods=['PATCH'])
def update_rol(id_: str) -> dict:
    rol = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=rol)
    return response.json()


@rol_blueprints.route("/rol/delete/<string:id_>", methods=['DELETE'])
def delete_rol(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()

