#Confugracion de la app // 
from flask import Flask, render_template as render
from flask_bootstrap import Bootstrap
from app.config import config   # Importando config.py
from .database import db
from .Autentificacion import Autentificacion



def create_app():
    # Crear app de FLASK
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config)
    app.register_blueprint(Autentificacion)
    db.init_app(app)
    return app