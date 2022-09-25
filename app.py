from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)