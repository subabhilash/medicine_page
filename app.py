from flask import Flask, render_template, request
import mysql.connector
from database import mydb, load_db


app = Flask(__name__)

@app.route('/')
def hello_world():
  patients = load_db()
  return render_template('home.html', patients=patients)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)