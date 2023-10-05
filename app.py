from connection import connection_string
from flask import Flask ,jsonify ,request
from flask_cors import CORS      
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import mysql.connector



app = Flask(__name__)
CORS(app)

#DB
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

conn = mysql.connector.connect(user = "root", host = "localhost")
cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS testing')
cursor.execute('USE testing')
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
)""")


conn.commit()
conn.close()




# # Ruta para la página principal
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Ruta para manejar el formulario y guardar datos en la base de datos
# @app.route('/registro', methods=['POST'])
# def guardar_datos():
#     # Obtener datos del formulario
#     name = request.form['name']
#     lastname = request.form['lastname']
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']

#     # Crear un nuevo usuario
#     new_user = User(name=name, lastname=lastname, username=username, email=email, password=password)

#     # Agregar el nuevo usuario a la base de datos
#     db.session.add(new_user)
#     db.session.commit()

#     return "Registro exitoso"

