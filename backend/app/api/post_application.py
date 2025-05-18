from datetime import datetime
from flask import Blueprint, request, jsonify
import json
from app.api import database as db
post_application_bp= Blueprint("post_application", __name__)

@post_application_bp.route("/upload", methods=["POST"])
def post_application():
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    phoneNumber = request.form["phoneNumber"]
    jobPosition = request.form["position"]
    #resume = request.form["resume"]
    suburb = request.form["suburb"]
    state = request.form["state"]
    postcode = request.form["postcode"]
    timestamp = "2005-02-26 7:00:00" 
    resumePath = "meomeo/com"
    script = f"INSERT INTO CANDIDATE VALUES (DEFAULT, '{firstName}', '{lastName}', '{email}', '{phoneNumber}', '{state}', '{suburb}', '{postcode}', '{resumePath}', '{jobPosition}', NOW());"
    
    db.database_action_script(script)

    if (firstName +" "+lastName) == "Phung Do Thi Tuyet":
        return jsonify({"error": "this name has been taken"}), 403 
    else: 
        return jsonify({"msg": "success", "script": script}), 200
