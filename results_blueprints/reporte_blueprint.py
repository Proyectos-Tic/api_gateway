from flask import Blueprint, request
import requests
from utils import HEADERS, load_file_config

reports_blueprint = Blueprint("reports_blueprint",__name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-results') + "/reports"

@reports_blueprint.route("/reports/voto/sorted_candidato", methods=["GET"])
def get_candidates_report() -> dict:
    url = url_base + "/voto/sorted_candidato"
    response = requests.get(url, headers=HEADERS)
    return response.json()

@reports_blueprint.route("/reports/voto/sorted_candidato/<string:id_>", methods=["GET"])
def get_candidates_report_by_id(id_ : str) -> dict:
    url = url_base + f'/voto/sorted_candidato/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@reports_blueprint.route("/reports/voto/sorted_mesa", methods=["GET"])
def get_tables_report() -> dict:
    url = url_base + f'/voto/sorted_mesa'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@reports_blueprint.route("/reports/voto/sorted_partido", methods=["GET"])
def get_parties_report() -> dict:
    url = url_base + f'/voto/sorted_partido'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@reports_blueprint.route("/reports/voto/sorted_partido/<string:id_>", methods=["GET"])
def get_parties_report_by_id( id_ : int) -> dict:
    url = url_base + f'/voto/sorted_partido/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()

@reports_blueprint.route("/reports/voto/partido/porcentual", methods=["GET"])
def get_porcentual_parties() -> dict:
    url = url_base + f'/voto/partido/porcentual'
    response = requests.get(url, headers=HEADERS)
    return response.json()
