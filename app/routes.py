from app import app


@app.route("/index", methods=["GET"])
def index():
    return "This is an awesome app!"
