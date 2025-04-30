from flask import Flask, request, render_template
from markupsafe import escape
import database as db
from app.api import filter_job

app = Flask(__name__)

app.register_blueprint(filter_job.filter_job_bp)

@app.route("/")
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return "<h1>You GET this page</h1>"
    elif request.method == "POST":
        return "<h1>You POST this page</h1>"


print(app.url_map)
