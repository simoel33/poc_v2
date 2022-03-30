import os

# ! configuration class
#basedir = os.path.abspath(os.path.dirname(__file__))
#import pyodbc
#import pymssql

class DevConfiguration:
    SECRET_KEY = 'ELYAZID MOHAMED APP'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'patients-exp.db')
    # ! https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyodbc    # for pyodbc and manually instalation

    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://elyazid:QsMpafyY6eBQthaR@poc-dih4cps.database.windows.net/POC?driver=SQL+Server'

    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://elyazid:QsMpafyY6eBQthaR@poc-dih4cps.database.windows.net/POC'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8
#SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://elyazid:QsMpafyY6eBQthaR@poc-dih4cps.database.windows.net/POC?driver=SQL+Server'
