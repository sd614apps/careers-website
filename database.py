from sqlalchemy import create_engine

db_conn_uri = "mysql+pymysql://fvhzp2iuhn01uiou1og6:pscale_pw_3KJ57CxvKjJI8EeAwwPPzdBSU8N5hxdMjYuSeS2s4RE@ap-south.connect.psdb.cloud/sd614appscareers?charset=utf8mb4"

engine = create_engine(
  db_conn_uri,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  })
