from datetime import timedelta
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, verify_jwt_in_request,
                                get_jwt_identity)
import requests

from waitress import serve
from utils import clear_url, load_file_config, HEADERS, validate_grant

#=== Import results-backend blueprints ===
from results_blueprints.candidato_blueprint import candidato_blueprint
from results_blueprints.mesa_blueprint import mesa_blueprint
from results_blueprints.partido_blueprint import partido_blueprint
from results_blueprints.reporte_blueprint import reports_blueprint
from results_blueprints.voto_blueprint import voto_blueprint

#=== Import security-backend blueprints ===
from security_blueprints.permission_blueprint import permission_blueprint
from security_blueprints.rol_blueprint import rol_blueprint
from security_blueprints.user_blueprint import user_blueprint

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mission-tic"
CORS(app)
jwt = JWTManager(app)

#=== Register results-backend blueprints ===
app.register_blueprint(candidato_blueprint)
app.register_blueprint(mesa_blueprint)
app.register_blueprint(partido_blueprint)
app.register_blueprint(reports_blueprint)
app.register_blueprint(voto_blueprint)
#=== Register security-backend blueprints ===
app.register_blueprint(permission_blueprint)
app.register_blueprint(rol_blueprint)
app.register_blueprint(user_blueprint)

@app.before_request
def before_request_callback() -> tuple:
    endpoint = clear_url(request.path)
    exclude_routes = ['/login','/']
    if exclude_routes.__contains__(endpoint):
        pass
    elif verify_jwt_in_request():
        user : dict = get_jwt_identity()
        if user.get('rol'):
            has_grant = validate_grant(endpoint, request.method, user['rol'].get('idRol') )
            if not has_grant:
                return {"message":f"The rol {user['rol']['idRol']}:{user['rol']['name']} doesn't have permission to access {endpoint}"}, 401
            print(f'Permiso:{has_grant}')
        else:
            return {"message":"Permission denied. Rol not defined."}, 401

@app.route("/", methods=["GET"])
def home():
    response = {"message":"Welcome!"}
    return response, 200

@app.route("/login", methods=["POST"])
def login() -> tuple:
    user = request.get_json()
    url = data_config.get("url-backend-security") + "/user/login"
    response = requests.post(url=url, headers=HEADERS, json=user)
    if response.status_code == 200:
        user_logged :dict = response.json()
        del user_logged["rol"]["permissions"]
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token":access_token, "user_id":user_logged.get("idUser")}, 200
    else: 
        return {"message":"Access denied"}, 401



if __name__ == "__main__":
    data_config = load_file_config()
    print("API Gateway Server Running: http://"+
            data_config.get("url-api-gateway")+":"+
            str(data_config.get("port")))
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
