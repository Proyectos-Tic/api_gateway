from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

result_blueprints = Blueprint('result_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-voting') + "/result"


@result_blueprints.route("/result/insert", methods=['POST'])
def insert_result() -> tuple:
    vote = request.get_json()
    table_id = vote.get('table').get('_id')
    candidate_id = vote.get('candidate').get('_id')
    url = url_base + f"/table/{table_id}/candidate/{candidate_id}"
    response = requests.post(url, headers=HEADERS, json=vote)
    return {"message": "processed"}, response.status_code
