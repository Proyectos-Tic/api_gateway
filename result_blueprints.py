from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

result_blueprints = Blueprint('result_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/result"


@result_blueprints.route("/result/insert", methods=['POST'])
def insert_result() -> dict:
    result = request.get_json()
    url = url_base + "/result/insert"
    response = requests.post(url, headers=HEADERS, json=result)
    return response.json()
