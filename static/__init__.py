from flask import Blueprint

swagger_ui_bluerint_perso = Blueprint('swagger_ui_bluerint_perso', __name__)

from . import routes
