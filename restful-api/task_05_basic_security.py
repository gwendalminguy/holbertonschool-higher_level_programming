#!./venv/bin/python3
"""
Module containing basic Flask API.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

import json

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "63f4945d921d599f27ae4fdf5bada3f1"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
    "fabien": {
        "username": "fabien",
        "password": generate_password_hash("APPLEANDNOTHINGELSE"),
        "role": "admin"
    },
    "hugo": {
        "username": "hugo",
        "password": generate_password_hash("JSISTHEBEST"),
        "role": "user"
    },
}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@auth.verify_password
def verify_password(username, password):
    if username in users.keys() and check_password_hash(users[username]["password"], password):
        return username


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        content = json.loads(request.data)
        username = content["username"]
        password = content["password"]
        if username in users.keys() and check_password_hash(users[username]["password"], password):
            #print("VALID USER")
            additional_claims = {"role": users[username]["role"]}
            users[username]["access_token"] = create_access_token(
                identity=users[username]["username"],
                additional_claims=additional_claims
            )
            return jsonify(access_token=users[username]["access_token"]), 200
        else:
            #print("INVALID USER")
            return jsonify({"message": "Invalid Username or Password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    role = users[user]["role"]
    if role == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
