# syntax=docker/dockerfile:1

# Passo a passo para fazer a instalação do projeto
# 1. Instalar python e escolher sua versão
# 2. Escolher em que pasta colocar o projeto
# 3. Instalar as dependências do projeto
# 4. Copia o projeto
# 5. Rodar o projeto!


FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT python3 run.py
