import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        port="5432",
        user="postgres",
        password="postgres",
        database="mydatabase"
    )

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Hello, Docker! Database version: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)