from flask import Blueprint

patient_blueprint = Blueprint('patient_blueprint', __name__, url_prefix='/patient')

from . import routes
