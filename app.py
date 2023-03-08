from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text


app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs"))

    jobs = []
    for row in results:
      jobs.append(row._mapping)
    return jobs


@app.route("/")
def hello_sd614apps():
  jobs = load_jobs_from_db()
  return render_template("home.html",
                         jobs=jobs,
                         company_name="SD614 Apps")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
