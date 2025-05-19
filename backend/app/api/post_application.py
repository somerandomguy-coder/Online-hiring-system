from datetime import datetime
import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import json
from app import app
from app.api import database as db
post_application_bp= Blueprint("post_application", __name__)

@post_application_bp.route("/upload", methods=["POST"])
def post_application():
    app.config["UPLOAD_FOLDER"] = "/home/namle/Documents/git-repos/Online-hiring-system/backend/app/upload_resumes/"
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    phoneNumber = request.form["phoneNumber"]
    jobPosition = request.form["position"]
    resume = request.files["resume"]
    filename = secure_filename(resume.filename)
    resumePath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    resume.save(resumePath)
    suburb = request.form["suburb"]
    state = request.form["state"]
    postcode = request.form["postcode"]
    script = f"INSERT INTO CANDIDATE VALUES (DEFAULT, '{firstName}', '{lastName}', '{email}', '{phoneNumber}', '{state}', '{suburb}', '{postcode}', '{resumePath}', '{jobPosition}', NOW());"
    
    db.database_action_script(script)

    return jsonify({"msg": "success", "form": request.form, }), 200
