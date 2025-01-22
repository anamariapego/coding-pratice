# Define uma imagem base, nesse exemplo o Node.js
FROM node

# Define o diretótio de trabalho no container
WORKDIR /app

# Copia os arquivos package.json e package-lock.json para o container
COPY package*.json .

# Instala as dependências do projeto
RUN npm install

#  Copia todos os arquivos do diretório local para o container
COPY . . 

# Declara a porta que será usada pela aplicação
EXPOSE 3000

# Comando para inicializar a aplicação
CMD ["node", "app.js"]
