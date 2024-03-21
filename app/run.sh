#!/bin/bash

cd backend/
pip install fastapi uvicorn

# Comando para rodar a API
# uvicorn main:app --port 3000

uvicorn main:app --port 3000 &

# Volte para o diretório principal
cd ../frontend

# Navegue até o diretório do frontend e instale as dependências
cd /app/frontend
npm install

# Comando para rodar o frontend
# npm run dev

npm run dev
