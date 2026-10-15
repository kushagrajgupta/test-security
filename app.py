import os
import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Hardcoded Secret/Credentials
# Semgrep rule: python.flask.security.audit.hardcoded-config
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "super_secret_password_123!"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerability 2: SQL Injection
    # Semgrep rule: python.lang.security.deserialization.sql-injection
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    return str(cursor.fetchall())

@app.route('/ping')
def ping():
    target = request.args.get('target')
    
    # Vulnerability 3: Command Injection
    # Semgrep rule: python.lang.security.audit.os-system-injection
    os.system("ping -c 1 " + target)
    
    return "Ping executed"

def hash_data(data):
    # Vulnerability 4: Insecure Cryptographic Hash
    # Semgrep rule: python.lang.security.audit.insecure-hash-algorithms
    return hashlib.md5(data.encode()).hexdigest()

if __name__ == '__main__':
    # Vulnerability 5: Debug mode enabled in production
    # Semgrep rule: python.flask.security.dangerous-app-run
    app.run(host='0.0.0.0', port=5000, debug=True)
