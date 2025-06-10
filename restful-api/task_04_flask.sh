#!/bin/bash

echo -e "\n> Access root:"
curl http://localhost:5000

echo -e "\n\n> Access status:"
curl http://localhost:5000/status

echo -e "\n\n> Add new users:"
curl -X POST -H "Content-Type: application/json" -d '{"username":"hugo","name":"Hugo","age":"22","city":"Toulouse"}' http://localhost:5000/add_user
curl -X POST -H "Content-Type: application/json" -d '{"username":"fabien","name":"Fabien","age":"35","city":"Toulouse"}' http://localhost:5000/add_user

echo -e "\n> Add new user without username (error expected):"
curl -X POST -H "Content-Type: application/json" -d '{"name":"Gwendal","age":"27","city":"Toulouse"}' http://localhost:5000/add_user

echo -e "\n> Access data (user list expected):"
curl http://localhost:5000/data

echo -e "\n> Access existing users:"
curl http://localhost:5000/users/hugo
curl http://localhost:5000/users/fabien

echo -e "\n> Access not existing user (error expected):"
curl http://localhost:5000/users/gwendal
