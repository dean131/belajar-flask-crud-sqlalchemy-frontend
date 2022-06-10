from app import app
from flask import render_template

@app.route('/')
def f_index():
    return render_template('home.html')

@app.route('/admin')
@app.route('/inputUser')
def f_admin():
    return render_template('admFormUsr.html')

@app.route('/tabelUsers')
def f_tabelUsers():
    return render_template('admTblUsrs.html')