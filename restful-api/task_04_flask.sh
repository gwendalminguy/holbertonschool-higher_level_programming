#!/bin/bash

echo -e "\n> Access Root:"
curl http://localhost:5000

echo -e "\n\n> Access Status:"
curl http://localhost:5000/status

echo -e "\n\n> Add New Users:"
curl -X POST -H "Content-Type: application/json" -d '{"username":"hugo","name":"Hugo","age":"22","city":"Toulouse"}' http://localhost:5000/add_user
curl -X POST -H "Content-Type: application/json" -d '{"username":"fabien","name":"Fabien","age":"35","city":"Toulouse"}' http://localhost:5000/add_user

echo -e "\n> Add New User Without Username (Error Expected):"
curl -X POST -H "Content-Type: application/json" -d '{"name":"Gwendal","age":"27","city":"Toulouse"}' http://localhost:5000/add_user

echo -e "\n> Access Data (User List Expected):"
curl http://localhost:5000/data

echo -e "\n> Access Existing Users:"
curl http://localhost:5000/users/hugo
curl http://localhost:5000/users/fabien

echo -e "\n> Access Not Existing User (Error Expected):"
curl http://localhost:5000/users/gwendal
