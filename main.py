from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)

from waitress import serve

import json

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mission-tic"
CORS(app)
jwt = JWTManager(app)

@app.route("/", methods=["GET"])
def home():
    response = {"message":"Welcome!"}
    return response, 200

# Config and execute app
def load_file_config() -> dict:
    """
    
    :return:
    """
    with open("config.json", "r") as file_:
        data = json.load(file_)
    return data

if __name__ == "__main__":
    data_config = load_file_config()
    print("API Gateway Server Running: http://"+
            data_config.get("url-api-gateway")+":"+
            str(data_config.get("port")))
    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
