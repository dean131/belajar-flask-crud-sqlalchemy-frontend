from app import app
from flask import render_template, session

@app.route('/')
@app.route('/index')
def f_index():
    # if session['email'] not in session:
    #     return render_template('login.html')
    return render_template('login.html')

@app.route('/admin')
@app.route('/inputUser')
def f_admin():
    return render_template('admFormUsr.html')

@app.route('/tabelUsers')
def f_tabelUsers():
    return render_template('admTblUsrs.html')