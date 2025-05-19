from flask import Flask, request, render_template, url_for
from flask_cors import CORS
from markupsafe import escape
from app import database as db

app = Flask(__name__)
CORS(app, resource={r"/api/*": {"origins": ["http://happyhiring.com:8080", "http://localhost:8080"]}})



@app.route("/")
def index():
    return render_template("base.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        name = request.form.get("username")
        passw = request.form.get("password")
        if name != "" and passw != "":
            return "<h1>Succesfully posted</h1>"
        else: 
            return "<h1>Some information missing</h1>"

from app.api import filter_job, post_application
app.register_blueprint(filter_job.filter_job_bp)
app.register_blueprint(post_application.post_application_bp)
