from flask import Blueprint, request
from api.schema.jobschema import jobschema, jobsschema
from api.models.jobsmodel import Job
from api import db

jobs = Blueprint("jobs", __name__, url_prefix="/jobs")


# get_all_avalable_jobs
@jobs.route("/", methods=['GET'])
def get_jobs():
    job_db = Job.query.all()
    return jobsschema.dump(job_db)


# get_job_by_id
@jobs.route("/<id>", methods=['GET'])
def get_jobs_id(id):
    job_db = Job.query.get(id)
    return jobschema.jsonify(job_db)


# post_job
@jobs.route("/", methods=['POST'])
def post_jobs():
    job_db = Job(
        position = request.json["position"],
        company = request.json["company"],
        location = request.json["location"],
        site_posted = request.json["site_posted"],
        job_type = request.json["job_type"],
        time_posted = request.json["time_posted"],
        cv_data = request.json["cv_data"],
        description = request.json["description"],
        modified = request.json["modified"],
        company_website = request.json["company_website"]
    )
    db.session.add(job_db)
    db.session.commit()
    return jobschema.jsonify(job_db)


# delete_job
@jobs.route("/jobs/<id>", methods=["DELETE"])
def delete_jobs(id):
    job_db = Job.query.get(id)
    db.session.delete(job_db)
    db.session.commit()
    return jobschema.jsonify(job_db)