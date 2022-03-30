from flask import Blueprint

experimentation_blueprint = \
Blueprint('experimentation_blueprint',__name__, url_prefix='/experimentation')

from . import routes