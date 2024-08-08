# Librerías importadas
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db


from flask import Flask
import credentials
from firebase_admin import initialize_app
# Obtener las credenciales de acceso a la API de Firebase
# Para la Base de Datos No Relacional
credential = credentials.firebase_cred_file
default_app = initialize_app(credential)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345rtfescdvf'
    
    from .userAPI import userAPI
    app.register_blueprint(userAPI, url_prefix='/tasks')
    
    return app