from connection import connection_string
from flask import Flask ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)



#DB
app.config['SQL_SERVER_CONNECTION_STRING'] = connection_string
if app.config:
        print("Se conecto correctamente")


db = SQLAlchemy(app)


def get_db_connection():
    return pyodbc.connect(app.config['SQL_SERVER_CONNECTION_STRING'])