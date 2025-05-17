from flask import Blueprint, request, jsonify
import json
post_application_bp= Blueprint("post_application", __name__)

@post_application_bp.route("/upload", methods=["POST"])
def post_application():
    data = request.form.get("name")
    if data == "Phung Do Thi Tuyet":
        return jsonify({"error": "this name has been taken"}), 403 
    else: 
        return 200
# script = f"INSERT TABLE RESUME VALUES ({id}, {firstname}, {lastname}, {email}, {state}, {suburb}, {postcode}, {resume}, {coverletter}, {jobposition}, {timestamp})"
