from flask import render_template
from application import app

@app.route("/health")
def check_status():
    return "Status OK"

@app.route("/data")
def data():
    return render_template("data.html")
