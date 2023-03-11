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


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(f"INSERT INTO applications ("
                     f"job_id,"
                     f" full_name,"
                     f" email,"
                     f" linkedin_url,"
                     f" education,"
                     f" work_experience,"
                     f" resume_url) VALUES ("
                     f"{job_id},"
                     f" '{data['full_name']}',"
                     f" '{data['email']}',"
                     f" '{data['linkedin_url']}',"
                     f" '{data['education']}',"
                     f" '{data['work_experience']}',"
                     f" '{data['resume_url']}')")

        conn.execute(query)
