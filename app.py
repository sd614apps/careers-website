from flask import Flask, render_template, request, jsonify
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)
company_name = "SD614 Apps"


@app.route("/")
def hello_sd614apps():
    jobs = load_jobs_from_db()
    return render_template("home.html",
                           jobs=jobs,
                           company_name=company_name)


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jobs


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)

    if not job:
        return "Not Found", 404

    return render_template("jobpage.html",
                           job=job,
                           company_name=company_name)


# [TODO] provide an API to access individual applications by ID
# API to access individual job listings by ID
@app.route("/api/job/<id>")
def show_job_json(id):
    job = load_job_from_db(id)
    return jsonify(job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    # store this in the DB
    add_application_to_db(id, data)

    # [TODO] send an email acknowledgement to admin and candidate
    # [TODO] use captcha in the application form to prevent spam/bots

    # display the acknowledgement
    return render_template("application_submitted.html",
                           application=data,
                           job=job,
                           company_name=company_name)


# [TODO] Future work
# Admin login interface to check submitted applications
# allow admins to mark applications as accepted/rejected
# User login interface to check application status


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
