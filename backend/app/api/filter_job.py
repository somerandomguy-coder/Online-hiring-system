from flask import Blueprint, jsonify
import database as db

filter_job_bp = Blueprint("filter_job", __name__)

@filter_job_bp.route("/filter_job/", methods=["GET"])
def get_job():
    script = "SELECT * FROM jobpost"
    lst = db.database_query_script(script)
    output = format_for_json(lst)
    return jsonify(output)

def format_for_json(lst) -> list:
    output = []
    columns = db.database_get_columns("jobpost")
    for i in range(len(lst)):
        record = lst[i]
        dic = {}
        for j in range(len(record)):
            dic[columns[j]]=record[j]
        output.append(dic)
    return output
