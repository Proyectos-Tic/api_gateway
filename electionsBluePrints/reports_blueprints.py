from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

reports_blueprint = Blueprint('reports_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/reports"


@reports_blueprint.route("/reports/general", methods=['GET'])
def get_general() -> list:
    url = url_base + '/general'
    response = requests.post(url, headers=HEADERS)
    return response
