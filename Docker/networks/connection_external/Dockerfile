# Imagem do python
FROM python:3

# Instalação e atualizaçãodas dependências
RUN apt-get update && \
  apt-get install -y --no-install-recommends curl && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho
WORKDIR /app

# Instalação do fremework e biblioteca
RUN pip install Flask
RUN pip install requests

# Copia o arquivo da aplicação
COPY . .

# Expoção da porta
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "./app.py"]