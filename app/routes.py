from app import app, products_collection
from flask import render_template
import sentry_sdk


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    sentry_sdk.profiler.start_profiler()
    try:
        1 / 0  # raises an error
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    sentry_sdk.profiler.stop_profiler()
    return render_template("index.html")


@app.route("/products", methods=["GET"])
def products():
    # Retrieve the product information from MongoDB
    sentry_sdk.profiler.start_profiler()
    products = list(products_collection.find())
    sentry_sdk.profiler.stop_profiler()
    # print(products)
    # Return an HTML page with the product information in a table
    return render_template("products.html", products=products)
