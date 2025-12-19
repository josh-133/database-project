import psycopg2
from psycopg2.pool import SimpleConnectionPool

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host="postgres",
    database="sqldb",
    user="postgres",
    password="password",
)

def get_conn():
    return pool.getconn()

def release_conn(conn):
    pool.putconn(conn)