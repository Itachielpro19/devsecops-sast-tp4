from flask import Flask, request
import sqlite3
import subprocess
import hashlib

app = Flask(__name__)
SECRET_KEY = "mysecretkey123"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    query = "SELECT * FROM users WHERE id=" + user_id
    result = conn.execute(query).fetchall()
    return str(result)

@app.route('/ping')
def ping():
    host = request.args.get('host')
    output = subprocess.check_output(
        "ping -c 1 " + host, shell=True
    )
    return output

@app.route('/hash')
def hash_password():
    pwd = request.args.get('pwd')
    return hashlib.md5(pwd.encode()).hexdigest()

if __name__ == "__main__":
    app.run(debug=True)
