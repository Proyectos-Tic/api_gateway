from datetime import timedelta
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, verify_jwt_in_request,
                                get_jwt_identity)
import requests

from waitress import serve
from utils import load_file_config, HEADERS

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mission-tic"
CORS(app)
jwt = JWTManager(app)


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
