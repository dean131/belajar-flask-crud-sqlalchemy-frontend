from app import app
from flask import render_template

@app.route('/index')
def index():
    return render_template('index1.html')