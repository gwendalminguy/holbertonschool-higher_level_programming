#!/bin/bash

echo -e "\n> Access Root:"
curl http://localhost:5000

echo -e "\n\n> Access Basic Protected Valid Credentials:"
curl --user hugo:JSISTHEBEST http://localhost:5000/basic-protected

#echo -e "\n> Access Basic Protected Invalid Password (Error Expected):"
#curl --user hugo:PYTHONSUCKS http://localhost:5000/basic-protected

#echo -e "\n\n> Login Invalid User (Error Expected):"
#curl -X POST -H "Content-Type: application/json" -d '{"username":"gwendal","password":"METALRULES"}' http://localhost:5000/login

#echo -e "\n> Login Invalid Password (Error Expected):"
#curl -X POST -H "Content-Type: application/json" -d '{"username":"hugo","password":"PYTHONSUCKS"}' http://localhost:5000/login

echo -e "\n\n> Login Valid Credentials:"
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d '{"username":"fabien","password":"APPLEANDNOTHINGELSE"}' http://localhost:5000/login)
export JWT="$(echo "$RESPONSE" | jq -r '.access_token')"
echo "Access Token: $JWT"

#echo -e "\n> Access JWT Protected Route Invalid Token (Error Expected):"
#curl -H "Authorization: Bearer ABCDEFGHIJKLMNOPQRSTUVWXYZ" http://localhost:5000/jwt-protected

echo -e "\n> Access JWT Protected Route Valid Token:"
curl -H "Authorization: Bearer $JWT" http://localhost:5000/jwt-protected

echo -e "\n\n> Access Admin Only:"
curl -H "Authorization: Bearer $JWT" http://localhost:5000/admin-only
