#!/bin/bash

echo -e "\n> Access Root:"
curl http://localhost:5000

echo -e "\n\n> Login Invalid User (Error Expected):"
curl -X POST -H "Content-Type: application/json" -d '{"username":"gwendal","password":"METALRULES"}' http://localhost:5000/login

echo -e "\n> Login Valid User + Invalid Password (Error Expected):"
curl -X POST -H "Content-Type: application/json" -d '{"username":"hugo","password":"PYTHONSUCKS"}' http://localhost:5000/login

echo -e "\n> Login Valid User + Valid Password:"
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username":"fabien","password":"APPLEANDNOTHINGELSE"}' http://localhost:5000/login)
export JWT="$(echo "$RESPONSE" | jq -r '.access_token')"
echo "Access Token: $JWT"

echo -e "\n> Access Basic Protected:"
curl http://localhost:5000/basic-protected

echo -e "\n\n> Access JWT Protected Route Invalid Token (Error Expected):"
curl -H "Authorization: Bearer ABCDEFGHIJKLMNOPQRSTUVWXYZ" http://localhost:5000/jwt-protected

echo -e "\n\n> Access JWT Protected Route Valid Token:"
curl -H "Authorization: Bearer $JWT" http://localhost:5000/jwt-protected

echo -e "\n> Access Admin Only:"
curl -H "Authorization: Bearer $JWT" http://localhost:5000/admin-only
