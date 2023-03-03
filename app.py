from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'INR 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New Delhi, India',
    'salary': 'INR 15,00,000'
  },
  {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'Remote',
    'salary': 'INR 12,00,000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'San Jose, USA',
    'salary': 'USD 90,000'
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                         company_name="SD614 Apps")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
