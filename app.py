from flask import Flask, request, jsonify, render_template, send_from_directory
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('oven_records.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS records
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         duration INTEGER,
         status TEXT,
         timestamp TEXT)
    ''')
    conn.commit()
    conn.close()

# Add root route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/records', methods=['POST'])
def add_record():
    data = request.json

    conn = sqlite3.connect('oven_records.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO records (duration, status, timestamp)
        VALUES (?, ?, ?)
    ''', (data['duration'], data['status'], data['timestamp']))

    conn.commit()
    conn.close()

    return jsonify({'status': 'success'}), 200

@app.route('/api/records', methods=['GET'])
def get_records():
    conn = sqlite3.connect('oven_records.db')
    c = conn.cursor()

    c.execute('SELECT * FROM records ORDER BY timestamp DESC LIMIT 100')
    records = c.fetchall()

    conn.close()

    return jsonify([{
        'id': r[0],
        'duration': r[1],
        'status': r[2],
        'timestamp': r[3]
    } for r in records])

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
