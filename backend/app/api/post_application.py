from datetime import datetime
import random
import os
from flask import Blueprint, request, jsonify
import json
from app import app
from app.api import database as db
post_application_bp= Blueprint("post_application", __name__)
from app.services.processing_resume import processing_resume, relevant_score, unique_score

@post_application_bp.route("/upload", methods=["POST"])
def post_application():
    app.config["UPLOAD_FOLDER"] = "/home/namle/Documents/git-repos/Online-hiring-system/backend/app/upload_resumes/"
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    phoneNumber = request.form["phoneNumber"]
    jobPosition = request.form["position"]
    resume = request.files["resume"]
    file_extension = resume.filename[-3:]
    filename = "resume" + str(random.randint(1, 999999)) + file_extension
    resumePath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    resume.save(resumePath)
    suburb = request.form["suburb"]
    state = request.form["state"]
    postcode = request.form["postcode"]
    script = f"INSERT INTO CANDIDATE VALUES (DEFAULT, '{firstName}', '{lastName}', '{email}', '{phoneNumber}', '{state}', '{suburb}', '{postcode}', '{resumePath}', '{jobPosition}', NOW());"
    
    db.database_action_script(script)
    
    text = processing_resume(resumePath)
    rel_score, skill_matched = relevant_score(text)
    model_path = "/home/namle/Documents/git-repos/Online-hiring-system/backend/app/ENVIRONMENT/vectorizer.pkl"
    mean_path = "/home/namle/Documents/git-repos/Online-hiring-system/backend/app/ENVIRONMENT/means_resume.pkl"
    uni_score = unique_score(text, model_path, mean_path)
    print(rel_score, uni_score)
    return jsonify({"msg": "success", "relevant_score": rel_score, "skill_matched": skill_matched, "unique_score": uni_score, }), 200
