import json
import re

import requests

HEADERS  = {"Content-Type":"application/json; charset=utf-8"}
# Config and execute app
def load_file_config() -> dict:
    """
    
    :return:
    """
    with open("config.json", "r") as file_:
        data = json.load(file_)
    return data

def clear_url(url: str) -> str:
    """
    With a recursive search find a digit in each segment of the url and change it to '?', for easy injection.

    :param url:
    :return str
    """
    segments = url.split('/')
    for segment in segments:
        if re.search('\\d',segment):
            url = url.replace(segment, "?")
    return url

def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    """
    Request the microservice from security-backend to verify if a specified rol has the provided method and url (Permission).

    :param endpoint:
    :param method:
    :param id_rol:
    :return has_grant:
    """
    data_config = load_file_config()
    url = data_config.get('url-backend-security') + f'/rol/validate/{id_rol}'
    body = {
        "url": endpoint,
        "method": method
    }
    response = requests.get(url, headers=HEADERS,json=body)
    has_grant = False
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant
