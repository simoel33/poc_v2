from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
#import pyodbc
import pymssql


import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config):
    # * creation of Flask APP
    app = Flask(__name__)

    app.config.from_object(config)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'patients-exp.db')
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    # TODO: register Blueprints 
    from patients import patient_blueprint
    from experimentation import experimentation_blueprint

    app.register_blueprint(experimentation_blueprint)
    app.register_blueprint(patient_blueprint)

    return app
