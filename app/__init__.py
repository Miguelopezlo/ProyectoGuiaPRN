#Confugracion de la app // 
from flask import Flask
from flask_bootstrap import Bootstrap
from app import Administrador
from app.config import config   # Importando config.py
from .database import db
from .Autentificacion import Autentificacion
from .Administrador import Administrador



def create_app():
    # Crear app de FLASK
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config)
    app.register_blueprint(Autentificacion)
    app.register_blueprint(Administrador)
    db.init_app(app)
    return app