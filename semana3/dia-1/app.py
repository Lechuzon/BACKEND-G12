from flask import Flask, request
from db import db
from models.products_model import ProductsModel

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/codigo" 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)


@app.before_request
def first_request():
    db.create_all()

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        return "GET"
    elif request.method == "POST":
        json = request.get_json()
        record = ProductsModel(
                               name=json['name'], 
                               stock=json['stock'], 
                               price=json['price'], 
                               created_at=json['created_at'], 
                               updated_at=json['updated_at'], 
                               status=json['status'])

        db.session.add(record)
        db.session.commit()
        return "Producto guardado correctamente"

if __name__ == '__main__':
    app.run(debug=True)
