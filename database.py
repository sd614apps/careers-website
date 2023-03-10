from sqlalchemy import create_engine, text
import os

db_conn_uri = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_conn_uri,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs"))

    jobs = []
    for row in results:
      jobs.append(dict(row._mapping))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    query = text(f"SELECT * FROM jobs WHERE id= {id}")
    res = conn.execute(query)

    if res.rowcount == 0:
      return None

    for row in res:
      return dict(row._mapping)
