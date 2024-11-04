from app import app, products_collection
from flask import render_template


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/products", methods=["GET"])
def products():
    # Retrieve the product information from MongoDB
    products = list(products_collection.find())
    print(products)
    # Return an HTML page with the product information in a table
    return render_template("products.html", products=products)
