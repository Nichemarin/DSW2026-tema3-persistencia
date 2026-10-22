from flask import Flask
from app.models import db, Product

app = Flask(__name__)
app.config["SECRET_KEY"] = "Jwolfenwasher3."

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if not Product.query.first():
        new_product = Product(nombre="Teclado Mecánico RGB", precio=49.99)
        db.session.add(new_product)
        db.session.commit()
        print("Diablo mi lidel, el producto se gualdo")


@app.route("/")
def hello():
    return "Keloke lidel mio"

@app.route("/test.db")
def test_db():
    products = Product.query.all()
    return f"Pero mi lidel, mire el catalogo: {products}"

@app.route("/nuevo-producto")
def nuevo_productos():
    new_product = Product(nombre="Ratón Inalámbrico", precio=29.99, disponible=True)
    db.session.add(new_product)
    db.session.commit()
    return f"Nuevo producto agregado: {new_product}"

@app.route("/nuevo-producto/<string:nombre>/<float:precio>")
def nuevo_producto(nombre, precio):
    new_product = Product(nombre=nombre, precio=precio)

    db.session.add(new_product)
    db.session.commit()

    return f"Producto creado correctamente con ID: {new_product.id}"

if __name__ == "__main__":
    app.run(debug=True)
