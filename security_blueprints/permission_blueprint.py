from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

permission_blueprint = Blueprint("permission_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/permission"

@permission_blueprint.route("/permission/all", methods=["GET"])
def get_all_permissions() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@permission_blueprint.route("/permission/<int:id_>", methods=["GET"])
def get_permission_by_id(id_ : int) -> dict:
    url = url_base + f'/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@permission_blueprint.route("/permission/create", methods=["POST"])
def create_permission() -> dict:
    permission = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=permission)
    return response.json()

@permission_blueprint.route("/permission/update/<int:id_>", methods=["PUT"])
def update_permission(id_ : int) -> dict:
    permission = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.put(url, headers=HEADERS, json=permission)
    return response.json()

@permission_blueprint.route("/permission/delete/<int:id_>", methods=["DELETE"])
def delete_permission( id_ : int) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return {'Deleted':response.status_code}
