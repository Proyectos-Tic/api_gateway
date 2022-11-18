from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

user_blueprint = Blueprint("user_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-security') + "/user"

@user_blueprint.route("/user/all", methods=["GET"])
def get_all_users() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@user_blueprint.route("/user/by_id/<int:id_>", methods=["GET"])
def get_user_by_id(id_ : int) -> dict:
    url = url_base + f'/by_id/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@user_blueprint.route("/user/by_nickname/<string:id_>", methods=["GET"])
def get_user_by_id(id_ : str) -> dict:
    url = url_base + f'/by_nickname/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@user_blueprint.route("/user/by_email/<string:id_>", methods=["GET"])
def get_user_by_id(id_ : str) -> dict:
    url = url_base + f'/by_email/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@user_blueprint.route("/user/create", methods=["POST"])
def create_user() -> dict:
    user = request.get_json()
    url = url_base + f'/create'
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()

@user_blueprint.route("/user/update/<int:id_>", methods=["POST"])
def update_user(id_ : int) -> dict:
    user = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()

@user_blueprint.route("/user/delete/<int:id_>", methods=["DELETE"])
def delete_user( id_ : int) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()
