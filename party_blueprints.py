from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

party_blueprints = Blueprint('party_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/student"


@party_blueprints.route("/party", methods=['GET'])
def get_all_parties() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()
