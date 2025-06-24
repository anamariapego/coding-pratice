from flask import Flask
from src.main.routes.routes import user_route_bp

# Instância principal da aplicação Flask
app = Flask(__name__)

# Registro do blueprint de rotas de usuários
app.register_blueprint(user_route_bp)
