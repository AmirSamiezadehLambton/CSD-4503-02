from app import app
from flask import render_template


@app.route("/index", methods=["GET"])
def index():
    return "This is an awesome app!"


@app.route("/", methods=["GET"])
def landing():
    return render_template("index.html")
