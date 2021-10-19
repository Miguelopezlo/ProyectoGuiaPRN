from flask import Blueprint, blueprints


Autentificacion = Blueprint('Autentificacion', __name__, url_prefix='/Autentificacion', template_folder='templates')
from . import vistas