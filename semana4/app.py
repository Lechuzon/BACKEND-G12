from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from os import environ # muestra las variables de entorno

# load_dotenv > carga todas las variables presentes en el archivo .env y las coloca 
# como si fuesen variables de entorno, siempre debe ir en la primera linea del archivo principal del proyecto
load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['SQLACHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# app.config['SQLACHEMY_DATABASE_URI'] = environ('DATABASE_URL')

print(environ.get('DATABASE_URL'))

if __name__ == '__main__':
    app.run(debug=True)
