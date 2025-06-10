#!./venv/bin/python3
"""
Module containing basic Flask API.
"""
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
users = {}
        #"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        #"david": {"username": "david", "name": "David", "age": 22, "city": "New York"}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_usernames():
    usernames = [username for username in users.keys()]
    return jsonify(usernames)


@app.route("/users/<username>")
def get_user(username):
    if username in users.keys():
        user = users[username]
        return jsonify(user)
    else:
        error = {"error": "User not found"}
        return jsonify(error)


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST":
        content = json.loads(request.data)

        if "username" in content.keys():
            user = {
                "username": content["username"],
                "name": content["name"],
                "age": content["age"],
                "city": content["city"]
            }
            users[user["username"]] = user
            message = "User added"
            return jsonify({
                "message": message,
                "user": user
            }), 201

        else:
            message = {"error": "Username is required"}
            return jsonify(message), 400


@app.route("/status")
def get_status():
    return ("OK")


if __name__ == "__main__":
    app.run()
