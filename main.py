from datetime import timedelta
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, verify_jwt_in_request,
                                get_jwt_identity)
from waitress import serve
from electionsBluePrints.party_blueprints import party_blueprints
from electionsBluePrints.candidate_blueprints import candidate_blueprints
from electionsBluePrints.table_blueprints import table_blueprints
from securityBluePrints.user_blueprints import user_blueprints
from securityBluePrints.rol_blueprints import rol_blueprints
from securityBluePrints.permission_blueprints import permission_blueprints
from electionsBluePrints.result_blueprints import result_blueprints

import requests

import utils

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "misiontic"
cors = CORS(app)
jwt = JWTManager(app)
app.register_blueprint(party_blueprints)
app.register_blueprint(candidate_blueprints)
app.register_blueprint(table_blueprints)
app.register_blueprint(user_blueprints)
app.register_blueprint(permission_blueprints)
app.register_blueprint(rol_blueprints)
app.register_blueprint(result_blueprints)


@app.before_request
def before_request_callback():
    endpoint = utils.clear_url(request.path)
    exclude_routes = ['/login', '/']
    if exclude_routes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get('rol'):
            has_grant = utils.validate_grant(endpoint, request.method, user['rol'].get('idRol'))
            if not has_grant:
                return {"message": "Permission denied."}, 401
        else:
            return {"message": "Permission denied, no rol identified"}, 401


@app.route("/", methods=['GET'])
def home():
    response = {"message": "HELLO"}
    return response


@app.route("/login", methods=['POST'])
def login() -> tuple:
    user = request.get_json()
    url = data_config.get("url-backend-security") + "/user/login"
    response = requests.post(url, headers=utils.HEADERS, json=user)
    if response.status_code == 200:
        user_logged = response.json()
        del user_logged['rol']['permissions']
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get('id')}, 200
    else:
        return {"message": "ACCESS DENIED"}, 201


if __name__ == '__main__':
    data_config = utils.load_file_config()
    print("API GATEWAY RUNNING -> http://" +
          data_config.get("url-api-gateway") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
