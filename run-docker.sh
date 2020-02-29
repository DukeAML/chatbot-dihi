#!/usr/bin/env bash

echo killing old docker processes
docker-compose rm -fs

echo if you need to generate self-signed certificates:
echo openssl req -x509 -newkey rsa:4096 -nodes -keyout chatbot-moderator/key.pem -out chatbot-moderator/cert.pem -days 3650 -subj "/CN=localhost"
echo openssl req -x509 -newkey rsa:4096 -nodes -keyout server/key.pem -out server/cert.pem -days 3650 -subj "/CN=localhost"

echo building docker containers
docker-compose up --build -d
